'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import reports
from master_api.account_login import User


class StatisticsBaseTest(unittest.TestCase):
    """ 統計報表 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.statistics = reports.Statistics(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_Statistics_relatedApi_status_01(self):
        """驗證 統計報表 - 取得頁面狀態"""
        response_data = self.statistics.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_02(self):
        """驗證 統計報表 - 取得代理商或會員資訊"""
        data = {"account": "GPK_A",
                "isMember": "false"}
        response_data = self.statistics.getAgentInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_03(self):
        """驗證 統計報表 - 取得統計資訊(起始日期、結束日期、代理商帳號)"""
        data = {"begin": common_config.BeginDate,
                "end": common_config.EndDate,
                "agent": "GPK_A"}
        response_data = self.statistics.getCategoryInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_04(self):
        """驗證 統計報表 - 取得統計資料會員數"""
        data = {"begin": common_config.BeginDate,
                "end": common_config.EndDate,
                "agent": "GPK_A"}
        response_data = self.statistics.getMemberCount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_05(self):
        """驗證 統計報表 - 取得統計報表詳細資料"""
        data = {"begin": common_config.BeginDate,
                "end": common_config.EndDate,
                "agent": "GPK_A",
                "types": " ",
                "orderBy": "Commissionable",
                "reverse": "true",
                "take": "100",
                "skip": "0"}
        response_data = self.statistics.getDetailInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_06(self):
        """驗證 統計報表 - 匯出"""
        data = {"begin": common_config.WagersTimeBegin,
                "end": common_config.FirstDay,
                "agent": "",
                "types": "",
                'isExportGameName': 'true'}
        response_data = self.statistics.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_07(self):
        """驗證 統計報表 - 更新狀態"""
        response_data = self.statistics.UpdateStatus({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_Statistics_relatedApi_status_07(self):
    #     """驗證 統計報表 - 重新導向 FTP Site"""
    #     response_data = self.statistics.getToManualExportFileFTP()
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
