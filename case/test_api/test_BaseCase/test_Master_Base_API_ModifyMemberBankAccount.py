'''
@Created by yuhsiang
@Date : 2019/6/4
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from data_config.system_config import systemSetting


class MemberSearchModifyBankAccountTest(unittest.TestCase):
    """Master 會員- 更新修改銀行帳戶"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearchPage = member_and_agent.MemberSearch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_Member_Modify_BankAccount_Is_Normal(self):
        """驗證-會員正常更新修改銀行帳戶"""
        data = {"memberAccount": self.config.test_Member_config(),
                "GroupBankId": 3,
                "Province": '江西省',
                "City": '南昌市',
                "Account": '354564456',
                "ForceUpdate": False}
        response_data = self.memberSearchPage.update_bank_account(data)
        status_code = response_data[0]
        self.assertEqual(common_config.Status_Code, status_code)
        # returnStatus = response_data[1]['IsSuccess']
        # self.assertEqual(returnStatus, True)

    def test_Member_Modify_BankAccount_Account_Is_Null(self):
        """驗證-會員更新修改銀行帳戶-帳戶為空"""
        data = {"memberAccount": '',
                "GroupBankId": 3,
                "Province": '江西省',
                "City": '南昌市',
                "Account": '354564456',
                "ForceUpdate": False}
        response_data = self.memberSearchPage.update_bank_account(data)
        status_code = response_data[0]
        self.assertEqual(common_config.Status_Code, status_code)
        # status = response_data[1]['IsSuccess']
        # self.assertEqual(False, status)

    def test_Member_Modify_BankAccount_Account_Ali_pay(self):
        """驗證-會員更新修改銀行帳戶-帳戶為空"""
        data = {"memberAccount": self.config.test_Member_config(),
                "GroupBankId": 1,
                "Province": "江西省",
                "City": "南昌市",
                "Account": "475644134131",
                "Memo": None,
                "AlipayAccount": "\yuhsiang@tabo.com",
                "AlipayNickName": "qa",
                "AlipayMemo": "test",
                "ForceUpdate": True}
        response_data = self.memberSearchPage.update_bank_account(data)
        status_code = response_data[0]
        self.assertEqual(common_config.Status_Code, status_code)
        # returnStatus = response_data[1]['IsSuccess']
        # self.assertEqual(returnStatus, False)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
