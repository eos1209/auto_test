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


class CheckInEventBaseTest(unittest.TestCase):
    """ 签到奖励 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.checkInEvent = ActivityManagement.CheckInEvent(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_CheckInEvent_Get_List_Data(self):
        """驗證 签到奖励 - 取得列表資料"""
        data = {"take": 100,
                "skip": 0,
                "query": {"AllState": True,
                          "StatusList": [0, 1, 2]}
                }
        response_data = self.checkInEvent.loadNew(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_CheckInEvent_Get_List_Data(self):
    #     """驗證 签到奖励 - 新增簽到獎勵"""
    #     data = {
    #         "BeginTime": "2020/05/01 00:02:47",
    #         "EventSettings": [
    #         ],
    #         "CheckType": 2,
    #         "IsSupplement": 'true',
    #         "SupplementSetting": {
    #             "SettlementType": 1,
    #             "DepositTotalCount": 1,
    #             "DepositTotalAmount": 1
    #         },
    #         "Name": "22",
    #         "EndTime": "2020/08/31 23:59:59",
    #         "DailyCheckMoney": 1,
    #         "MemberLevelSettings": [
    #             62]
    #     }
    #     response_data = self.checkInEvent.Create(data)
    #     print(response_data[1])
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
