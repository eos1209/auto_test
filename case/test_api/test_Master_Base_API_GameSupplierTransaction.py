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
        data = {}
        response_data = self.gameSupplierTransaction.index(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameSupplierTransaction_relatedApi_status_02(self):
        """驗證 娛樂城轉帳紀錄查詢 - 搜尋"""
        data = {
            "Account": "hsiang",
            "Suppliers": ["1", "3", "6", "9", "11", "12", "13", "14", "15", "16", "17", "21", "25", "26", "27",
                          "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42",
                          "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "54", "55", "56", "57", "58",
                          "59", "60", "61", "62", "63", "64", "65"],
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
    unittest.main(testRunner=HTMLTestRunner())
