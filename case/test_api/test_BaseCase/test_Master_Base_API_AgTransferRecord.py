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


class AgTransferRecordBaseTest(unittest.TestCase):
    """AG 交易紀錄匯出 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.agTransferRecord = reports.AgTransferRecord(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_AgTransferRecord_baseApi_status_01(self):
        """驗證 AG交易记录汇出 - 頁面狀態"""
        response_data = self.agTransferRecord.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgTransferRecord_baseApi_status_02(self):
        """驗證 AG交易记录汇出 - 取得種類"""
        response_data = self.agTransferRecord.getAgTrTypeList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgTransferRecord_baseApi_status_03(self):
        """驗證 AG交易记录汇出 - 匯出"""
        data = {"dateBegin": common_config.BeginDate,
                "dateEnd": common_config.EndDate,
                "trtype": ["COMP_ENROLL",
                           "COMP_PRIZE",
                           "COMP_REFUND",
                           "DONATEFEE",
                           "EVENT_PRIZE",
                           "PROPFEE",
                           "RED_POCKET",
                           "SLOTEVENT"]
                }
        response_data = self.agTransferRecord.exportAgTransferRecord(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
