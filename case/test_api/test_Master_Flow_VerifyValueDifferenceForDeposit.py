'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import time
import unittest

from parameterized import parameterized

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import memeber_and_agent
from master_api.account_login import User


class VerifyValueDifferenceForDeposit(unittest.TestCase):
    """驗證人工存款流程"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = memeber_and_agent.MemberSearch(self.__http)
        self.memberDeposit = memeber_and_agent.MemberDeposit(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @parameterized.expand([
        ("verify_deposit_none_manual", "None", 4),
        ("verify_deposit_none_bonus", "None", 5),
        ("verify_deposit_none_discount", "None", 6),
        ("verify_deposit_none_reissuePayOff", "None", 7),
        ("verify_deposit_none_other", "None", 99),
        ("verify_deposit_deposit_manual", "Deposit", 4),
        ("verify_deposit_deposit_bonus", "Deposit", 5),
        ("verify_deposit_deposit_discount", "Deposit", 6),
        ("verify_deposit_deposit_reissuePayOff", "Deposit", 7),
        ("verify_deposit_deposit_other", "Deposit", 99),
        ("verify_deposit_discount_manual", "Discount", 4),
        ("verify_deposit_discount_bonus", "Discount", 5),
        ("verify_deposit_discount_discount", "Discount", 6),
        ("verify_deposit_discount_reissuePayOff", "Discount", 7),
        ("verify_deposit_discount_other", "Discount", 99),
    ])
    def testCase(self, name, audit_type, select_type):
        # 測試案例名稱、稽核方式、类型
        # Step1 取得目前帳戶餘額
        data = {"Account": "QAUser",
                "connectionId": self.user.info()}
        response_data = self.memberSearch.search(data)
        self.beforeDepositSumBalance = response_data[1]['PageData'][0]['Balance']

        # Step2 取得人工存入的token
        response_data = self.memberDeposit.deposit_token()

        # Step 人工存入api 呼叫
        data = {"AccountsString": "QAUser",
                "AmountString": "1",
                "AuditType": audit_type,
                "Audit": "0.01",
                "Type": select_type,
                "IsReal": 'false',
                "Memo": "test",
                "PortalMemo": "",
                "Password": "123456",
                "DepositToken": response_data[1],
                "TimeStamp": time.time()}
        self.response_data = self.memberDeposit.deposit_submit(data)

        # Step5 再次取得目前帳戶餘額
        data = {'Account': 'QAUser'}
        response_data = self.memberSearch.get_detail(data)
        self.afterDepositSumBalance = response_data[1]['Member']['Balance']

        # Step6 進行驗證
        self.assertEqual(int(self.afterDepositSumBalance) - int(self.beforeDepositSumBalance), 1)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
