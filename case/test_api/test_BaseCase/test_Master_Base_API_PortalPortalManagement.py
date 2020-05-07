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


class PortalManagementBaseTest(unittest.TestCase):
    """ 網站版面 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = PortalManagement.PortalManagement(self.__http)
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

    def test_GetProductSetting_relatedApi_status_01(self):
        """ 網站版面 - 取得網站版面獲取產品設置 電腦&直向&橫向 狀態"""
        ID = self.getWebsiteId()
        deviceType = [1, 2, 3]
        for x in deviceType:
            data = {"device": x, "websiteId": ID}
            response_data = self.siteParameter.GetProductSetting(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_SaveProductSetting_relatedApi_status_02(self):
        """ 網站版面 - 修改標題名稱&前台顯示站名 電腦&直向&橫向 狀態"""
        ID = self.getWebsiteId()
        menu = random.randint(1, 50)
        deviceType = [1, 2, 3]
        for i in deviceType:
            data = {
                "websiteId": ID,
                "device": i,
                "titleName": "Stage 测试站" + str(menu),
                "portalSiteName": "Stage 测试站" + str(menu)
            }
            response_data = self.siteParameter.SaveProductSetting(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    # def test_SaveProductSetting_relatedApi_status_03(self):
    #     """ 網站版面 - 修改標題ico 電腦&直向&橫向 狀態"""
    #     # 我卡點在處...
    #     ID = self.getWebsiteId()
    #     menu = random.randint(1, 50)
    #     deviceType = [1, 2, 3]
    #     for i in deviceType:
    #         data = {
    #             "websiteId": ID,
    #             "device": i,
    #             "titleName": "Stage 测试站" + str(menu),
    #             "portalSiteName": "Stage 测试站" + str(menu)
    #         }
    #         response_data = self.siteParameter.SaveProductSetting(data)
    #         status_code = response_data[0]
    #         self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
