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
from data_config.system_config import systemSetting


class PortalManagementBaseTest(unittest.TestCase):
    """ 前台網站管理列表 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.PortalManagement = system_management.PortalManagement(self.__http)
        self.portalSetting = system_management.PortalSetting(self.__http)
        self.user.login()

    def getWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        print(response_data[1])
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.siteName_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def getPortalSettingId(self):
        response_data = self.portalSetting.getList({})
        for i in range(len(response_data[1])):
            if self.config.siteName_config() == response_data[1][i]['Name']:
                Id = response_data[1][i]['Id']
                return Id

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
        data = {"Id": self.getWebsiteId(),
                "Code": self.config.siteName_config(),
                "Name": self.config.siteName_config(),
                "Url": self.config.Portal_config(),
                "MobileUrl": self.config.Mobile_config(),
                "Memo": "AB005-01資料勿亂動",
                "DefaultAgentAccount": self.config.agentLv4(),
                "AnyTimeDiscountPromotionStatus": 'true',
                "PortalSetting": {"Id": self.getPortalSettingId(), "Name": "Default12"},
                "MemberRegisterVerifySwitch": 'false',
                "PortalSettingId": self.getPortalSettingId(),
                "PortalSettingName": "Default12",
                "editable": 'false',
                "oldValues": {"DefaultAgentAccount": self.config.agentLv4()},
                "isProcessing": 'true'}
        response_data = self.PortalManagement.updateWebsite(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
