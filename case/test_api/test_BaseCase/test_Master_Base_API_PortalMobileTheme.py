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


class MobileThemeManagementBaseTest(unittest.TestCase):
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

    def getThemeId(self, ID, databool):
        data = {"WebSiteId": ID,
                "IsHorizontal": databool
                }
        response_data = self.siteParameter.GetMobileTheme(data)
        ThemeId = response_data[1]['ReturnObject']['ThemeList'][0]['ThemeId']
        return ThemeId

    def getMobileThemeSettingId(self, ID, databool):
        data = {"WebSiteId": ID,
                "IsHorizontal": databool
                }
        index = {"ThemeId": "", "ThemeName": ""}
        response_data = self.siteParameter.GetMobileTheme(data)
        for i in range(len(response_data[1]['ReturnObject']['ThemeList'][0]['ColorCollection'])):
            index["ThemeId"] = response_data[1]['ReturnObject']['ThemeList'][0]['ColorCollection'][i][
                'MobileThemeSettingId']
            index["ThemeName"] = response_data[1]['ReturnObject']['ThemeList'][0]['ColorCollection'][i]['Name']
        return index

    def test_BeforeLoggingIn_relatedApi_status_01(self):
        """ 主題設置 - 獲取主題設置獲取手機域名 直向&橫向 狀態"""
        ID = self.getWebsiteId()
        IsHorizontalType = ["false", "true"]
        for i in IsHorizontalType:
            data = {"WebSiteId": ID,
                    "IsHorizontal": i
                    }
            response_data = self.siteParameter.GetMobileTheme(data)
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

    def test_AddColor_relatedApi_status_03(self):
        """ 主題設置 - 新增另存色系tag 直向 狀態"""
        ID = self.getWebsiteId()
        ThemeId = self.getThemeId(ID, "false")
        data = {
            "WebsiteId": ID,
            "ColorName": "極緻黑",
            "NewColorCode": {
                "--login-bg": "#1C1717",
                "--login-color": "#ff3682",
                "--login-input-bg": "#ff8929",
                "--login-input-color": "#fff",
                "--login-btn-bg": "#ff3c6d",
                "--login-btn-color": "#fff",
                "--header-bg-top": "#fff",
                "--header-bg-bottom": "#d5d5d6",
                "--header-domain-color": "#1C1717",
                "--header-domain-color2": "#e83347",
                "--btn01-bg": "#ec692e",
                "--btn01-color": "#fff",
                "--btn02-bg": "#df3070",
                "--btn02-color": "#fff",
                "--news-bg": "#ea073f",
                "--news-color": "#fff",
                "--lobby-bg": "#fff",
                "--lobby-color": "#ea073f",
                "--lobby-color2": "#1C1717",
                "--game-bg": "#ea073f",
                "--game-color": "#fff",
                "--footer-bg-top": "#1C1717",
                "--footer-bg-bottom": "#cacacc",
                "--footer-color": "#1C1717",
                "--footer-line": "#ddd",
                "--profile-bg": "#fff",
                "--profile-color": "#ea073f",
                "--nav-bg": "#ea073f",
                "--nav-color": "#fff",
                "--nav-color2": "#f6527a",
                "--page-title-bg": "#5a158c",
                "--page-title-color": "#fff",
                "--content-bg": "#fff",
                "--content-color": "#000",
                "--content-color2": "#fe0095",
                "--promo-btn-bg": "#df3070",
                "--promo-btn-color": "#fff",
                "--promo-title-bg": "#ea073f",
                "--promo-title-color": "#fff",
                "--promo-content-bg": "#fff",
                "--promo-content-color": "#5a158c"
            },
            "ThemeId": ThemeId,
            "IsHorizontal": "false"
        }
        response_data = self.siteParameter.AddColor(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AddColor_relatedApi_status_04(self):
        """ 主題設置 - 新增另存色系tag 橫向 狀態"""
        ID = self.getWebsiteId()
        ThemeId = self.getThemeId(ID, "true")
        data = {"WebsiteId": ID,
                "ColorName": "極緻黑橫向版",
                "NewColorCode": {"--primary-bg": "#18204e",
                                 "--primary-light-bg": "#18204e",
                                 "--primary-dark-bg": "#3a4278",
                                 "--primary-border": "#8e8bdc",
                                 "--table-border": "#334192",
                                 "--table-bg": "#13193d",
                                 "--text-color": "#fff",
                                 "--light-text-color": "#ff0",
                                 "--light-color": "#afbdff",
                                 "--title-top-bg": "#5e6ebc",
                                 "--title-bottom-bg": "#212c6d",
                                 "--btn01-top-bg": "#fffdf8",
                                 "--btn01-bottom-bg": "#d57d00",
                                 "--btn01-border": "#fff100",
                                 "--btn01-text-border": "#c37700",
                                 "--btn02-top-bg": "#b9e2f4",
                                 "--btn02-bottom-bg": "#8a77d5",
                                 "--btn02-border": "#e8c8f7",
                                 "--btn02-text-border": "#7261b4"},
                "ThemeId": ThemeId,
                "IsHorizontal": "true"}
        response_data = self.siteParameter.AddColor(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateColorName_relatedApi_status_05(self):
        """ 主題設置 - 修改色系tag名稱 直向 狀態"""
        ID = self.getWebsiteId()
        nemu = self.getMobileThemeSettingId(ID, "false")
        data = {"MobileThemeSettingId": nemu["ThemeId"],
                "NewName": nemu["ThemeName"] + "1",
                "IsHorizontal": "false"
                }
        response_data = self.siteParameter.UpdateColorName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateColorName_relatedApi_status_06(self):
        """ 主題設置 - 修改色系tag名稱 橫向 狀態"""
        ID = self.getWebsiteId()
        nemu = self.getMobileThemeSettingId(ID, "true")
        nemu["ThemeName"] = "咖啡色"
        data = {"MobileThemeSettingId": nemu["ThemeId"],
                "NewName": nemu["ThemeName"],
                "IsHorizontal": "true"
                }
        response_data = self.siteParameter.UpdateColorName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_DeleteColor_relatedApi_status_07(self):
        """ 主題設置 - 刪除色系tag名稱 直向 狀態"""
        ID = self.getWebsiteId()
        ThemeId = self.getThemeId(ID, "false")
        nemu = self.getMobileThemeSettingId(ID, "false")
        data = {"WebsiteId": ID,
                "MobileThemeSettingId": nemu["ThemeId"],
                "ThemeId": ThemeId,
                "IsHorizontal": "false"}
        response_data = self.siteParameter.DeleteColor(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_DeleteColor_relatedApi_status_08(self):
        """ 主題設置 - 刪除色系tag名稱 橫向 狀態"""
        ID = self.getWebsiteId()
        ThemeId = self.getThemeId(ID, "true")
        nemu = self.getMobileThemeSettingId(ID, "true")
        data = {"WebsiteId": ID,
                "MobileThemeSettingId": nemu["ThemeId"],
                "ThemeId": ThemeId,
                "IsHorizontal": "true"}
        response_data = self.siteParameter.DeleteColor(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SaveMobileTheme_relatedApi_status_09(self):
        """ 主題設置 - 更換預設版型 - 切換D版 直向 狀態"""
        ID = self.getWebsiteId()
        ThemeId = self.getThemeId(ID, "false")
        data = {
            "WebsiteId": ID,  # 站台id
            "ThemeId": ThemeId,  # 預設版型id
            "MobileThemeSettingId": 1,  # 色系 id
            "ColorCode": "null",
            "DefaultThemeTypeId": 5,  # 1: 預設，2: A版
            "DefaultMobileThemeSettingId": 5,
            "IsHorizontal": "false"
        }
        response_data = self.siteParameter.SaveMobileTheme(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SaveMobileTheme_relatedApi_status_10(self):
        """ 主題設置 - 更換預設版型 - 切換預設版 直向 狀態"""
        ID = self.getWebsiteId()
        ThemeId = self.getThemeId(ID, "false")
        data = {
            "WebsiteId": ID,  # 站台id
            "ThemeId": ThemeId,  # 預設版型id
            "MobileThemeSettingId": 1,  # 色系 id
            "ColorCode": "null",
            "DefaultThemeTypeId": 1,  # 1: 預設，5：D版
            "DefaultMobileThemeSettingId": 1,
            "IsHorizontal": "false"
        }
        response_data = self.siteParameter.SaveMobileTheme(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SaveMobileTheme_relatedApi_status_11(self):
        """ 主題設置 - 更換版型 - 切換D版 直向 狀態"""
        ID = self.getWebsiteId()
        data = {
            "WebsiteId": ID,  # 站台id
            "ThemeId": 5,  # 預設版型id
            "MobileThemeSettingId": 2,  # 色系 id
            "ColorCode": "null",
            "DefaultThemeTypeId": 1,  # 1: 預設，5：D版
            "DefaultMobileThemeSettingId": 1,
            "IsHorizontal": "false"
        }
        response_data = self.siteParameter.SaveMobileTheme(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SaveMobileTheme_relatedApi_status_12(self):
        """ 主題設置 - 更換版型 - 切換預設 直向 狀態"""
        ID = self.getWebsiteId()
        data = {
            "WebsiteId": ID,  # 站台id
            "ThemeId": 1,  # 預設版型id
            "MobileThemeSettingId": 1,  # 色系 id
            "ColorCode": "null",
            "DefaultThemeTypeId": 1,  # 1: 預設，5：D版
            "DefaultMobileThemeSettingId": 1,
            "IsHorizontal": "false"
        }
        response_data = self.siteParameter.SaveMobileTheme(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)




if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
