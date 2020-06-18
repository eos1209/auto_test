'''
@Created by Jo
@Date : 2020/06/16
'''

import unittest
import random
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import JackPotActivity
from master_api.Home import Home
from master_api.account_login import User
from data_config.system_config import systemSetting
from base import TimeClass


class ThirdPartyPayoutBaseTest(unittest.TestCase):
    """ GPK活動記錄 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.home = Home(self.__http)
        self.siteParameter = JackPotActivity(self.__http)
        self.user.login()

    # 登出
    def tearDown(self):
        self.user.logout()

    def getIDlist(self):
        """取一筆ID"""
        data = {
            "pageSize": 100,
            "pageIndex": 0,
            "search": {
            }
        }
        items = self.siteParameter.GetList(data)
        for i in range(len(items[1]['ReturnObject'])):
            ID = items[1]['ReturnObject'][i]['Id']
        return ID

    def getJoinIDlist(self):
        """取一筆ID"""
        data = {
            "id": self.getIDlist(),
            "pageSize": 100,
            "pageIndex": 0,
            "search": {
            }
        }
        items = self.siteParameter.GetJoinList(data)
        for i in range(len(items[1]['ReturnObject'])):
            MemberId = items[1]['ReturnObject'][i]['MemberId']
        return MemberId

    def test_JackPotActivity_relatedApi_status_01(self):
        """驗證 GPK活動記錄 - 取得列表 狀態"""
        data = {
            "pageSize": 100,
            "pageIndex": 0,
            "search": {
            }
        }
        response_data = self.siteParameter.GetList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_JackPotActivity_relatedApi_status_02(self):
        """驗證 GPK活動記錄 - 獲取加入列表 狀態"""
        data = {
            "id": self.getIDlist(),
            "pageSize": 100,
            "pageIndex": 0,
            "search": {
            }
        }
        response_data = self.siteParameter.GetJoinList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_JackPotActivity_relatedApi_status_03(self):
        """驗證 GPK活動記錄 - 獲取加入列表以獲取全部信息 狀態"""
        data = {
            "id": self.getIDlist(),
            "search": {
            }
        }
        response_data = self.siteParameter.GetJoinListTotalInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_JackPotActivity_relatedApi_status_04(self):
        """驗證 GPK活動記錄 - 獲取加入列表活動信息 狀態"""
        data = {
            "id": self.getIDlist()
        }
        response_data = self.siteParameter.GetJoinListActivityInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_JackPotActivity_relatedApi_status_05(self):
        """驗證 GPK活動記錄 - 獲取加入列表活動信息 狀態"""
        data = {
            "id": self.getIDlist(),
            "memberId": self.getJoinIDlist()
        }
        response_data = self.siteParameter.GetJoinDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_JackPotActivity_relatedApi_status_06(self):
        """驗證 GPK活動記錄 - 匯出Excel 狀態"""
        data = {
            "id": self.getIDlist()
        }
        response_data = self.siteParameter.JoinListExport(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_JackPotActivity_relatedApi_status_07(self):
        """驗證 GPK活動記錄 - GPK活动钱包额度转移记录搜尋 狀態"""
        data = {
            "StartTime": TimeClass.get_yesterdayS(),
            "EndTime": TimeClass.get_todaynowS(),
            "IsAllGameSupplier": 'true',
            "pageIndex": 0,
            "pageSize": 10
        }
        response_data = self.siteParameter.Search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
