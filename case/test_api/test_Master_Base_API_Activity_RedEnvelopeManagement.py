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


class RedEnvelopeManagementBaseTest(unittest.TestCase):
    """ 红包派送 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.redEnvelopeManagement = ActivityManagement.RedEnvelopeManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_RedEnvelopeManagement_relatedApi_status_01(self):
        """驗證 红包派送 - 取得列表資料"""
        data = {"take": 100, "skip": 0, "search": {}}
        response_data = self.redEnvelopeManagement.get_list(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_02(self):
        """驗證 红包派送 - 詳細資料"""
        data = {"id": 255}
        response_data = self.redEnvelopeManagement.get_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
