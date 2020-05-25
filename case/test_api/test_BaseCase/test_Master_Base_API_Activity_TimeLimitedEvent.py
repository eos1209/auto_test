'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest
import random

from time import sleep
from datetime import datetime, timedelta
from master_api.account_login import User
from master_api.system_management import ActivityManagement
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from data_config.system_config import systemSetting
from base.CommonMethod import system_config_Setting
from base.CommonMethod import GameHallType


class TimeLimitedEventBaseTest(unittest.TestCase):
    """ 限时优惠 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.timeLimitedEvent = ActivityManagement.TimeLimitedEvent(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def create_NewTimeLimitdEvent(self):  # 新增限時優惠活動
        BeginTime = (datetime.now() + timedelta(hours=-12)).strftime("%Y/%m/%d %H:%M:%S")
        EndTime = (datetime.now() + timedelta(hours=-11)).strftime("%Y/%m/%d %H:%M:%S")
        people = random.randint(0, 200)
        data = {"BeginTime": BeginTime,
                "IsApplyRepeatable": "true",
                "CommissionSettings": [],
                "BonusSettings": [
                    {
                        "AuditTimes": 1,
                        "Bonus": 1,
                        "DepositAmount": 1,
                        "isInsert": "true"
                    }],
                "Name": "QATEST",
                "EndTime": EndTime,
                "MaxApplyCount": people,  # 上限人次
                "ImageUrl": "/Cdn2Redirect/Web.Portal/Image/TimeLimitedEvent/Upload/BannerImages/4ef443a80847486c839bcd5251dbc47e.png",
                "BonusGameCategories": [
                    "Im2Slot",
                    "Im2Board"],  # 發送平台-選擇遊戲的類型
                "MemberLevelSettings": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24, 26,
                                        27, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 40, 43, 45, 46, 47, 48, 49, 50, 51,
                                        52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66],  # 會員等級 - 全選
                "MemberJoinTimeStart": "Invalid date",
                "MemberJoinTimeEnd": "Invalid date"
                }
        return data

    def getTimeLimitdEventId(self):
        """取得ID"""
        data = {"count": 100,
                "skip": 0,
                "query": {"AllState": "true",
                          "StatusList": [0, 1]  # [0, 1, 2]讀全部的列表 ，[0, 1]讀已開始列表
                          }
                }
        response_data = self.timeLimitedEvent.loadNew(data)
        for i in range(len(response_data[1]['ReturnObject']['TimeLimitedEvents'])):
            if response_data[1]['ReturnObject']['TimeLimitedEvents'][i]['Name'] == 'QATEST':
                Id = response_data[1]['ReturnObject']['TimeLimitedEvents'][i]['Id']
                return Id

    def test_TimeLimitedEvent_relatedApi_status_01(self):
        """驗證 限时优惠 - 取得列表資料"""
        data = {"websiteId": 29,
                "count": 100,
                "skip": 0,
                "query": {"AllState": True,
                          "StatusList": [0, 1, 2]}
                }
        response_data = self.timeLimitedEvent.loadNew(data)
        # print(response_data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)  # 驗證回傳200碼

    def test_TimeLimitedEvent_relatedApi_status_02(self):
        """驗證 限时优惠 - 新增限時優惠"""
        data = self.create_NewTimeLimitdEvent()
        response_data = self.timeLimitedEvent.Create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TimeLimitedEvent_relatedApi_status_03(self):
        """驗證 限时优惠 - 取得活動詳細資料"""
        Id = self.getTimeLimitdEventId()
        data = {"id": Id}
        response_data = self.timeLimitedEvent.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TimeLimitedEvent_relatedApi_status_04(self):
        """驗證 限时优惠 - 取得活動會員參與名單"""
        Id = self.getTimeLimitdEventId()
        data = {"id": Id, "take": 100, "skip": 0, "query": {}}
        response_data = self.timeLimitedEvent.memberJoinListLoadNew(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TimeLimitedEvent_relatedApi_status_05(self):
        """驗證 限时优惠 - 取得活動名稱"""
        Id = self.getTimeLimitdEventId()
        data = {"id": Id}
        response_data = self.timeLimitedEvent.getEventName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TimeLimitedEvent_relatedApi_status_06(self):
        """驗證 限時優惠 - 立即下架 狀態"""
        Id = self.getTimeLimitdEventId()
        data = {"eventID": Id}
        response_data = self.timeLimitedEvent.eventOff(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
