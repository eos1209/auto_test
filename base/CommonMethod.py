'''
@Created by yuhsiang
@Date : 2019/12/17
'''

import logging
from data_config import common_config
from data_config.system_config import systemSetting
from selenium import webdriver
from time import sleep
from master_api import reports
from master_api import Home
from data_config import portal_config
import time
from master_api.account_login import User
from base.httpRequest import HttpRequest
import random
import os
from portal_api.portal_api import Portal_api
from base.TimeClass import get_todaynow


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

    def getMemberLevelId_2(self):  # 會員等級_2
        level = self.home.getAllMemberLevels({})
        for i in range(len(level[1])):
            if self.config.MemberLevelSetting_2_config() == level[1][i]['Text']:
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
            elif Type[1] == 'ico':
                self.file_type = 'image/ico'  # 上傳類型

    def Upload_file(self):  # 上傳檔案-方法
        data = {self.upload_name: (self.filename, self.open_file, self.file_type, {'Expires': '0'})}
        return data

    def Close_file(self):  # 檔案關閉-方法
        self.open_file.close()


class Portal_test:
    def __init__(self):
        self.portal = Portal_api()  # 實作API
        self.config = systemSetting()  # 系統參數

    def login(self, Account, Passowrd):
        getImg = self.portal.get_login_image()
        Img = getImg[1]["value"]  # 取得驗證碼
        # print(Img)
        data = {"account": Account,
                "password": Passowrd,
                "checkCode": portal_config.PortalCheckCode,
                "checkCodeEncrypt": Img
                }
        response_data = self.portal.portal_login(data)
        cookie = response_data[2]
        # print(cookie)
        return cookie

    def Trail(self):
        getImg = self.portal.get_trail_image()
        Img = getImg[1]["value"]  # 取得驗證碼
        data = {"number": str(int(time.time())), "checkCode": portal_config.PortalCheckCode, "columnType": 1,
                "checkCodeEncrypt": Img}
        self.portal.portal_trial(data)

    def changePassword(self, Account, Password):
        cookie = self.login(Account, Password)
        data = {"oldPassword": Password, "newPassword": "a123456"}
        self.portal.portal_changePassword(data, cookie)

    def setBankAccount(self, Account, Password):  # 設定銀行帳號
        cookie = self.login(Account, Password)
        data = {"BankName": {"Id": 1, "Name": "农业银行", "Sort": 1, "AccountFormat": 2}, "Province": "vvvvvvv",
                "City": "aaa", "Account": str(int(time.time())), "GroupBankId": 1}
        self.portal.portal_setBankAccount(data, cookie)

    def resetMoneyPassword(self, account, password, MoneyPassword):  # 重設取款密碼
        new_password = '123456'
        cookie = self.login(account, password)
        data = {"oldPassword": MoneyPassword, "newPassword": new_password}
        self.portal.portal_resetMoneyPassword(data, cookie)

    def verifyDraw(self, Account, Password, MoneyPassword):  # 取款
        cookie = self.login(Account, Password)
        type = random.randint(1, 2)
        data = {"withdrawType": type, "amount": "1", "moneyPassword": MoneyPassword}
        self.portal.portal_verifyDraw(data, cookie)

    def siteMail(self, Account, Password):  # 前端寄信
        cookie = self.login(Account, Password)
        data = {"Subject": "dfgdfg", "MailBody": "<p>dfgdfgdfgfd</p>\n"}
        self.portal.portal_siteMail(data, cookie)

    def CompanyDeposit(self, Account, Password):  # 公司入款
        cookie = self.login(Account, Password)
        data = {"accountId": 802, "amount": 6, "depositName": "@QA_automation", "groupAccountType": "Alipay",
                "bankId": "Alipay", "time": get_todaynow()}
        self.portal.portal_CompanyDeposit(data, cookie)

    def OnlineDeposit_Create_V2(self, Account, Password):
        cookie = self.login(Account, Password)
        data = {"amount": 10, "settingId": 828, "paymentyType": 1}
        self.portal.portal_OnlineDeposit_Create_V2(data, cookie)

    def OnlineDeposit_Send_V2(self, Account, Password):
        cookie = self.login(Account, Password)
        data = {"amount": 10, "settingId": 828, "paymentyType": 1}
        self.portal.portal_OnlineDeposit_Send_V2(data, cookie)

    def RedEnvelope_Received(self, Account, Password, master_Id):
        cookie = self.login(Account, Password)
        data = {}
        response_data = self.portal.portal_Get_RedEnvelopeList(data, cookie)
        Id = response_data[1][0]['Id']
        recordId = response_data[1][0]['RecordId']
        if recordId == master_Id:
            data = {'id': Id}
            response_data = self.portal.portal_RedEnvelope_Recevied(data, cookie)
            return response_data[1]['IsSuccess']
        else:
            return '會員沒有領到紅包'

    def AnytimeDiscount_Received(self, Account, Password):
        cookie = self.login(Account, Password)
        data = {}
        response_data = self.portal.portal_GetMemberDiscountDetail(data, cookie)
        if response_data[1]['TotalAmount'] != 0:
            response_data = self.portal.portal_ReceiveMemberAnyTimeDiscount(data, cookie)
            if response_data[0] == 200:
                message = '會員領取時返成功'
                return message
        else:
            message = '該會員沒有時時返水'
            return message

    def luckyWheel(self, Account, Password, luckyWheel_id, serialNumber):
        cookie = self.login(Account, Password)
        data = {'eventID': luckyWheel_id, 'account': Account, 'serialNumber': serialNumber}
        self.portal.portal_LuckyWheel_inputSerialNumber(data, cookie)  # 輸入序號
        data = {'eventID': luckyWheel_id, 'account': Account}
        self.portal.portal_LuckyWheel_startRaffle(data, cookie)  # 抽獎

    def newLuckyWheel(self, Account, Password, newLuckyWheel_id):
        cookie = self.login(Account, Password)
        data = {'luckywheelId': newLuckyWheel_id}
        response_data = self.portal.portal_NewLuckyWheel_startRaffle(data, cookie)
        return response_data[1]['IsSuccess']

    def MissionReward(self, Account, Password, Id):
        cookie = self.login(Account, Password)
        data = {'id': Id}
        response_data = self.portal.portal_missionReward(data, cookie, Id)
        getId = response_data[1]['ReturnObject'][0]['Id']
        data = {'id': getId}
        response_data = self.portal.portal_missionReward_CompleteMission(data, cookie)
        return response_data[1]['IsSuccess']


class PortalExecution(object):
    # Portal端
    def __init__(self):
        self.config = systemSetting()  # 參數設定
        path = "D:/chromedriver.exe"
        self.chrome_Path = os.path.abspath(path)
        self.driver = webdriver.Chrome(self.chrome_Path)
        self.windowSize = self.driver.maximize_window()
        self.link = self.driver.get(self.config.Portal_config())

    def Login(self, Account, Password):  # 登入
        self.driver.find_element_by_xpath('//*[@id="login_account"]').send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(Password)  # 會員密碼
        self.driver.find_element_by_xpath('//*[@id="check-code-wrapper"]/input').send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login-box"]').click()
        sleep(3)

    def Register(self, Account):  # 註冊
        self.driver.get(self.config.Portal_config() + '/Register')
        sleep(2)
        self.driver.find_element_by_id("parentAccount").send_keys(self.config.agentLv4())
        self.driver.find_element_by_xpath("//fieldset[1]/div[2]/div[1]/input").send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath("//fieldset[1]/div[3]/div[1]/input").send_keys("a123456")  # 會員密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[4]/div[1]/input").send_keys("a123456")  # 確認密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[5]/div[1]/input").send_keys("123456")  # 取款密碼
        sleep(3)
        self.driver.find_element_by_xpath("//*[@ng-model='scope.params.Name']").send_keys('QATest')  # 真實姓名
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-submit']").click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-confirm').click()
        self.driver.quit()

    def Trail(self):  # 試玩帳號註冊
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
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
        # self.driver.find_element_by_xpath('//*[@id="marquee"]/footer/span').click()
        # self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(account)  # 試玩帳號
        self.driver.find_element_by_name('password').send_keys(password)  # 試玩密碼
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[12]/div/div/div/div/div[2]/form/button').click()
        sleep(2)
        trailAccount = self.driver.find_element_by_class_name('account').text
        self.driver.quit()
        return trailAccount

    def AgentLink(self, link, Account):
        self.link = self.driver.get(link)
        self.driver.find_element_by_xpath('//*[@id="account-box"]/form/button[2]').click()
        sleep(3)
        self.driver.find_element_by_xpath("//fieldset[1]/div[2]/div[1]/input").send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath("//fieldset[1]/div[3]/div[1]/input").send_keys("a123456")  # 會員密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[4]/div[1]/input").send_keys("a123456")  # 確認密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[5]/div[1]/input").send_keys("123456")  # 取款密碼
        sleep(1)
        self.driver.find_element_by_xpath("//*[@ng-model='scope.params.Name']").send_keys('QATest')  # 真實姓名
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-submit']").click()
        sleep(3)
        self.driver.find_element_by_class_name('btn-confirm').click()
        self.driver.quit()
