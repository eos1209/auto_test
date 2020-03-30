'''
@Created by loka
@Date : 2020/03/10
'''
from data_config.system_config import systemSetting
from selenium import webdriver
from time import sleep
from master_api.system_management import PortalManagement
from master_api.account_login import User
from base.httpRequest import HttpRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_config import portal_config
import os


class mobileExecution(object):
    # Mobile端
    def __init__(self):
        self.config = systemSetting()  # 參數設定
        path = "D:/chromedriver.exe"
        self.chrome_Path = os.path.abspath(path)
        option = webdriver.ChromeOptions()
        mobile_emulation = {"deviceName": "iPhone X"}
        option.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(self.chrome_Path, chrome_options = option)
        self.windowSize = self.driver.maximize_window()
        self.link = self.driver.get(self.config.Mobile_config())

    def UI_AnyTimeDiscount(self, version):
        if version == 'L':
            sleep(3)
            self.driver.find_element_by_xpath(
                '/html/body/plan-shared-root-component/root-component/r-footer-component/footer/ul/li[3]')
            AntTimeDiscount = self.driver.find_element_by_xpath(
                "//footer/ul/li[3]/a[3]/span").text  # 時時返水
            return AntTimeDiscount

    def AnyTimeDiscount_process(self, verison, Account, Password):
        if verison == 'L':
            sleep(3)
            self.driver.find_element_by_xpath(
                '/html/body/plan-shared-root-component/root-component/r-footer-component/footer/ul/li[3]').click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="login_account"]').send_keys(Account)  # 會員帳號
            self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(Password)  # 會員密碼
            self.driver.find_element_by_xpath('//*[@id="check-code-wrapper"]/input').send_keys(
                portal_config.PortalCheckCode)  # 萬用碼
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="account-box"]/form/button').click()  # 登入
            self.driver.find_element_by_xpath(
                '/html/body/plan-shared-root-component/root-component/r-footer-component/footer/ul/li[3]').click()

    def mobile_Login(self, Account, Password):  # 帳號、密碼、登入版型
        self.driver.get(self.config.Mobile_config())
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="login_account"]').send_keys(Account)  # 會員帳號
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(Password)  # 會員密碼
        self.driver.find_element_by_xpath('//*[@id="check-code-wrapper"]/input').send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="account-box"]/form/button').click()  # 登入
        self.driver.find_element_by_xpath(
            '/html/body/plan-shared-root-component/root-component/v-modal-page-component/div/vl-login-component/div/form/button')

    def mobile_Login_Fail(self, Account, Password):  # 登入失敗
        self.mobile_Login(Account, Password)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "btn-confirm")))
            self.driver.find_element_by_class_name('btn-confirm').click()
        finally:
            self.driver.quit()

    def mobile_RedEnvelope(self, Account, Password):  # 搶紅包
        self.mobile_Login(Account, Password)
        sleep(5)
        self.driver.get(self.config.Mobile_config() + '/redEnvelope')
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="red-envelope"]/re-layout-component/div/div/div[2]/div/div[1]').click()
        sleep(5)
        self.driver.find_element_by_class_name("btn-withdraw").click()
        sleep(5)
        # self.driver.find_element_by_xpath('/html/body/div[1]').click()
        self.driver.quit()
