'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User


class GameSupplierTransactionBaseTest(unittest.TestCase):
    """ 娛樂城轉帳紀錄查詢 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.gameSupplierTransaction = reports.GameSupplierTransaction(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_GameSupplierTransaction_relatedApi_status_01(self):
        """驗證 娛樂城轉帳紀錄查詢 - 取得頁面狀態"""
        response_data = self.gameSupplierTransaction.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameSupplierTransaction_relatedApi_status_02(self):
        """驗證 娛樂城轉帳紀錄查詢 - 搜尋"""
        data = {
            "Account": "hsiang",
            "transactionDateBegin": common_config.BeginDate,
            "transactionDateEnd": common_config.EndDate
        }
        response_data = self.gameSupplierTransaction.search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameSupplierTransaction_relatedApi_status_03(self):
        """驗證 娛樂城轉帳紀錄查詢 - 匯出"""
        data = {"Account": "hsiang",
                "transactionDateBegin": common_config.BeginDate,
                "transactionDateEnd": common_config.EndDate
                }
        response_data = self.gameSupplierTransaction.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
