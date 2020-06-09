'''
@Created by Jo
@Date : 2020/06/09
'''

import unittest
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.account_management import Master
from master_api.account_login import User

from data_config.system_config import systemSetting


class MemberBatchBaseTest(unittest.TestCase):
    """子帳號管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = Master(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def Get_All_Account(self):
        response_data = self.siteParameter.GetAll({})
        for i in range(len(response_data[1])):
            Account = response_data[1][i]['Account']
            ID = response_data[1][i]['Id']
            return Account, ID

    def test_Master_relatedApi_status_01(self):
        """驗證 子帳號管理 - 取得頁面 狀態"""
        response_data = self.siteParameter.List({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Master_relatedApi_status_02(self):
        """驗證 子帳號管理 - 取得列表 狀態"""
        response_data = self.siteParameter.GetAll({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Master_relatedApi_status_03(self):
        """驗證 子帳號管理 - 取得角色列表 狀態"""
        response_data = self.siteParameter.GetRoleList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Master_relatedApi_status_04(self):
        """驗證 子帳號管理 - 取得詳細資料 狀態"""
        data = {
            "account": self.Get_All_Account()[0]
        }
        response_data = self.siteParameter.GetDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Master_relatedApi_status_05(self):
        """驗證 子帳號管理-獲取角色授權已獲取詳細信息 狀態"""
        data = {"roleId": [self.Get_All_Account()[1]]}
        response_data = self.siteParameter.GetRoleAuthorityForDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Master_relatedApi_status_06(self):
        """驗證 子帳號管理-獲取歷史訊息 狀態"""
        response_data = self.siteParameter.History({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Master_relatedApi_status_07(self):
        """驗證 子帳號管理-獲取帳號歷史訊息 狀態"""
        data = {
            "account": self.Get_All_Account()[0],
            "take": 100,
            "skip": 0,
            "query": {
            }
        }
        response_data = self.siteParameter.LoadHistory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
