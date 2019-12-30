'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import random
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User


class MemberLoginBaseTest(unittest.TestCase):
    """登入记录查询- 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberLogin = reports.MemberLogin(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberLoginRecords_relatedApi_status_01(self):
        """驗證 登入记录查询 - 查詢頁面 狀態"""
        response_data = self.memberLogin.query({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberLoginRecords_relatedApi_status_02(self):
        """驗證 查詢v2 狀態"""
        response_data = self.memberLogin.searchV2({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberLoginRecords_relatedApi_status_03(self):
        """驗證 登入记录查询 - 取得詳細頁面 狀態"""
        response_data = self.memberLogin.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberLoginRecords_relatedApi_status_04(self):
        """驗證 登入记录查询 - 取得詳細資料 狀態"""
        # STEP1
        response_data = self.memberLogin.searchV2({})
        ff = len(response_data[1]['PageData'])
        flag = random.randint(0, ff - 1)
        loginId = response_data[1]['PageData'][flag]['Id']

        # STEP2
        data = {"id": loginId}
        response_data = self.memberLogin.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberLoginRecords_relatedApi_status_05(self):
        """驗證 登入记录查询 - 匯出 狀態"""
        response_data = self.memberLogin.export({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_MemberLoginRecords_relatedApi_status_05(self):
    #     """驗證 查詢 狀態"""
    #     # 查詢
    #     response_data = self.memberLogin.search()
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
