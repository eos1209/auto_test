'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import account_management
from master_api.account_login import User


class MemberTransactionBaseTest(unittest.TestCase):
    """交易記錄查詢 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberTransaction = account_management.MemberTransaction(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberTransaction_baseApi_status_01(self):
        """驗證 交易記錄查詢頁面狀態"""
        data = {}
        response_data = self.memberTransaction.query(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_02(self):
        """驗證 取得交易紀錄類型狀態"""
        data = {}
        response_data = self.memberTransaction.queryInit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_03(self):
        """驗證 交易紀錄搜尋狀態"""
        data = {"Types": [
            "Account",
            "ThirdPartyPayment",
            "OnlineWithdraw",
            "Manual",
            "Bonus",
            "Discount",
            "Payoff",
            "AnyTimeDiscount",
            "Other"
        ]}
        response_data = self.memberTransaction.search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_04(self):
        """驗證 取得交易記錄詳細頁面狀態"""
        data = {}
        response_data = self.memberTransaction.detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_05(self):
        """驗證 取得單筆紀錄明細狀態"""
        data = {"id": 3468324}
        response_data = self.memberTransaction.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_MemberTransaction_baseApi_status_06(self):
    #     """驗證 更新實際存提狀態"""
    #     data = {"id": 3468324,
    #             "isReal": True}
    #     response_data = self.memberTransaction.updateIsReal(data)
    #     print(response_data)
    #     status_code = response_data[0]
    #     self.checkIfTheTestCaseIsPassOrFail(status_code)

    def test_MemberTransaction_baseApi_status_07(self):
        """驗證 匯出狀態"""
        data = {"Account": "hsiang",
                "TimeBegin": common_config.BeginDate,
                "Types": ["Account",
                          "ThirdPartyPayment",
                          "OnlineWithdraw",
                          "Manual",
                          "Bonus",
                          "Discount",
                          "Payoff",
                          "AnyTimeDiscount",
                          "Other"]}
        response_data = self.memberTransaction.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
