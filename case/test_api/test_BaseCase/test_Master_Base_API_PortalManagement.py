'''
@Created by loka
@Date : 2020/01/03
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import system_management
from master_api.account_login import User


class PortalManagementBaseTest(unittest.TestCase):
    """ 前台網站管理列表 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.PortalManagement = system_management.PortalManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_PortalManagement_relatedApi_status_01(self):
        """驗證 前台網站管理列表 - 取得前台網站管理列表"""
        response_data = self.PortalManagement.getWebsiteList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalManagement_relatedApi_status_02(self):
        """驗證 前台網站管理列表 - 取得會員端設定"""
        response_data = self.PortalManagement.getPortalSettings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalManagement_relatedApi_status_03(self):
        """驗證 前台網站管理列表 - 更新前台網站管理列表"""
        data = {"Id": 29,
                "Code": "AB005-01",
                "Name": "AB005-01",
                "Url": "http://www.fnjtd.com/",
                "MobileUrl": "http://m2.fnjtd.com",
                "Memo": "AB005611211",
                "DefaultAgentAccount": "GPK_D",
                "AnyTimeDiscountPromotionStatus": 'true',
                "PortalSetting": {"Id": 0, "Name": "Default12"},
                "MemberRegisterVerifySwitch": 'false',
                "PortalSettingId": 0,
                "PortalSettingName": "Default12",
                "editable": 'false',
                "oldValues": {"DefaultAgentAccount": "GPK_D"},
                "isProcessing": 'true'}
        response_data = self.PortalManagement.updateWebsite(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
