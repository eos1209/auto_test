'''
@Created by yuhsiang
@Date : 2018/12/7
'''
import time
import unittest
from parameterized import parameterized
from data_config import master_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from base.CommonMethod import SetDelayTime
from master_api import member_and_agent
from master_api.account_login import User
from data_config.system_config import systemSetting


class VerifyValueDifferenceForDeposit(unittest.TestCase):
    """驗證人工存款流程"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = member_and_agent.MemberSearch(self.__http)
        self.memberDeposit = member_and_agent.MemberDeposit(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @parameterized.expand([
        ("Verify_deposit_none_manual", "None", 4),  # Verify_deposit_none_manual 驗證存款_無手動
        ("Verify_deposit_none_bonus", "None", 5),  # Verify_deposit_none_bonus 驗證存款_無獎金
        ("Verify_deposit_none_discount", "None", 6),  # Verify_deposit_none_discount 驗證存款_無折扣
        ("Verify_deposit_none_reissuePayOff ", "None", 7),  # Verify_deposit_none_reissuePayOff 驗證存款_無重發送付款
        ("Verify_deposit_none_other", "None", 99),  # Verify_deposit_none_other 驗證存款_無其他
        ("Verify_deposit_deposit_manual", "Deposit", 4),  # Verify_deposit_deposit_manual 驗證存款_手動
        ("Verify_deposit_deposit_bonus", "Deposit", 5),  # Verify_deposit_deposit_bonus 驗證存款_獎金
        (" Verify_deposit_deposit_discount", "Deposit", 6),  # Verify_deposit_deposit_discount 驗證存款_折扣
        ("Verify_deposit_deposit_reissuePayOff", "Deposit", 7),  # Verify_deposit_deposit_reissuePayOff 驗證存款_重新發出付款
        ("Verify_deposit_deposit_other", "Deposit", 99),  # Verify_deposit_deposit_other 驗證存款_其他折扣
        ("Verify_deposit_discount_manual", "Discount", 4),  # Verify_deposit_discount_manual 驗證存款_折扣手冊
        ("Verify_deposit_discount_bonus ", "Discount", 5),  # Verify_deposit_discount_bonus 驗證存款_折扣獎金
        ("Verify_deposit_discount_discount ", "Discount", 6),  # Verify_deposit_discount_discount 驗證存款_折扣
        ("Verify_deposit_discount_reissuePayOff", "Discount", 7),  # Verify_deposit_discount_reissuePayOff驗證存款_折扣重新發行支付
        ("Verify_deposit_discount_other", "Discount", 99),  # Verify_deposit_discount_other 驗證存款_其他折扣
    ])
    def testCase(self, name, audit_type, select_type):
        # 測試案例名稱、稽核方式、类型
        # 因修改查詢頻率限制
        SetDelayTime()
        # Step1 取得目前帳戶餘額
        data = {"Account": self.config.test_Member_config(),
                "connectionId": self.user.info()}
        response_data = self.memberSearch.search(data)
        self.beforeDepositSumBalance = response_data[1]['PageData'][0]['Balance']

        # Step2 取得人工存入的token
        response_data = self.memberDeposit.deposit_token({})

        # Step 人工存入api 呼叫
        data = {"AccountsString": self.config.test_Member_config(),
                "AmountString": "1",
                "AuditType": audit_type,
                "Audit": "0.01",
                "Type": select_type,
                "IsReal": 'false',
                "Memo": "test",
                "PortalMemo": "",
                "Password": master_config.Master_Password,
                "DepositToken": response_data[1],
                "TimeStamp": time.time()}
        self.response_data = self.memberDeposit.deposit_submit(data)

        # Step5 再次取得目前帳戶餘額
        # 因修改查詢頻率限制
        SetDelayTime()
        data = {'Account': self.config.test_Member_config()}
        response_data = self.memberSearch.get_detail(data)
        self.afterDepositSumBalance = response_data[1]['Member']['Balance']

        # Step6 進行驗證
        self.assertEqual(int(self.afterDepositSumBalance) - int(self.beforeDepositSumBalance), 1)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
