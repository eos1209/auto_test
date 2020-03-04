'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User
from data_config.system_config import systemSetting


class ContributionBaseTest(unittest.TestCase):
    """貢獻金查詢 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.contribution = reports.Contribution(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_Contribution_relatedApi_status_01(self):
        """驗證 取得頁面 狀態"""
        response_data = self.contribution.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Contribution_relatedApi_status_02(self):
        """驗證 取得有貢獻金的娛樂城清單 狀態"""
        response_data = self.contribution.getContributionGameSuppliers({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Contribution_relatedApi_status_03(self):
        """驗證 取得當期累計貢獻金 狀態"""
        data = {"date": common_config.TodayDate,
                "halfYear": "false"}
        response_data = self.contribution.getSummary(data)
        status_code = response_data[0]
        # self.gameSupplierId = response_data[1]['ContributionSummary']['Details'][0]['GameSupplier']
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Contribution_relatedApi_status_04(self):
        """驗證 取得詳情 狀態"""
        data = {"date": common_config.TodayDate,
                "halfYear": "false",
                "gameSupplier": self.config.Contribution_gameSupplier()}
        response_data = self.contribution.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Contribution_relatedApi_status_05(self):
        """驗證 取得娛樂城詳情 狀態"""
        data = {
            "date": common_config.TodayDate,
            "halfYear": 'false',
            "gameSupplier": self.config.Contribution_gameSupplier()
        }
        response_data = self.contribution.getGameSupplierDetail(data)
        status_code = response_data[0]
        # self.gameTypeId = response_data[1]['ContributionGameSupplierDetail']['GameContributions'][0]['GameTypeId']
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Contribution_relatedApi_status_06(self):
        """驗證 取得全部 狀態"""
        data = {
            "date": common_config.TodayDate,
            "halfYear": 'false'
        }
        response_data = self.contribution.getAllGameSupplierSummary(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Contribution_relatedApi_status_07(self):
        """驗證 取得娛樂城獎池彩金清單 狀態"""
        data = {
            "gameSupplier": self.config.Contribution_gameSupplier(),
            "pageSize": 20,
            "pageIndex": 0,
            "halfYear": 'true',
            "date": common_config.TodayDate
        }
        response_data = self.contribution.getSupplierJackPotMemberList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Contribution_relatedApi_status_08(self):
        """驗證 取得遊戲獎池彩金清單 狀態"""
        data = {
            "gameSupplier": self.config.Contribution_gameSupplier(),
            "gameTypeId": 8280,
            "pageSize": 20,
            "pageIndex": 0,
            "halfYear": 'true',
            "date": common_config.TodayDate
        }
        response_data = self.contribution.getGameJackPotMemberList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
