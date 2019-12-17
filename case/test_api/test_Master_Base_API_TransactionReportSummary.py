'''
@Created by loka
@Date : 2019/12/10
'''

import unittest
from data_config import common_config
from data_config import master_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import account_management
from master_api.account_login import User


class TransactionReportSummaryBaseTest(unittest.TestCase):
    """總存取款匯出 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.TransactionReportSummary = account_management.TransactionReportSummary(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def switchMonthDay(self, mode):
        if mode == 1:  # 月
            data = {'beginDate': common_config.FirstDay, 'endDate': common_config.EndDay, 'isByMonth': 1}
            return self.TransactionReportSummary.reportExport(data)
        elif mode == 0:  # 日
            data = {'beginDate': common_config.BeginDate, 'endDate': common_config.EndDate, 'isByMonth': 0}
            return self.TransactionReportSummary.reportExport(data)

    def test_TransactionReportSummary_baseApi_status_01(self):
        """驗證 總存取款匯出-總存取款匯出頁面 狀態"""
        response_data = self.TransactionReportSummary.summary({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TransactionReportSummary_baseApi_status_02(self):
        """驗證 總存取款匯出-總存取款匯出 -日 狀態"""
        response_data = self.switchMonthDay(0)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TransactionReportSummary_baseApi_status_03(self):
        """驗證 總存取款匯出-總存取款匯出 -月 狀態"""
        response_data = self.switchMonthDay(1)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_TransactionReportSummary_baseApi_status_04(self):
        """驗證 總存取款匯出-大量匯出時更新狀態 狀態"""
        response_data = self.TransactionReportSummary.updateStatus({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
