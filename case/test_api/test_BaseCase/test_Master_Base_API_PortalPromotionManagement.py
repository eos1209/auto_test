'''
@Created by loka
@Date : 2020/01/20
'''

import unittest
from time import sleep

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement
from master_api.account_login import User
from data_config.system_config import systemSetting


class PromotionManagementBaseTest(unittest.TestCase):
    """ 優惠管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = PortalManagement.PromotionManage(self.__http)
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

    # 取大分類sort + 1
    def getSort(self, data):
        response_data = self.siteParameter.GetPromotions(data)
        item = len(response_data[1]['Categories']) + 1
        return item

    # 取大分類id
    def getSortId(self, data):
        PromotionsID = []
        response_data = self.siteParameter.GetPromotions(data)
        for i in range(len(response_data[1]['Categories'])):
            PromotionsID = response_data[1]['Categories'][i]['Id']
        return PromotionsID

    # 取子分類ID
    def getSubcategoriesID(self, data):
        PromotionsID = []
        response_data = self.siteParameter.GetPromotions(data)
        for i in range(len(response_data[1]['Categories'])):
            PromotionsID = response_data[1]['Categories'][i]['Id']
        return PromotionsID

    # 取子子分類ID
    def getPromotionsID(self, data):
        PromotionsID = []
        PID = []
        response_data = self.siteParameter.GetPromotions(data)
        for i in range(len(response_data[1]['Categories'])):
            PromotionsID = response_data[1]['Categories'][i]['Promotions']
        for x in PromotionsID:
            PID = PromotionsID[0]['Id']
        return PID

    def test_PromotionManagement_relatedApi_status_01(self):
        """ 優惠管理 - 取得優惠管理目前列表 狀態"""
        data = {"id": self.getWebsiteId()}
        response_data = self.siteParameter.GetPromotions(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Promotion_Add_Category_relatedApi_status_02(self):
        """ 優惠管理 - 新增大分類功能"""
        ID = self.getWebsiteId()
        sort_item = self.getSort(ID)
        data = {"Id": ID,
                "Categories":
                    [
                        {
                            "Name": "QA大分類之一",
                            "Sort": sort_item,
                            "Promotions": []
                        }
                    ]
                }
        response_data = self.siteParameter.Submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Promotion_Add_Subcategories_relatedApi_status_03(self):
        """ 優惠管理 - 新增大分類中的子分類功能"""
        ID = self.getWebsiteId()
        SortId = self.getSortId(ID)
        data = {
            "Id": ID,
            "Categories": [
                {
                    "Id": SortId,
                    "Promotions": [
                        {
                            "Name": "測試子分類一",
                            "Sort": 1,
                            "IsEnabled": "true",
                            "IsWeb": "true",
                            "IsMobile": "true",
                            "IsHorizontal": "true",
                            "DetailType": 1,
                            "Detail": "<p>測試一號</p>\n"
                        }
                    ]
                }
            ]
        }
        response_data = self.siteParameter.Submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Promotion_Edit_Subcategories_relatedApi_status_04(self):
        """ 優惠管理 - 修改大分類中的子子分類功能 - 不啟用"""
        ID = self.getWebsiteId()
        SortId = self.getSortId(ID)
        PId = self.getPromotionsID(ID)
        data = {
            "Id": ID,
            "Categories": [
                {
                    "Id": SortId,
                    "Promotions": [
                        {
                            "Id": PId,
                            "IsEnabled": "false"
                        }]
                }]
        }
        response_data = self.siteParameter.Submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Promotion_Del_Subcategories_relatedApi_status_05(self):
        """ 優惠管理 - 移除大分類中的子子分類功能"""
        ID = self.getWebsiteId()
        PId = self.getPromotionsID(ID)
        data = {
            "Id": ID,
            "Categories": [],
            "RemovePromotions": [PId]
        }
        response_data = self.siteParameter.Submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Promotions_Del_relatedApi_status_06(self):
        """ 優惠管理 - 移除大分類功能"""
        ID = self.getWebsiteId()
        SortId = self.getSortId(ID)
        data = {
            "Id": ID,
            "Categories": [],
            "RemoveCategories": [SortId]
        }
        response_data = self.siteParameter.Submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
