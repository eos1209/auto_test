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
        self.siteParameter = PortalManagement.MobileTheme(self.__http)
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
        """ 主題設置 - 獲取主題設置獲取手機域名 直向&橫向 狀態"""
        ID = self.getWebsiteId()
        IsHorizontalType = ["false", "true"]
        for i in IsHorizontalType:
            data = {"WebSiteId": ID,
                    "IsHorizontal": i
                    }
            response_data = self.siteParameter.GetMobileTheme(data)
            print(response_data[0])
            print(response_data[1])
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_GetMobileTheme_relatedApi_status_02(self):
        """ 主題設置 - 獲取手機 - 色系列表 直向&橫向 狀態"""
        ID = self.getWebsiteId()
        IsHorizontalType = ["false", "true"]
        for i in IsHorizontalType:
            data = {"WebSiteId": ID,
                    "IsHorizontal": i
                    }
            response_data = self.siteParameter.GetMobileThemeDomain(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    # def test_AddColor_relatedApi_status_03(self):
    #     """ 主題設置 - 另存色系tag 直向&橫向 狀態"""
    #     ID = self.getWebsiteId()
    #     data = {
    #         "WebsiteId": ID,
    #         "ColorName": "極緻黑9453",
    #         "NewColorCode": {
    #             "--login-bg": "#1C1717",
    #             "--login-color": "#ff3682",
    #             "--login-input-bg": "#ff8929",
    #             "--login-input-color": "#fff",
    #             "--login-btn-bg": "#ff3c6d",
    #             "--login-btn-color": "#fff",
    #             "--header-bg-top": "#fff",
    #             "--header-bg-bottom": "#d5d5d6",
    #             "--header-domain-color": "#1C1717",
    #             "--header-domain-color2": "#e83347",
    #             "--btn01-bg": "#ec692e",
    #             "--btn01-color": "#fff",
    #             "--btn02-bg": "#df3070",
    #             "--btn02-color": "#fff",
    #             "--news-bg": "#ea073f",
    #             "--news-color": "#fff",
    #             "--lobby-bg": "#fff",
    #             "--lobby-color": "#ea073f",
    #             "--lobby-color2": "#1C1717",
    #             "--game-bg": "#ea073f",
    #             "--game-color": "#fff",
    #             "--footer-bg-top": "#1C1717",
    #             "--footer-bg-bottom": "#cacacc",
    #             "--footer-color": "#1C1717",
    #             "--footer-line": "#ddd",
    #             "--profile-bg": "#fff",
    #             "--profile-color": "#ea073f",
    #             "--nav-bg": "#ea073f",
    #             "--nav-color": "#fff",
    #             "--nav-color2": "#f6527a",
    #             "--page-title-bg": "#5a158c",
    #             "--page-title-color": "#fff",
    #             "--content-bg": "#fff",
    #             "--content-color": "#000",
    #             "--content-color2": "#fe0095",
    #             "--promo-btn-bg": "#df3070",
    #             "--promo-btn-color": "#fff",
    #             "--promo-title-bg": "#ea073f",
    #             "--promo-title-color": "#fff",
    #             "--promo-content-bg": "#fff",
    #             "--promo-content-color": "#5a158c"
    #         },
    #         "ThemeId": "1",
    #         "IsHorizontal": "false"
    #     }
    #     response_data = self.siteParameter.AddColor(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)
    #
    # def test_UpdateColorName_relatedApi_status_04(self):
    #     """ 主題設置 - 修改色系tag名稱 直向&橫向 狀態"""
    #     ID = self.getWebsiteId()
    #     data = {"MobileThemeSettingId": "22",
    #             "NewName": "極緻黑666",
    #             "IsHorizontal": "false"
    #             }
    #     response_data = self.siteParameter.UpdateColorName(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
