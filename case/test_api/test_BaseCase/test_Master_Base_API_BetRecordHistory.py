'''
@Created by loka
@Date : 2020/01/06
'''
import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User
import datetime
import re
from data_config.system_config import systemSetting


class BetRecordHistoryBaseTest(unittest.TestCase):
    """ 歷史投注紀錄查詢 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecordHistory = reports.BetRecordHistory(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_BetRecordHistory_relatedApi_status_01(self):
        """驗證 歷史投注紀錄查詢 - 取得頁面狀態"""
        response_data = self.betRecordHistory.query({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecordHistory_relatedApi_status_02(self):
        """驗證 歷史投注紀錄查詢 - 取得時間區間"""
        response_data = self.betRecordHistory.getHistoryDateRange({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecordHistory_relatedApi_status_03(self):
        """驗證 歷史投注紀錄查詢 - 取得娛樂城詳細資料"""
        response_data = self.betRecordHistory.getSupplierCategories({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecordHistory_relatedApi_status_04(self):
        """驗證 歷史投注紀錄查詢 - 搜尋"""
        # step 1: 取得DateRange限制的時間查詢區間
        response_data = self.betRecordHistory.getHistoryDateRange({})
        timeBegin = re.split('[()]', response_data[1][0])[1][:10]
        timeEnd = re.split('[()]', response_data[1][1])[1][:10]
        timeBegin = datetime.datetime.utcfromtimestamp(int(timeBegin)).strftime("%Y-%m-%d %H:%M:%S")
        timeEnd = datetime.datetime.utcfromtimestamp(int(timeEnd)).strftime("%Y-%m-%d %H:%M:%S")
        data = {"Account": "abby", "WagersTimeBegin": timeBegin, "WagersTimeEnd": timeEnd,
                "PayoffTimeBegin": timeBegin, "PayoffTimeEnd": timeEnd,
                "connectionId": self.user.info()}
        response_data = self.betRecordHistory.search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecordHistory_relatedApi_status_05(self):
        """驗證 歷史投注紀錄查詢 - 匯出Excel"""
        # step 1: 取得DateRange限制的時間查詢區間
        response_data = self.betRecordHistory.getHistoryDateRange({})
        timeBegin = re.split('[()]', response_data[1][0])[1][:10]
        timeEnd = re.split('[()]', response_data[1][1])[1][:10]
        timeBegin = datetime.datetime.utcfromtimestamp(int(timeBegin)).strftime("%Y-%m-%d %H:%M:%S")
        timeEnd = datetime.datetime.utcfromtimestamp(int(timeEnd)).strftime("%Y-%m-%d %H:%M:%S")
        data = {"Account": "abby", "WagersTimeBegin": timeBegin, "WagersTimeEnd": timeEnd,
                "PayoffTimeBegin": timeBegin, "PayoffTimeEnd": timeEnd}
        response_data = self.betRecordHistory.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecordHistory_relatedApi_status_06(self):
        """驗證 歷史投注紀錄查詢 - 歷史投注紀錄詳細頁面"""
        response_data = self.betRecordHistory.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecordHistory_relatedApi_status_07(self):
        """驗證 歷史投注紀錄查詢 - 歷史投注紀錄詳細資料"""
        data = {"id": self.config.BetRecordHistory()}
        response_data = self.betRecordHistory.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
