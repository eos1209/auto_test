'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import unittest
from time import sleep

from parameterized import parameterized

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import master_config
from master_api import member_and_agent
from master_api.account_login import User
from base.CommonMethod import SetDelayTime


class VerifyValueDifferenceForWithdraw(unittest.TestCase):
    """驗證人工提款流程"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = member_and_agent.MemberSearch(self.__http)
        self.memberWithdraw = member_and_agent.MemberWithdraw(self.__http)
        self.user.login()

    @parameterized.expand([
        ("驗證提款類型手冊Verify_withdraw_type_manual", 4),
        ("驗證提款類型獎金Verify_withdraw_type_bonus", 5),
        ("驗證提現類型折扣Verify_withdraw_type_discount", 6),
        ("確認提款類型重新簽發Verify_withdraw_type_reissuePayOff", 7),
        ("驗證提款類型其他Verify_withdraw_type_other", 99),
    ])
    def testCase(self, name, withdraw_type):
        # 測試案例名稱、提款類型
        # 因修改查詢頻率限制
        # sleep(1.5)
        SetDelayTime()
        # Step1 取得目前帳戶餘額
        data = {"Account": "QAUser",
                "connectionId": self.user.info()}
        response_data = self.memberSearch.search(data)
        self.beforeWithdrawSumBalance = response_data[1]['PageData'][0]['Balance']

        # Step2 取得會員ID
        data = {"Account": "QAUser"}
        response_data = self.memberSearch.get_detail(data)
        self.memberId = response_data[1]['Member']['Id']

        # Step3 人工提出 api 呼叫
        data = {"id": self.memberId,
                "money": 5,
                "type": withdraw_type,
                "password": master_config.Master_Password,
                "isReal": 'false',
                "memo": "test123"}
        self.submit = self.memberWithdraw.withdraw_submit(data)

        # Step4 再次取得目前帳戶餘額
        # sleep(1.5)
        SetDelayTime()
        data = {'Account': 'QAUser',
                'connectionId': self.user.info()}
        response_data = self.memberSearch.search(data)
        self.afterWithdrawSumBalance = response_data[1]['PageData'][0]['Balance']

        # Step5 進行驗證
        self.assertEqual(int(self.beforeWithdrawSumBalance) - int(self.afterWithdrawSumBalance), 5)

    def tearDown(self):
        self.user.logout()


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
