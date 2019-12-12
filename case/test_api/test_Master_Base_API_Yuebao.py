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


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
