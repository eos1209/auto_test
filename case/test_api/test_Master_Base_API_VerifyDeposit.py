'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import account_management
from master_api.account_login import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


# Portal 前端月底調整

class VerifyDepositBaseTest(unittest.TestCase):
    """ 公司入款审核 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.verify_deposit = account_management.VerifyDeposit(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def Portal_VerifyDeposit(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://fnjtd.com/")
        self.driver.find_element_by_id("login_account").send_keys("DS_player8")
        self.driver.find_element_by_id("login_password").send_keys("a123456")
        self.driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("e5466e48e20e4944a0bdaa6bac351c8d")
        sleep(2)
        self.driver.find_element_by_id("login-box").click()
        sleep(2)
        self.driver.get("http://fnjtd.com/Deposit")
        sleep(2)
        self.driver.find_element_by_link_text("公司入款").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".custom-deposit-border-color:nth-child(2)").click()
        self.driver.find_element(By.NAME, "accountId").click()
        element = self.driver.find_element(By.NAME, "accountId")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".footer-btn:nth-child(4) > .ng-binding").click()
        self.driver.find_element(By.ID, "amount").click()
        self.driver.find_element(By.ID, "amount").send_keys("1")
        self.driver.find_element(By.ID, "depositName").click()
        self.driver.find_element(By.ID, "depositName").send_keys("@QA_automation")
        self.driver.find_element(By.CSS_SELECTOR, ".footer-btn > .ng-binding:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".deposit-finish:nth-child(2) > .ng-binding").click()
        self.driver.close()

    def test_VerifyDeposit_relatedApi_status_01(self):
        """驗證 公司入款审核 - 取得頁面"""
        # response_data = self.verifyDeposit.index(data)
        # self.Portal_VerifyDeposit()
        response_data = self.verify_deposit.get_index_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_02(self):
        """驗證 公司入款审核 - 取得列表資料"""
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verify_deposit.get_load_data(data)
        status_code = response_data[0]
        self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_03(self):
        """驗證 公司入款审核 - 匯出"""
        data = {"search": None}
        response_data = self.verify_deposit.export_data(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_04(self):
        """驗證 公司入款审核 - 取得訂單狀態"""
        response_data = self.verify_deposit.get_apply_states({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_05(self):
        """驗證 公司入款审核 - 取得詳細頁面"""
        response_data = self.verify_deposit.get_detail_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_06(self):
        """驗證 公司入款审核 - 取得詳細資料"""
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verify_deposit.get_load_data(data)
        self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']

        data = {"id": self.get_verify_deposit_id}
        response_data = self.verify_deposit.get_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
