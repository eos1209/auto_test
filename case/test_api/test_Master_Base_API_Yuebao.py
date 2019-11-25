'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import account_management
from master_api.account_login import User


class YuebaoBaseTest(unittest.TestCase):
    """ 余额宝 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.yuebaoBoard = account_management.YuebaoBoard(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_Yuebao_relatedApi_status_01(self):
        """驗證 余额宝 - 取得看板頁面"""
        data = {}
        response_data = self.yuebaoBoard.index(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_02(self):
        """驗證 余额宝 - 取得看板列表資料"""
        data = {"pageSize": 100,
                "search": {}}
        response_data = self.yuebaoBoard.list(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_03(self):
        """驗證 余额宝 - 取得總計數據"""
        data = {}
        response_data = self.yuebaoBoard.summary(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
