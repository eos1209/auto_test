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


class TimeLimitedEventBaseTest(unittest.TestCase):
    """ 限时优惠 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.timeLimitedEvent = ActivityManagement.TimeLimitedEvent(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_TimeLimitedEvent_relatedApi_status_01(self):
        """驗證 限时优惠 - 取得列表資料"""
        data = {"websiteId": 29, "count": 100, "skip": 0, "query": {"AllState": True, "StatusList": [0, 1, 2]}}
        response_data = self.timeLimitedEvent.loadNew(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TimeLimitedEvent_relatedApi_status_02(self):
        """驗證 限时优惠 - 取得活動名稱"""
        data = {"id": 290}
        response_data = self.timeLimitedEvent.getEventName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TimeLimitedEvent_relatedApi_status_03(self):
        """驗證 限时优惠 - 取得活動詳細資料"""
        data = {"id": 290}
        response_data = self.timeLimitedEvent.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TimeLimitedEvent_relatedApi_status_04(self):
        """驗證 限时优惠 - 取得活動會員參與名單"""
        data = {"id": "290", "take": 100, "skip": 0, "query": {}}
        response_data = self.timeLimitedEvent.memberJoinListLoadNew(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
