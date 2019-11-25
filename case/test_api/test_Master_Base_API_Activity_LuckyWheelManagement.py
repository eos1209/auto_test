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


class LuckyWheelManagementBaseTest(unittest.TestCase):
    """ 幸运转盘 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.luckyWheelManagement = ActivityManagement.LuckyWheelManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_LuckyWheelManagement_relatedApi_status_01(self):
        """驗證 幸运转盘 - 取得列表資料"""
        data = {"Size": 100, "IsPending": True, "IsStart": True, "IsEnd": True}
        response_data = self.luckyWheelManagement.getEventList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
