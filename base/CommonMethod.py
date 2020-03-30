'''
@Created by yuhsiang
@Date : 2019/12/17
'''

import logging
from data_config import common_config
from data_config.system_config import systemSetting
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep
from master_api import reports
from master_api import Home
from data_config import portal_config
import time
from master_api.system_management import PortalManagement
from master_api.account_login import User
from base.httpRequest import HttpRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def get_logger():
    global logPath
    try:
        logPath
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    return logging


def SetDelayTime():
    # 因修改查詢頻率限制抽公用
    sleep(common_config.DelayTime)


class system_config_Setting(object):
    # 抓取所有的接口分類/Home底下、返水等級、會員等級
    def __init__(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.user.login()
        self.home = Home.Home(self.__http)

    def getDiscountSettingId(self):  # 返水設定
        response_data = self.home.getAllDiscountSettings({})
        for i in range(len(response_data[1])):
            if self.config.DiscountSetting_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def getMemberLevelId(self):  # 會員等級
        level = self.home.getAllMemberLevels({})
        for i in range(len(level[1])):
            if self.config.MemberLevelSetting_config() == level[1][i]['Text']:
                Id = level[1][i]['Value']
                return Id


class GameHallType(object):
    # 活動類娛樂城種類
    def __init__(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.user.login()
        self.betRecord = reports.BetRecords(self.__http)

    def GameCategories(self):
        # 取得娛樂城種類
        gameCategories = []
        response_data = self.betRecord.getSupplierCategories({})
        categories = len(response_data[1])
        print(categories)  # 總共娛樂城數量
        for i in range(categories):
            for j in range(len(response_data[1][i]['Categories'])):
                gameCategories.append(response_data[1][i]['Categories'][j]['PropertyName'])
        return gameCategories


class UploadFile(object):
    # 上傳檔案
    def __init__(self, path, upload_name, filename):
        file_path = 'D:/automation_test_project/test_data/' + path  # 檔案路徑
        self.path = os.path.abspath(file_path)
        self.upload_name = upload_name  # 上傳欄位
        self.filename = filename  # 上傳檔名
        self.open_file = open(self.path, 'rb')  # 開啟檔案
        Type = path.split('/')  # 以檔案資料夾路徑來判斷檔案上傳類型，採切割字串方式
        if Type[0] == 'document':
            self.file_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳類型
        elif Type[0] == 'image':
            if Type[1] == 'png':
                self.file_type = 'image/png'  # 上傳類型
            elif Type[1] == 'jpg':
                self.file_type = 'image/jpeg'  # 上傳類型
            elif Type[1] == 'gif':
                self.file_type = 'image/gif'  # 上傳類型

    def Upload_file(self):  # 上傳檔案-方法
        data = {self.upload_name: (self.filename, self.open_file, self.file_type, {'Expires': '0'})}
        return data

    def Close_file(self):  # 檔案關閉-方法
        self.open_file.close()


class IsAnnouncementList(object):  # 判斷前台管理後端的公告是否有開啟，減少因為公告關係而讓案例發生錯誤
    def __init__(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.AnnouncementManagement = PortalManagement.AnnouncementManagement(self.__http)
        self.user.login()

    def getWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.siteName_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def IsEnable(self):
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1"}
        response_data = self.AnnouncementManagement.getAnnouncementList(data)
        for i in range(len(response_data[1]['List'])):
            if bool(response_data[1]['List'][i]['IsEnable'] == True):  # 檢查 Portal端的公告設定狀態
                return 'true'

        return 'false'

    def logout(self):
        self.user.logout()


class PortalExecution(object):
    # Portal端
    def __init__(self):
        self.config = systemSetting()  # 參數設定
        path = "D:/chromedriver.exe"
        self.chrome_Path = os.path.abspath(path)
        self.driver = webdriver.Chrome(self.chrome_Path)
        self.windowSize = self.driver.maximize_window()
        self.link = self.driver.get(self.config.Portal_config())
        self.IsEnableAnnouncementList = IsAnnouncementList()  # 公告判斷

    def Login(self, Account, Password):  # 登入
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(3)
        self.IsEnableAnnouncementList.logout()
        self.driver.find_element_by_xpath('//*[@id="login_account"]').send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(Password)  # 會員密碼
        self.driver.find_element_by_xpath('//*[@id="check-code-wrapper"]/input').send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login-box"]').click()
        sleep(3)

    def Login_Fail(self, Account, Password):
        self.Login(Account, Password)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "btn-confirm")))
            self.driver.find_element_by_class_name('btn-confirm').click()
        finally:
            self.driver.quit()

    def Register(self, Account):  # 註冊
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(3)
        self.driver.find_element_by_xpath('//*[@id="account-box"]/form/button[2]').click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-click').click()  # 其他選項
        sleep(2)
        self.driver.find_element_by_id("parentAccount").send_keys(self.config.agentLv4())
        self.driver.find_element_by_xpath("//fieldset[1]/div[2]/div[1]/input").send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath("//fieldset[1]/div[3]/div[1]/input").send_keys("a123456")  # 會員密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[4]/div[1]/input").send_keys("a123456")  # 確認密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[5]/div[1]/input").send_keys("123456")  # 取款密碼
        sleep(1)
        self.driver.find_element_by_xpath("//*[@ng-model='scope.params.Name']").send_keys('QATest')  # 真實姓名
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-submit']").click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-confirm').click()

    def SetBankAccount(self, Account, Password):  # 設定銀行帳戶
        self.Login(Account, Password)
        sleep(7)
        self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(1)
        self.driver.find_element_by_xpath('//*[@id="account-nav"]/ul/li[2]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="inputProvince"]').send_keys('QATest')  # 省分
        self.driver.find_element_by_xpath('//*[@id="inputCity"]').send_keys('QATest')  # 縣市
        self.driver.find_element_by_xpath('//*[@id="inputAccount"]').send_keys(int(time.time()))  # 銀行帳號
        self.driver.find_element_by_xpath('//*[@id="account-panel"]/div[2]/form/div[5]/div/button').click()  # 提交
        self.driver.quit()

    def ChangePassword(self, Account, Password):  # 修改密碼
        self.Login(Account, Password)
        sleep(7)
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[1]/div/div/input').send_keys(
            Password)  # 原始密碼
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[2]/div/div/input').send_keys(
            'a123456')  # 新密碼
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[3]/div/div/input').send_keys(
            'a123456')  # 確認新密碼
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[4]/div/button[1]').click()  # 變更
        sleep(2)
        self.driver.find_element_by_class_name('btn-confirm').click()
        sleep(2)

    def Trail(self):  # 試玩帳號註冊
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(3)
        self.driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/ul/li[1]/a').click()
        sleep(3)
        self.driver.find_element_by_class_name('mobile').send_keys(int(time.time()))  # 手機號碼
        self.driver.find_element_by_name('checkCode').send_keys(portal_config.PortalCheckCode)  # 驗證碼
        sleep(2)
        self.driver.find_element_by_class_name('modal-nt-apply').click()  # 提交
        sleep(2)
        self.driver.find_element_by_class_name('btn-confirm').click()  # 確定

    def Trail_Login(self, account, password):  # 試玩帳號登入
        self.Trail()
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(account)  # 試玩帳號
        self.driver.find_element_by_name('password').send_keys(password)  # 試玩密碼
        sleep(2)
        self.driver.find_element_by_class_name('modal-nt-login').click()
        sleep(2)
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(2)
        trailAccount = self.driver.find_element_by_class_name('account').text
        self.driver.quit()
        return trailAccount

    def resetMoneyPassword(self, account, password, MoneyPassword):  # 變更取款密碼
        newpassword = '123456'
        self.Login(account, password)
        sleep(7)
        self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(2)
        self.IsEnableAnnouncementList.logout()
        self.driver.find_element_by_xpath('//*[@id="account-nav"]/ul/li[5]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="change-money-pwd"]/div[2]/div/div/form/div[1]/div/div/input').send_keys(MoneyPassword)
        self.driver.find_element_by_xpath(
            '//*[@id="change-money-pwd"]/div[2]/div/div/form/div[2]/div/div/input').send_keys(newpassword)
        self.driver.find_element_by_xpath(
            '//*[@id="change-money-pwd"]/div[2]/div/div/form/div[3]/div/div/input').send_keys(newpassword)
        self.driver.find_element_by_xpath(
            '//*[@id="change-money-pwd"]/div[2]/div/div/form/div[4]/div/button[1]').click()
        sleep(1)
        self.driver.find_element_by_class_name('btn-confirm').click()
        self.driver.quit()

    def verifyWithdraw(self, account, password, MoneyPassword):  # 線上取款  ---PS:該登入會員必須先設定好銀行帳戶+支付寶帳戶
        self.Login(account, password)
        sleep(7)
        self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(2)
        self.driver.find_element_by_xpath('//*[@id="account-nav"]/ul/li[2]/a').click()
        sleep(2)
        self.driver.find_element_by_name('amount').send_keys('1')
        self.driver.find_element_by_id('money-pwd-input').send_keys(MoneyPassword)
        self.driver.find_element_by_class_name('btn-submit').click()
        sleep(5)
        self.driver.find_element_by_class_name('btn-confirm').click()
        self.driver.quit()

    def verifyDeposit(self, account, password):  # 公司入款 - 微信支付
        self.Login(account, password)
        sleep(1)
        self.driver.get(self.config.Portal_config() + '/CompanyDeposit/NewIndex')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div[1]/div[1]/form/div[3]/div/div[1]/div/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/form/div[4]/button').click()
        self.driver.find_element_by_xpath('//*[@id="amount"]').send_keys('5')
        self.driver.find_element_by_xpath('//*[@id="depositName"]').send_keys('QA_automation')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[2]/form/div/button[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
        sleep(2)
        verifyDepositId = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[2]/ul/li[5]').text
        self.driver.quit()
        return verifyDepositId  # 訂單號

    def ThirdPartyPayment(self, account, password):  # 線上支付
        self.Login(account, password)
        sleep(1)
        self.driver.get(self.config.Portal_config() + self.config.verifyDeposit())  # 方案C:銀聯條碼支付
        sleep(5)
        self.driver.find_element_by_name('amount').send_keys('1')
        sleep(5)
        self.driver.find_element_by_xpath('*//form/div[3]/button').click()
        sleep(2)
        # self.driver.quit()

    def SiteMail(self, account, password):  # 站內信件
        self.Login(account, password)
        sleep(1)
        self.driver.get(self.config.Portal_config() + '/SiteMail')
        sleep(2)
        self.driver.find_element_by_class_name('btn-primary').click()
        sleep(5)
        self.driver.find_element_by_name('subject').send_keys('@auto_SiteMail_ByPortal')
        sleep(10)
        self.driver.find_element_by_class_name('cke_button__horizontalrule_icon').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[13]/div/div/form/div[2]/button[2]').click()
        sleep(1)
        self.driver.find_element_by_class_name('btn-confirm').click()
        sleep(2)
        self.driver.quit()

    def AgentLink(self, link, Account):
        self.driver.get(link)
        sleep(7)
        validateIsEnable = self.IsEnableAnnouncementList.IsEnable()
        if validateIsEnable == 'true':  # 判斷公告是否有開啟
            self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
            sleep(2)
        self.driver.find_element_by_xpath('//*[@id="account-box"]/form/button[2]').click()
        sleep(3)
        self.driver.find_element_by_xpath("//fieldset[1]/div[2]/div[1]/input").send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath("//fieldset[1]/div[3]/div[1]/input").send_keys("a123456")  # 會員密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[4]/div[1]/input").send_keys("a123456")  # 確認密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[5]/div[1]/input").send_keys("123456")  # 取款密碼
        sleep(1)
        self.driver.find_element_by_xpath("//*[@ng-model='scope.params.Name']").send_keys('QATest')  # 真實姓名
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-submit']").click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-confirm').click()
        self.driver.quit()

    def NewLuckyWheel(self, account, password):
        self.Login(account, password)
        self.driver.get(self.config.Portal_config() + '/NewLuckyWheel')
        sleep(1)
        for i in range(5):
            self.driver.find_element_by_class_name('arrow').click()
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/button')))
                self.driver.find_element_by_xpath('/html/body/div[3]/div/div/button').click()
            except:
                result = 'Fail'
                return result
        self.driver.quit()
        result = 'Success'
        return result

    def MissionReward(self):
        self.driver.get(self.config.Portal_config() + '/MissionReward')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div/div[3]/ul/li/span').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[3]/div/div/div[3]/button[2]').click()
