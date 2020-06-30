'''
@Created by Jo
@Date : 2020/05/20
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement, retentionListUsers
from master_api.Home import Home
from master_api.account_login import User
from data_config.system_config import systemSetting


class RetentionListUsers(unittest.TestCase):
    """ 會員流失預測 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.home = Home(self.__http)
        self.siteParameter = retentionListUsers(self.__http)
        self.user.login()

    # 登出
    def tearDown(self):
        self.user.logout()

    def getlist(self):
        data = {"pageSize": 25,
                "pageIndex": 0}
        items = self.siteParameter.GetList(data)
        for i in range(len(items[1]['ReturnObject'])):
            MemberId = items[1]['ReturnObject'][i]['MemberId']
        return MemberId

    def test_RetentionListUsers_relatedApi_status_01(self):
        """驗證 會員流失預測 - 獲取計算時間 狀態"""
        data = {}
        response_data = self.siteParameter.GetComputeTime(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RetentionListUsers_relatedApi_status_02(self):
        """驗證 會員流失預測 - 取得列表 狀態"""
        data = {"pageSize": 25,
                "pageIndex": 0}
        response_data = self.siteParameter.GetList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RetentionListUsers_relatedApi_status_03(self):
        """驗證 會員流失預測 - 取得詳細列表 狀態"""
        data = {"memberId": self.getlist()}
        response_data = self.siteParameter.GetDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RetentionListUsers_relatedApi_status_04(self):
        """驗證 會員流失預測 - 匯出檔案 狀態"""
        data = {}
        response_data = self.siteParameter.Export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
