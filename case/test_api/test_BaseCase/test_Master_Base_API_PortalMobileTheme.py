'''
@Created by loka
@Date : 2020/01/20
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement
from master_api.account_login import User
from data_config.system_config import systemSetting


class SiteParameterBaseTest(unittest.TestCase):
    """ 主題設置 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = PortalManagement.MobileMenu(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    # 登出
    def tearDown(self):
        self.user.logout()

    # 取站台ID
    def getWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.siteName_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def test_BeforeLoggingIn_relatedApi_status_01(self):
        """ 主題設置 - 取得選單管理登入前 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "device": "2"}
        response_data = self.siteParameter.GetList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
