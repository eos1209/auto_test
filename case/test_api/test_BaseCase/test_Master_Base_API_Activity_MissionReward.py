'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest
from datetime import datetime, timedelta

from base.CommonMethod import UploadFile
from base.CommonMethod import system_config_Setting
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from data_config.system_config import systemSetting
from master_api.account_login import User
from master_api.system_management import ActivityManagement
from base.CommonMethod import PortalExecution
from master_api import account_management
from base.CommonMethod import Portal_test


class MissionRewardBaseTest(unittest.TestCase):
    """ 任务挑战 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.missionReward = ActivityManagement.MissionReward(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        data = {"take": 100,
                "skip": 0,
                "search": {}}
        response_data = self.missionReward.getList(data)
        return response_data[1][0]['Id']

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.thirdPartyPayment = account_management.ThirdPartyPayment(cls.__http)
        cls.user.login()

    def create_missionReward(self, mode):
        self.upload = UploadFile('image/jpg/test_jpg.jpg', 'ImageFile', 'test_jpg.jpg')
        data = self.upload.Upload_file()
        response_data = self.missionReward.uploadImage(data)
        self.upload.Close_file()
        self.system = system_config_Setting()
        BeginTime = (datetime.now() + timedelta(hours = -12)).strftime("%Y/%m/%d %H:%M:%S")
        EndTime = (datetime.now() + timedelta(hours = -11)).strftime("%Y/%m/%d %H:%M:%S")
        receiveBonusLimitTime = (datetime.now() + timedelta(hours = +12)).strftime("%Y/%m/%d %H:%M:%S")  # 領獎
        if mode == 1:
            data = {"taskCount": 1, "activityStartTime": BeginTime,
                    "item": [{"title": "A", "type": 2,
                              "img": {"$ngfBlobUrl": "blob:" + self.config.Master_config() + '/'},
                              "setting": 1,
                              "bonus": 1, "auditTimes": 1,
                              "imgStatus": 2, "imgErrorMsg": "",
                              "imageUrl": response_data[1]['ReturnObject'],
                              "errorFile": 'null',
                              "category": 'null',
                              "categoryFullName": 'null',
                              "gameCategoryPropertyNames": 'null'}],
                    "name": "QA_Test",
                    "activityEndTime": EndTime,
                    "receiveBonusLimitTime": receiveBonusLimitTime,
                    "receiveBonusDays": 1,
                    "registerStartTime": "", "registerEndTime": "", "completeBonus": 1,
                    "completeAuditTimes": 1, "memberLevelSettingIds": [self.system.getMemberLevelId()]}
            return data

    def test_MissionReward__relatedApi_status_01(self):
        """驗證 任务挑战 - 取得列表資料"""
        data = {"take": 100,
                "skip": 0,
                "search": {}}
        response_data = self.missionReward.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MissionReward__relatedApi_status_02(self):
        """驗證 任务挑战 - 取得任務種類 狀態"""
        response_data = self.missionReward.getConditionType({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MissionReward__relatedApi_status_03(self):
        """驗證 任务挑战 - 上傳任務圖片 狀態"""
        self.upload = UploadFile('image/jpg/test_jpg.jpg', 'ImageFile', 'test_jpg.jpg')
        data = self.upload.Upload_file()
        response_data = self.missionReward.uploadImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()

    def test_MissionReward__relatedApi_status_04(self):
        """驗證 任务挑战 - 新增任務挑戰 狀態"""
        data = self.create_missionReward(1)
        response_data = self.missionReward.create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MissionReward__relatedApi_status_05(self):
        """驗證 任务挑战 - 任務詳細資料 狀態"""
        Id = self.getId()
        data = {"Id": Id}
        response_data = self.missionReward.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MissionReward__relatedApi_status_06(self):
        """驗證 任务挑战 - 修改領獎期限 狀態"""
        Id = self.getId()
        NewTime = (datetime.now() + timedelta(hours = +12)).strftime("%Y/%m/%d %H:%M:%S")  # 領獎
        data = {"Id": Id, "NewTime": NewTime}
        response_data = self.missionReward.updateReceiveBonusLimitTime(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MissionReward__relatedApi_status_07(self):
        """驗證 任务挑战 - 取得任務挑戰名稱 狀態"""
        Id = self.getId()
        data = {"Id": Id}
        response_data = self.missionReward.getEventName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MissionReward__relatedApi_status_08(self):
        """驗證 任务挑战 - 取得任務挑戰參與名單 狀態"""
        Id = self.getId()
        data = {"id": Id, "take": 100, "skip": 0, "search": {}}
        response_data = self.missionReward.getJoinList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MissionReward__relatedApi_status_09(self):
        """驗證 任务挑战 - Portal任務挑戰 狀態"""
        self.portal = Portal_test()
        self.portal.OnlineDeposit_Create_V2(self.config.test_Member_config(), self.config.test_Password_config())
        self.portal.OnlineDeposit_Send_V2(self.config.test_Member_config(), self.config.test_Password_config())
        MissionRewardBaseTest.Master_login()  # 線上支付看板-同意
        data = {"count": 25, "query": {"isDTPP": 'true', "search": 'null'}}
        response_data = self.thirdPartyPayment.load_new(data)
        getId = response_data[1]['Data'][0]['Id']
        data = {'id': getId}
        self.thirdPartyPayment.allow_dTPP_manual(data)
        Id = self.getId()
        validateData = self.portal.MissionReward(self.config.test_Member_config(), self.config.test_Password_config(),
                                                 Id)
        self.assertEqual(validateData, True)

    def test_MissionReward__relatedApi_status_10(self):
        """驗證 任务挑战 - 立即下架 狀態"""
        Id = self.getId()
        NewEndTime = (datetime.now() + timedelta(hours = -12)).strftime("%Y/%m/%d %H:%M:%S")  # 領獎
        data = {"Id": Id, "NewEndTime": NewEndTime}
        response_data = self.missionReward.eventOff(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
