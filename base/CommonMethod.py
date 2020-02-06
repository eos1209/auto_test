'''
@Created by yuhsiang
@Date : 2019/12/17
'''

import logging
from data_config import common_config
from selenium import webdriver
from time import sleep
from data_config import portal_config
import time


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


class UploadFile(object):
    # 上傳檔案
    def __init__(self, path, upload_name, filename):
        self.path = common_config.file_Path + path  # 檔案路徑
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


class PortalExecution(object):
    # Portal端
    def __init__(self):
        self.chrome_Path = "D:\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_Path)
        self.windowSize = self.driver.set_window_size(1900, 1020)
        self.link = self.driver.get(portal_config.Portal_address)

    def Login(self, Account, Password):  # 登入
        sleep(3)
        self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="login_account"]').send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(Password)  # 會員密碼
        self.driver.find_element_by_xpath('//*[@id="check-code-wrapper"]/input').send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login-box"]').click()
        sleep(3)

    def Register(self, Account):  # 註冊
        sleep(3)
        self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="account-box"]/form/button[2]').click()
        sleep(3)
        self.driver.find_element_by_id("parentAccount").send_keys("QA_Test11070110")
        self.driver.find_element_by_xpath("//fieldset[1]/div[2]/div[1]/input").send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath("//fieldset[1]/div[3]/div[1]/input").send_keys("a123456")  # 會員密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[4]/div[1]/input").send_keys("a123456")  # 確認密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[5]/div[1]/input").send_keys("123456")  # 取款密碼
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-submit']").click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[14]/div/div/div[3]/button[2]').click()

    def SetBankAccount(self, Account, Password):  # 設定銀行帳戶
        self.Login(Account, Password)
        sleep(2)
        self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="account-nav"]/ul/li[2]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="inputProvince"]').send_keys('QATest')  # 省分
        self.driver.find_element_by_xpath('//*[@id="inputCity"]').send_keys('QATest')  # 縣市
        self.driver.find_element_by_xpath('//*[@id="inputAccount"]').send_keys(int(time.time()))  # 銀行帳號
        self.driver.find_element_by_xpath('//*[@id="account-panel"]/div[2]/form/div[5]/div/button').click()  # 提交

    def ChangePassword(self, Account, Password):  # 修改密碼
        self.Login(Account, Password)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[1]/div/div/input').send_keys(
            Password)  # 原始密碼
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[2]/div/div/input').send_keys(
            'a123456')  # 新密碼
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[3]/div/div/input').send_keys(
            'a123456')  # 確認新密碼
        self.driver.find_element_by_xpath('//*[@id="change-pwd"]/div[2]/form/div[4]/div/button[1]').click()  # 變更
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[13]/div/div/div[3]/ button[2]').click()
        sleep(2)

    def Trail(self):  # 試玩帳號註冊
        sleep(3)
        self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/ul/li[1]/a').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[13]/div/div/div/div/div[2]/form/input').send_keys(
            int(time.time()))  # 手機號碼
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/body/div[13]/div/div/div/div/div[2]/form/div[1]/input').send_keys(
            portal_config.PortalCheckCode)  # 驗證碼
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/body/div[13]/div/div/div/div/div[2]/form/button[1]').click()  # 提交
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[14]/div/div/div[3]/button[2]').click()  # 確定

    def Trail_Login(self, account, password):  # 試玩帳號登入
        self.Trail()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/body/div[13]/div/div/div/div/div[2]/form/input[1]').send_keys(account)  # 試玩帳號
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/body/div[13]/div/div/div/div/div[2]/form/input[2]').send_keys(password)  # 試玩密碼
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ng-app"]/body/div[13]/div/div/div/div/div[2]/form/button').click()  # 立即試玩

    def close(self):
        self.driver.close()
