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


class CommissionServiceBaseTest(unittest.TestCase):
    """佣金计算 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.commissionService = account_management.CommissionService(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_CommissionService_relatedApi_status_01(self):
        """驗證 佣金计算 - 取得頁面(新)"""
        response_data = self.commissionService.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionService_relatedApi_status_02(self):
        """驗證 佣金计算 - 取得結果(新)"""
        data = {"param": {"DateBegin": common_config.BeginDate,
                          "DateEnd": common_config.EndDate},
                "connectionId": self.user.info()}
        response_data = self.commissionService.getCommission(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_CommissionService_relatedApi_status_03(self):
    #     """驗證 佣金计算 - 匯出"""
    #     data = {}
    #     response_data = self.commissionService.export(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, config.Status_Code)
    #
    # def test_CommissionService_relatedApi_status_04(self):
    #     """驗證 佣金计算 - 匯出(個別代理)"""
    #     data = {"date": config.TodayDate,
    #             "halfYear": "false",
    #             "gameSupplier": 41}
    #     response_data = self.commissionService.exportDataToVerify(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
