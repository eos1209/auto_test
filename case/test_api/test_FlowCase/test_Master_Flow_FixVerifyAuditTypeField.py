'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import time
import unittest

from parameterized import parameterized

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import master_config
from master_api import member_and_agent
from master_api.account_login import User


class FixVerifyAuditTypeField(unittest.TestCase):
    """驗證存款類型於即時稽核顯示邏輯"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = member_and_agent.MemberSearch(self.__http)
        self.memberDeposit = member_and_agent.MemberDeposit(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @parameterized.expand([
        # 免稽核 - 優惠金額
        ("verify_audit_type_field", "None", 5),
        ("verify_audit_type_field", "None", 6),
        # 存款稽核 - 存款金額
        ("verify_audit_type_field", "Deposit", 5),
        ("verify_audit_type_field", "Deposit", 6),
        # 優惠稽核 - 優惠金額
        ("verify_audit_type_field", "Discount", 5),
        ("verify_audit_type_field", "Discount", 6),
    ])
    def testCase(self, name, audit_type, select_type):
        # 測試案例名稱、稽核方式、类型
        # Step1 取得人工存入的token
        response_data = self.memberDeposit.deposit_token({})

        # Step2 人工存入api 呼叫
        data = {"AccountsString": master_config.Test_Account,
                "AmountString": "1",
                "AuditType": audit_type,
                "Audit": 0.01,
                "Type": select_type,
                "IsReal": 'false',
                "Memo": "test",
                "PortalMemo": "",
                "Password": "123456",
                "DepositToken": response_data[1],
                "TimeStamp": time.time()}
        self.submit = self.memberDeposit.deposit_submit(data)

        # Step3 取得目前帳戶即時稽核詳細
        data = {"account": master_config.Test_Account}
        response_data = self.memberSearch.get_audit_detail(data)
        deposit_amount = response_data[1]['WithdrawAuditDataList'][0]['Amount']
        discount_amount = response_data[1]['WithdrawAuditDataList'][0]['Discount']

        if audit_type == "None" and (not [discount_amount] is None):
            flag_status = True
        elif audit_type == "Deposit" and (not [deposit_amount] is None):
            flag_status = True
        elif audit_type == "Discount" and (not [discount_amount] is None):
            flag_status = True
        else:
            flag_status = False

        # Step4 進行驗證
        self.assertEqual(flag_status, True)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
