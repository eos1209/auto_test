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


class DiscountBaseTest(unittest.TestCase):
    """ 返水计算 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.discount = account_management.Discount(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_discount_relatedApi_status_01(self):
        """驗證 返水计算 - 取得頁面"""
        response_data = self.discount.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_02(self):
        """驗證 返水计算 - 載入歷史資料"""
        data = {"take": 100,
                "skip": 0}
        response_data = self.discount.loadHistory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_03(self):
        """驗證 返水計算 - 清除Temp 狀態"""
        data = {}
        response_data = self.discount.ClearTemp(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)



if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
