'''
@Created by loka
@Date : 2020/01/03
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement
from master_api.account_login import User
from data_config.system_config import systemSetting


class AnnouncementManagementBaseTest(unittest.TestCase):
    """ 公告管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.AnnouncementManagement = PortalManagement.AnnouncementManagement(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.siteName_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def getOtherWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.other_Website_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def getId(self, mode):
        data = {"WebsiteId": self.getWebsiteId(), "Device": mode}
        response_data = self.AnnouncementManagement.getAnnouncementList(data)
        Id = response_data[1]['List'][0]['Id']
        return Id

    def updateMarqueeContent(self, mode):
        data = {"WebsiteId": self.getWebsiteId(), "Device": mode}
        response_data = self.AnnouncementManagement.getMarqueeContent(data)
        content = response_data[1]['ReturnObject']
        data = {"WebsiteId": self.getWebsiteId(), "Device": mode, 'Content': content}
        return data

    def test_AnnouncementManagement_relatedApi_status_01(self):
        """ 公告管理-取得電腦版公告列表 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1"}
        response_data = self.AnnouncementManagement.getAnnouncementList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_02(self):
        """ 公告管理-取得直向手機版公告列表 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2"}
        response_data = self.AnnouncementManagement.getAnnouncementList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_03(self):
        """ 公告管理-取得橫向手機版公告列表 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3"}
        response_data = self.AnnouncementManagement.getAnnouncementList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_04(self):
        """ 公告管理 - 檢查教程需要觀看  狀態"""
        data = {"tutorial": 1}
        response_data = self.AnnouncementManagement.checkTutorialNeedWatch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_05(self):
        """ 公告管理-取得電腦版設定 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1"}
        response_data = self.AnnouncementManagement.getAnnouncementSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_06(self):
        """ 公告管理-取得直向手機板設定 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2"}
        response_data = self.AnnouncementManagement.getAnnouncementSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_07(self):
        """ 公告管理-取得橫向手機版設定 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3"}
        response_data = self.AnnouncementManagement.getAnnouncementSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_08(self):
        """ 公告管理-更新電腦版設定 狀態"""
        data = {
            "WebsiteId": self.getWebsiteId(),
            "Device": "1",
            "PopupWhenChangedEnable": 'true',
            "PopupFrequencyEnable": 'true',
            "PopupFrequency": 1,
            "PopupHeader": "@QA_automation" + common_config.TodayDate,
            "PopupWhenRefreshPage": 'true',
            "NeedSynchronize": 'false'
        }
        response_data = self.AnnouncementManagement.updateAnnouncementSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_09(self):
        """ 公告管理-更新直向手機板設定 狀態"""
        data = {
            "WebsiteId": self.getWebsiteId(),
            "Device": "2",
            "PopupWhenChangedEnable": 'true',
            "PopupFrequencyEnable": 'true',
            "PopupFrequency": 1,
            "PopupHeader": "",
            "PopupWhenRefreshPage": 'true',
            "NeedSynchronize": 'false'
        }
        response_data = self.AnnouncementManagement.updateAnnouncementSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_10(self):
        """ 公告管理-更新橫向手機板設定 狀態"""
        data = {
            "WebsiteId": self.getWebsiteId(),
            "Device": "3",
            "PopupWhenChangedEnable": 'true',
            "PopupFrequencyEnable": 'true',
            "PopupFrequency": 1,
            "PopupHeader": "",
            "PopupWhenRefreshPage": 'true',
            "NeedSynchronize": 'false'
        }
        response_data = self.AnnouncementManagement.updateAnnouncementSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_11(self):
        """ 公告管理-新增電腦版公告 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1", "Title": "@QA_automation_Portal", "Sort": 1,
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        response_data = self.AnnouncementManagement.addAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_12(self):
        """ 公告管理-新增直向手機板公告 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2", "Title": "@QA_automation_Mobile", "Sort": 1,
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        response_data = self.AnnouncementManagement.addAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_13(self):
        """ 公告管理-新增橫向手機板公告 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3", "Title": "@QA_automation_horizontalMobile",
                "Sort": 1,
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        response_data = self.AnnouncementManagement.addAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_14(self):
        """ 公告管理-取得電腦版公告詳細資料 狀態"""
        getId = self.getId(1)
        data = {"Id": getId}
        response_data = self.AnnouncementManagement.getAnnouncementDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_15(self):
        """ 公告管理-取得直向手機板公告詳細資料 狀態"""
        getId = self.getId(2)
        data = {"Id": getId}
        response_data = self.AnnouncementManagement.getAnnouncementDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_16(self):
        """ 公告管理-取得橫向手機板公告詳細資料 狀態"""
        getId = self.getId(3)
        data = {"Id": getId}
        response_data = self.AnnouncementManagement.getAnnouncementDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_17(self):
        """ 公告管理-修改電腦版公告 狀態"""
        getId = self.getId(1)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "1",
                "Title": "@QA_automation_Portal_Modify", "Sort": 1,
                "IsEnable": 'false',
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        response_data = self.AnnouncementManagement.modifyAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_18(self):
        """ 公告管理-修改手機版公告 狀態"""
        getId = self.getId(2)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "2",
                "Title": "@QA_automation_Mobile_Modify", "Sort": 1,
                "IsEnable": 'false',
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        response_data = self.AnnouncementManagement.modifyAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_19(self):
        """ 公告管理-修改橫向手機板公告 狀態"""
        getId = self.getId(3)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "3",
                "Title": "@QA_automation_horizontalMobile_Modify",
                "Sort": 1,
                "IsEnable": 'false',
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        response_data = self.AnnouncementManagement.modifyAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_20(self):
        """ 公告管理-修改電腦版啟用開關 狀態"""
        getId = self.getId(1)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "1", "IsEnable": 'true'}
        response_data = self.AnnouncementManagement.modifyAnnouncementEnable(data)
        status_code = response_data[0]
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "1", "IsEnable": 'false'}
        self.AnnouncementManagement.modifyAnnouncementEnable(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_21(self):
        """ 公告管理-修改手機版啟用開關 狀態"""
        getId = self.getId(2)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "2", "IsEnable": 'true'}
        response_data = self.AnnouncementManagement.modifyAnnouncementEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_22(self):
        """ 公告管理-修改橫向手機版啟用開關 狀態"""
        getId = self.getId(3)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "3", "IsEnable": 'true'}
        response_data = self.AnnouncementManagement.modifyAnnouncementEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_23(self):
        """ 公告管理-移動公告一輪(Portal->Mobile->horizontal Mobile->Portal) 狀態"""
        getId = self.getId(1)
        data = {"WebsiteId": self.getWebsiteId(), "MoveIds": [getId], "FromDevice": "1", "ToDevice": 2}
        response_data = self.AnnouncementManagement.moveAnnouncementToDevice(data)
        status_code1 = response_data[0]
        data = {"WebsiteId": self.getWebsiteId(), "MoveIds": [getId], "FromDevice": "2", "ToDevice": 3}
        response_data = self.AnnouncementManagement.moveAnnouncementToDevice(data)
        status_code2 = response_data[0]
        data = {"WebsiteId": self.getWebsiteId(), "MoveIds": [getId], "FromDevice": "3", "ToDevice": 1}
        response_data = self.AnnouncementManagement.moveAnnouncementToDevice(data)
        status_code3 = response_data[0]
        self.assertEqual(bool(status_code1 == status_code2 == status_code3), True)

    def test_AnnouncementManagement_relatedApi_status_24(self):
        """ 公告管理-電腦版移動公告至其他站台 狀態"""
        getId = self.getId(1)
        data = {"FromWebsiteId": self.getWebsiteId(), "MoveIds": [getId], "Device": "1",
                "ToWebsiteId": self.getOtherWebsiteId()}
        response_data = self.AnnouncementManagement.moveAnnouncementToWebsite(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1", "Title": "@QA_automation_Portal", "Sort": 1,
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        self.AnnouncementManagement.addAnnouncement(data)

    def test_AnnouncementManagement_relatedApi_status_25(self):
        """ 公告管理-手機版移動公告至其他站台 狀態"""
        getId = self.getId(2)
        data = {"FromWebsiteId": self.getWebsiteId(), "MoveIds": [getId], "Device": "2",
                "ToWebsiteId": self.getOtherWebsiteId()}
        response_data = self.AnnouncementManagement.moveAnnouncementToWebsite(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2", "Title": "@QA_automation_Mobile", "Sort": 1,
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        self.AnnouncementManagement.addAnnouncement(data)

    def test_AnnouncementManagement_relatedApi_status_26(self):
        """ 公告管理-橫向手機版移動公告至其他站台 狀態"""
        getId = self.getId(3)
        data = {"FromWebsiteId": self.getWebsiteId(), "MoveIds": [getId], "Device": "3",
                "ToWebsiteId": self.getOtherWebsiteId()}
        response_data = self.AnnouncementManagement.moveAnnouncementToWebsite(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_27(self):
        """ 公告管理-電腦版複製公告到手機板 狀態"""
        getId = self.getId(1)
        data = {"WebsiteId": self.getWebsiteId(), "CopyIds": [getId], "FromDevice": "1", "ToDevice": 2}
        response_data = self.AnnouncementManagement.copyAnnouncementToDevice(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        getId = self.getId(2)
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2", "DeleteIds": [getId]}
        self.AnnouncementManagement.deleteAnnouncement(data)

    def test_AnnouncementManagement_relatedApi_status_28(self):
        """ 公告管理-電腦版複製公告到橫向手機板 狀態"""
        getId = self.getId(1)
        data = {"WebsiteId": self.getWebsiteId(), "CopyIds": [getId], "FromDevice": "1", "ToDevice": 3}
        response_data = self.AnnouncementManagement.copyAnnouncementToDevice(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        getId = self.getId(3)
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3", "DeleteIds": [getId]}
        self.AnnouncementManagement.deleteAnnouncement(data)

    def test_AnnouncementManagement_relatedApi_status_29(self):
        """ 公告管理-電腦版改順序 狀態"""
        getId = self.getId(1)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "1", "Sort": 2}
        response_data = self.AnnouncementManagement.modifyAnnouncementSort(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_30(self):
        """ 公告管理- 手機版改順序 狀態"""
        getId = self.getId(2)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "2", "Sort": 2}
        response_data = self.AnnouncementManagement.modifyAnnouncementSort(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_31(self):
        """ 公告管理-橫向手機版改順序 狀態"""
        getId = self.getId(3)
        data = {"Id": getId, "WebsiteId": self.getWebsiteId(), "Device": "3", "Sort": 2}
        response_data = self.AnnouncementManagement.modifyAnnouncementSort(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_32(self):
        """ 公告管理-刪除電腦版公告 狀態"""
        getId = self.getId(1)
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1", "DeleteIds": [getId]}
        response_data = self.AnnouncementManagement.deleteAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_33(self):
        """ 公告管理-刪除手機版公告 狀態"""
        getId = self.getId(2)
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2", "DeleteIds": [getId]}
        response_data = self.AnnouncementManagement.deleteAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_34(self):
        """ 公告管理-刪除橫向手機版公告 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3", "Title": "@QA_automation_horizontalMobile",
                "Sort": 1,
                "Content":
                    "<p>"
                    "<img alt=\"\" src=\"https://www.itsfun.com.tw/cacheimg/84/ce/e2cecd886623d17eae7558a688ae.jpg\" />"
                    "</p>\n",
                "ForGuest": 'true', "ForMember": 'true'}
        self.AnnouncementManagement.addAnnouncement(data)
        getId = self.getId(3)
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3", "DeleteIds": [getId]}
        response_data = self.AnnouncementManagement.deleteAnnouncement(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_35(self):
        """ 公告管理-預覽公告 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "PreviewMode": 1}
        response_data = self.AnnouncementManagement.getAnnouncementPreviewList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_36(self):
        """ 公告管理-取得電腦版跑馬燈內容 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1"}
        response_data = self.AnnouncementManagement.getMarqueeContent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_37(self):
        """ 公告管理-取得手機版跑馬燈內容 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2"}
        response_data = self.AnnouncementManagement.getMarqueeContent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_38(self):
        """ 公告管理-取得橫向手機版跑馬燈內容 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3"}
        response_data = self.AnnouncementManagement.getMarqueeContent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_39(self):
        """ 公告管理-更新電腦版跑馬燈內容 狀態"""
        data = self.updateMarqueeContent(1)
        response_data = self.AnnouncementManagement.updateMarqueeContent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_40(self):
        """ 公告管理-更新手機版跑馬燈內容 狀態"""
        data = self.updateMarqueeContent(2)
        response_data = self.AnnouncementManagement.updateMarqueeContent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_41(self):
        """ 公告管理-更新橫向手機版跑馬燈內容 狀態"""
        data = self.updateMarqueeContent(3)
        response_data = self.AnnouncementManagement.updateMarqueeContent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnnouncementManagement_relatedApi_status_42(self):
        """ 公告管理-更新公告設定 狀態"""
        WebsiteId = self.getWebsiteId()
        data = {"WebsiteId": WebsiteId, "Device": "1", "UpdateAnnouncementSettingList": [
            {"SettingType": 1, "PopupWhenChangedEnable": 'true', "PopupFrequencyEnable": 'true', "PopupHeader": "公告",
             "PopupWhenRefreshPage": 'true', "NeedSynchronize": 'true'},
            {"SettingType": 2, "PopupWhenChangedEnable": 'true', "PopupFrequencyEnable": 'true', "PopupHeader": 'null',
             "PopupWhenRefreshPage": 'true', "NeedSynchronize": 'true'}]}
        response_data = self.AnnouncementManagement.updateAnnouncementSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
