# '''
# @Created by loka
# @Date : 2020/02/15
# '''
#
# import unittest
#
# from base.HTMLTestReportCN import HTMLTestRunner
# from base.httpRequest import HttpRequest
# from data_config import common_config
# from data_config import master_config
# from master_api import system_management
# from master_api import reports
# from master_api.account_login import User
#
#
# class AnyTimeDiscountBaseTest(unittest.TestCase):
#     """ 返水設定 - 相關 API 調用狀態"""
#
#     def setUp(self):
#         self.__http = HttpRequest()
#         self.user = User(self.__http)
#         self.AnyTimeDiscount = system_management.AnyTimeDiscountSetting(self.__http)
#         self.BetRecord = reports.BetRecords(self.__http)
#         self.user.login()
#
#     def test_create_ATDsetting(self):
#         """建立返水設定"""
#         # step1:
#
#
#
#     def tearDown(self):
#         self.user.logout()
#
# if __name__ == '__main__':
#     unittest.main(testRunner = HTMLTestRunner())
