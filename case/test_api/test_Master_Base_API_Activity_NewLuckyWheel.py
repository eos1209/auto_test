'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from master_api.account_login import User
from master_api.system_management import ActivityManagement
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config


class NewLuckyWheelBaseTest(unittest.TestCase):
    """ 时来运转 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.newLuckyWheel = ActivityManagement.NewLuckyWheel(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_NewLuckyWheel_relatedApi_status_01(self):
        """驗證 时来运转 - 取得列表資料"""
        data = {"websiteId": 29, "skip": 0, "take": 100, "search": {"AllState": True, "Status": [0, 1, 2]}}
        response_data = self.newLuckyWheel.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
