'''
@Created by yuhsiang
@Date : 2019/4/19
'''

import unittest
from time import sleep
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User


class MemberSearchAdjustReturnErrorMessage(unittest.TestCase):
    """会员查询：調整回傳錯誤訊息"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = member_and_agent.MemberSearch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_member_search_request_payload_have_connectionId(self):
        """驗證 会员查询 Request Payload 有帶 Connection Id"""
        data = {"Account": "hsiang",
                "connectionId": self.user.info()}
        response_data = self.memberSearch.search(data)
        error_message = response_data[1]['ErrorMessage']
        self.assertEqual(error_message, None)

    def test_member_search_request_payload_have_not_connectionId(self):
        """驗證 会员查询 Request Payload 未帶 Connection Id"""
        # 因修改查詢頻率限制
        sleep(1.5)
        data = {"Account": "hsiang"}
        response_data = self.memberSearch.search(data)
        error_message = response_data[1]['ErrorMessage']
        self.assertEqual(error_message, "connectionId cannot be null.")


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
