'''
@Created by loka
@Date : 2020/01/20
'''

import unittest

from base.CommonMethod import UploadFile
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.account_login import User
from master_api.system_management import PortalManagement
from data_config.system_config import systemSetting
from time import sleep


class SlideShowBaseTest(unittest.TestCase):
    """ 大圖輪播 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.slideShow = PortalManagement.SlideShow(self.__http)
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

    def test_SlideShow_relatedApi_status_01(self):
        """ 大圖輪播 - 取得電腦版資訊 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "1"}
        response_data = self.slideShow.GetSlideShowInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SlideShow_relatedApi_status_02(self):
        """ 大圖輪播 - 取得手機版資訊 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "2"}
        response_data = self.slideShow.GetSlideShowInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SlideShow_relatedApi_status_03(self):
        """ 大圖輪播 - 取得橫向手機版資訊 狀態"""
        data = {"WebsiteId": self.getWebsiteId(), "Device": "3"}
        response_data = self.slideShow.GetSlideShowInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SlideShow_relatedApi_status_04(self):
        """ 大圖輪播 - 上傳jpg圖檔 狀態"""
        self.upload = UploadFile('image/jpg/test_jpg.jpg',  # 檔案路徑
                                 'ImageFile',  # 上傳欄位
                                 'test_jpg.jpg'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()
        response_data = self.slideShow.UploadSlideShowImageV2(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()

    def test_SlideShow_relatedApi_status_05(self):
        """ 大圖輪播 - 上傳png圖檔 狀態"""
        self.upload = UploadFile('image/png/test_png.png',  # 檔案路徑
                                 'ImageFile',  # 上傳欄位
                                 'test_png.png'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()
        response_data = self.slideShow.UploadSlideShowImageV2(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()

    def test_SlideShow_relatedApi_status_06(self):
        """ 大圖輪播 - 上傳gif圖檔 狀態"""
        sleep(5)
        self.upload = UploadFile('image/gif/test_gif.gif',  # 檔案路徑
                                 'ImageFile',  # 上傳欄位
                                 'test_gif.gif'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()
        response_data = self.slideShow.UploadSlideShowImageV2(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()

    def test_SlideShow_relatedApi_status_07(self):
        """ 大圖輪播 - 電腦版更新大圖輪播 狀態"""
        data = {"currentWebsiteId": self.getWebsiteId(), "currentDevice": "1", "currentSlideShowItems": [
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/88b73347665e41048daa90f5d8fa8140.jpg", "link": "",
             "sort": 0},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/1848916a567847a88b3ed5d763acb701.jpg", "link": "",
             "sort": 1},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/63e11f4c2a5d4f03a6e85eca762e73eb.jpg", "link": "",
             "sort": 2},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/1cc66874bf72401b9e6960f52eba55d2.jpg", "link": "",
             "sort": 3},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/50ccb91baa274a20845043cf34adb33e.jpg", "link": "",
             "sort": 4}], "copyToSlideShowItems": []}
        response_data = self.slideShow.SaveSlideShowChangesV2(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SlideShow_relatedApi_status_08(self):
        """ 大圖輪播 - 手機版更新大圖輪播 狀態"""
        data = {"currentWebsiteId": self.getWebsiteId(), "currentDevice": 2, "currentSlideShowItems": [
            {"url": "/Cdn2Redirect/PortalManagement/Image/SlideShow/de0d274c32a44975b0cc60c1104513d2.png", "link": "",
             "sort": 0}], "copyToSlideShowItems": []}
        response_data = self.slideShow.SaveSlideShowChangesV2(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SlideShow_relatedApi_status_09(self):
        """ 大圖輪播 - 橫向手機版更新大圖輪播 狀態"""
        data = {"currentWebsiteId": self.getWebsiteId(), "currentDevice": 3, "currentSlideShowItems": [
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/c3e3294d56fb4bc3bdce68db3fb9f145.gif", "link": "",
             "sort": 0},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/69d4ed6d057e40eda901a43451087541.jpg", "link": "",
             "sort": 1},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/394da2470f244c8d8cea390826646c26.png", "link": "",
             "sort": 2},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/017cf1efd91e4379a3a0a6667406b1ff.png", "link": "",
             "sort": 3},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/8bb52541b5c94ca38b75640baf720042.jpg", "link": "",
             "sort": 4},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/fb3ed80d1f164a4a8f58e965855365f4.jpg", "link": "",
             "sort": 5},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/a18a7b57bc5b487b8228a4a5f97990b8.jpg", "link": "",
             "sort": 6},
            {"url": "/Cdn2Redirect/PortalManagement/AB005/SlideShow/b67e897370cb492a8e8dd528a8444c01.jpg", "link": "",
             "sort": 7}], "copyToSlideShowItems": []}
        response_data = self.slideShow.SaveSlideShowChangesV2(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
