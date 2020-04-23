'''
@Created by loka
@Date : 2020/01/20
'''

import unittest
import random
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement
from master_api.account_login import User
from data_config.system_config import systemSetting


class SiteParameterBaseTest(unittest.TestCase):
    """ 財務中心 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = PortalManagement.FinanceCenter(self.__http)
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

    # 取種類列表
    def getType(self, Hdata):
        response_data = self.siteParameter.GetFinanceCenterSubCategory(Hdata)
        return response_data

    def test_GetFinanceCenterSubCategory_relatedApi_status_01(self):
        """ 財務中心 - 取得財務中心目前列表 直向&橫向 狀態"""
        ID = self.getWebsiteId()
        deviceType = [2, 3]
        for x in deviceType:
            data = {"websiteId": ID,
                    "device": x}
            response_data = self.siteParameter.GetFinanceCenterSubCategory(data)
            status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GetOnlinePaymentDirectSetting_relatedApi_status_02(self):
        """ 財務中心 - 取得財務中心取得裝置種類狀態 直向&橫向 狀態"""
        ID = self.getWebsiteId()
        deviceType = [2, 3]
        for x in deviceType:
            data = {"websiteId": ID,
                    "deviceType": x}
            response_data = self.siteParameter.GetOnlinePaymentDirectSetting(data)
            status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GetFinanceCenterDetailSetting_relatedApi_status_03(self):
        """ 財務中心 - 取得財務中心詳細資料列表狀態 直向&橫向 狀態"""
        ID = self.getWebsiteId()
        deviceType = [2, 3]
        for x in deviceType:
            data = {"websiteId": ID,
                    "device": x}
            response_data = self.siteParameter.GetFinanceCenterDetailSetting(data)
            status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateFinanceCenterSubCategory_relatedApi_status_04(self):
        """ 財務中心 - 修改推廣圖標文字狀態 直向 狀態"""
        menu = random.randint(1, 50)
        Type_data = []
        ID = self.getWebsiteId()
        Hdata = {"websiteId": ID,
                 "device": "2"}

        TData = self.getType(Hdata)
        for i in range(len(TData[1]['ReturnObject'])):
            x = TData[1]['ReturnObject'][i]
            del x['WebSiteId']
            del x['Device']
            Type_data.append(x)

        Type_data[0]['RecommendTitle'] = '自動化' + str(menu)
        data = {
            "websiteId": ID,
            "device": "2",
            "financeCenterTypeList": Type_data
        }
        response_data = self.siteParameter.UpdateFinanceCenterSubCategory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateFinanceCenterSubCategory_relatedApi_status_05(self):
        """ 財務中心 - 修改推廣內容狀態 直向 狀態"""
        menu = random.randint(1, 50)
        Type_data = []
        ID = self.getWebsiteId()
        Hdata = {"websiteId": ID,
                 "device": "2"}
        TData = self.getType(Hdata)

        for i in range(len(TData[1]['ReturnObject'])):
            x = TData[1]['ReturnObject'][i]
            del x['WebSiteId']
            del x['Device']
            Type_data.append(x)

        Type_data[0]['RecommendContent'] = '這是個測試推廣內容的文字數：' + str(menu)
        data = {
            "websiteId": ID,
            "device": "2",
            "financeCenterTypeList": Type_data
        }
        response_data = self.siteParameter.UpdateFinanceCenterSubCategory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateFinanceCenterSubCategory_relatedApi_status_06(self):
        """ 財務中心 - 修改推廣圖標文字狀態 橫向 狀態"""
        menu = random.randint(1, 50)
        Type_data = []
        ID = self.getWebsiteId()
        Hdata = {"websiteId": ID,
                 "device": "3"}

        TData = self.getType(Hdata)
        for i in range(len(TData[1]['ReturnObject'])):
            x = TData[1]['ReturnObject'][i]
            del x['WebSiteId']
            del x['Device']
            Type_data.append(x)

        Type_data[0]['RecommendTitle'] = '自動化' + str(menu)
        data = {
            "websiteId": ID,
            "device": "3",
            "financeCenterTypeList": Type_data
        }
        response_data = self.siteParameter.UpdateFinanceCenterSubCategory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateFinanceCenterSubCategory_relatedApi_status_07(self):
        """ 財務中心 - 修改推廣內容狀態 橫向 狀態"""
        menu = random.randint(1, 50)
        Type_data = []
        ID = self.getWebsiteId()
        Hdata = {"websiteId": ID,
                 "device": "3"}
        TData = self.getType(Hdata)

        for i in range(len(TData[1]['ReturnObject'])):
            x = TData[1]['ReturnObject'][i]
            del x['WebSiteId']
            del x['Device']
            Type_data.append(x)

        Type_data[0]['RecommendContent'] = '這是個測試推廣內容的文字數：' + str(menu)
        data = {
            "websiteId": ID,
            "device": "3",
            "financeCenterTypeList": Type_data
        }
        response_data = self.siteParameter.UpdateFinanceCenterSubCategory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateFinanceCenterSubCategory_relatedApi_status_08(self):
        """ 財務中心 - 公司入款顯示關閉 狀態"""
        Type_data = []
        ID = self.getWebsiteId()
        Hdata = {"websiteId": ID,
                 "device": "2"}
        TData = self.getType(Hdata)
        for i in range(len(TData[1]['ReturnObject'])):
            x = TData[1]['ReturnObject'][i]
            del x['WebSiteId']
            del x['Device']
            Type_data.append(x)
        Type_data[0]['IsOpen'] = 'false'
        data = {
            "websiteId": ID,
            "device": "2",
            "financeCenterTypeList": Type_data
        }
        response_data = self.siteParameter.UpdateFinanceCenterSubCategory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_UpdateFinanceCenterSubCategory_relatedApi_status_09(self):
        """ 財務中心 - 公司入款顯示開啟 狀態"""
        Type_data = []
        ID = self.getWebsiteId()
        Hdata = {"websiteId": ID,
                 "device": "2"}
        TData = self.getType(Hdata)
        for i in range(len(TData[1]['ReturnObject'])):
            x = TData[1]['ReturnObject'][i]
            del x['WebSiteId']
            del x['Device']
            Type_data.append(x)
        Type_data[0]['IsOpen'] = 'True'
        data = {
            "websiteId": ID,
            "device": "2",
            "financeCenterTypeList": Type_data
        }
        response_data = self.siteParameter.UpdateFinanceCenterSubCategory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
