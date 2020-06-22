'''
@Created by loka
@Date : 2020/01/17
'''

import unittest
from time import sleep
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from base.CommonMethod import Portal_test


class TrailBaseTest(unittest.TestCase):
    """試玩審核 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.trail = member_and_agent.Trial(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        data = {"count": 100, "skip": 0}
        response_data = self.trail.load(data)
        Id = response_data[1][0]['Id']
        return Id

    def test_Trail_baseApi_status_01(self):
        """驗證 試玩審核 - 取得看板頁面"""
        response_data = self.trail.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_02(self):
        """驗證 試玩審核 - 取得試玩審核設定"""
        response_data = self.trail.getMemberTrialSetting({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_03(self):
        """驗證 試玩審核 - 讀取試玩帳號資料"""
        data = {"count": 100, "skip": 0}
        response_data = self.trail.load(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_04(self):
        """驗證 試玩審核 - 館端新增一組試玩"""
        response_data = self.trail.createNew({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_05(self):
        """驗證 試玩審核 - 更新自動審核按鈕"""
        data = {"isAuto": 'true'}
        response_data = self.trail.modifyAutoVerifyMemberTrial(data)
        status_code = response_data[0]
        data = {"isAuto": 'false'}
        self.trail.modifyAutoVerifyMemberTrial(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_06(self):
        """驗證 試玩審核 - 試玩轉跳設定"""
        data = {"trialViewType": 2}
        response_data = self.trail.modifyMemberTrialViewType(data)
        status_code = response_data[0]
        data = {"trialViewType": 1}
        self.trail.modifyMemberTrialViewType(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_07(self):
        """驗證 試玩審核 - 試玩申請欄位"""
        data = {"trialColumnType": 2}
        response_data = self.trail.modifyMemberTrialColumnType(data)
        status_code = response_data[0]
        data = {"trialColumnType": 1}
        self.trail.modifyMemberTrialColumnType(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_08(self):
        """驗證 試玩審核 - 允許試玩帳號"""
        self.portal = Portal_test()
        self.portal.Trail()
        Id = self.getId()
        data = {"id": Id}
        # print(Id)
        sleep(2)
        response_data = self.trail.allow(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Trail_baseApi_status_09(self):
        """驗證 試玩審核 - 拒絕試玩帳號"""
        self.portal = Portal_test()
        self.portal.Trail()
        Id = self.getId()
        data = {"id": Id}
        response_data = self.trail.deny(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
