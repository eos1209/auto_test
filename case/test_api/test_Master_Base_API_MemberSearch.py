'''
@Created by yuhsiang
@Date : 2019/4/19
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import memeber_and_agent
from master_api.account_login import User


class MemberSearchBaseTest(unittest.TestCase):
    """会员查询 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = memeber_and_agent.MemberSearch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberSearch_relatedApi_status_01(self):
        """驗證 会员查询頁面 狀態"""
        response_data = self.memberSearch.query_page()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_02(self):
        """驗證 会员查询 狀態"""
        data = {"Account": "hsiang",
                "connectionId": self.user.info()}
        response_data = self.memberSearch.search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_03(self):
        """驗證 会员查询 狀態"""
        data = {"Account": "hsiang"}
        response_data = self.memberSearch.search(data)
        error_message = response_data[1]['ErrorMessage']
        self.assertEqual(error_message, "connectionId cannot be null.")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
