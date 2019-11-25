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


class MissionRewardBaseTest(unittest.TestCase):
    """ 任务挑战 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.missionReward = ActivityManagement.MissionReward(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MissionReward_relatedApi_status_01(self):
        """驗證 任务挑战 - 取得列表資料"""
        data = {"take": 100, "skip": 0, "search": {}}
        response_data = self.missionReward.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
