'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import unittest
import re
import datetime
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User
from data_config.system_config import systemSetting


class VerifyBetRecordHistoryData(unittest.TestCase):
    """驗證历史投注记录查询每個月都注單"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecordHistory = reports.BetRecordHistory(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def testCase(self):
        """驗證历史投注记录查询注單"""
        # 測試案例名稱、傳入帳號、傳入投注時間、傳入派彩時間
        # step1
        response_data = self.betRecordHistory.getHistoryDateRange({})
        timeBegin = re.split('[()]', response_data[1][0])[1][:10]
        timeEnd = re.split('[()]', response_data[1][1])[1][:10]
        timeBegin = datetime.datetime.utcfromtimestamp(int(timeBegin)).strftime("%Y-%m-%d %H:%M:%S")
        timeEnd = datetime.datetime.utcfromtimestamp(int(timeEnd)).strftime("%Y-%m-%d %H:%M:%S")
        # Step2 歷史投注紀錄查詢 api 呼叫
        data = {"Account": self.config.test_Member_config(),
                "WagersTimeBegin": timeBegin,
                "WagersTimeEnd": timeEnd,
                "PayoffTimeBegin": timeBegin,
                "PayoffTimeEnd": timeEnd,
                "connectionId": self.user.info()}
        self.responseData = self.betRecordHistory.search(data)

        # Step3 進行驗證判斷回傳的PageData不為空
        self.assertNotEqual([], self.responseData[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
