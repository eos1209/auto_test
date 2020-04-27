# '''
# @Created by loka
# @Date : 2020/01/02
# '''
# import time
# import unittest
#
# from data_config import common_config
# from base.HTMLTestReportCN import HTMLTestRunner
# from base.httpRequest import HttpRequest
# from master_api import system_management
# from master_api.account_login import User
#
#
# class SystemInfoBaseTest(unittest.TestCase):
#     """ 站台系統值設置一開始先更改為文字驗並等待五分十秒 - 相關 API 調用狀態"""
#
#     def setUp(self):
#         self.__http = HttpRequest()
#         self.user = User(self.__http)
#         self.SystemInfo = system_management.SystemInfo(self.__http)
#         self.user.login()
#
#     def tearDown(self):
#         self.user.logout()
#
#     def test_SystemInfo_relatedApi_status_01(self):
#         """驗證 站台系統值設置 - 更新會員登入驗證碼類型"""
#         data = {"NewValue": "1"}
#         response_data = self.SystemInfo.updateCaptchaTypeLogin(data)
#         status_code = response_data[0]
#         time.sleep(310)
#         self.assertEqual(status_code, common_config.Status_Code)
#
#     def test_SystemInfo_relatedApi_status_02(self):
#         """驗證 站台系統值設置 - 取得列表頁面"""
#         response_data = self.SystemInfo.index({})
#         status_code = response_data[0]
#         self.assertEqual(status_code, common_config.Status_Code)
#
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HTMLTestRunner())
