'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import unittest

from parameterized import parameterized

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User


class VerifyBetRecordHistoryData(unittest.TestCase):
    """驗證历史投注记录查询每個月都注單"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecordHistory = reports.BetRecordHistory(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @parameterized.expand([
        ("verify_bet_record_history_11_month", "hsiang", "2018/11/01 00:00:00", "2018/11/30 23:59:59"),
        ("verify_bet_record_history_12_month", "hsiang", "2018/12/01 00:00:00", "2018/12/31 23:59:59"),
        ("verify_bet_record_history_01_month", "hsiang", "2019/01/01 00:00:00", "2019/01/31 23:59:59"),
        ("verify_bet_record_history_02_month", "hsiang", "2019/02/01 00:00:00", "2019/02/28 23:59:59"),
        ("verify_bet_record_history_03_month", "hsiang", "2019/03/01 00:00:00", "2019/03/31 23:59:59"),
        ("verify_bet_record_history_04_month", "hsiang", "2019/04/01 00:00:00", "2019/04/30 23:59:59"),
        ("verify_bet_record_history_05_month", "hsiang", "2019/05/01 00:00:00", "2019/05/31 23:59:59"),
        ("verify_bet_record_history_06_month", "hsiang", "2019/06/01 00:00:00", "2019/06/30 23:59:59"),
    ])
    def testCase(self, name, account, begin_time, end_time):
        # 測試案例名稱、傳入帳號、傳入投注時間、傳入派彩時間

        # Step1 歷史投注紀錄查詢 api 呼叫
        data = {"Account": account,
                "WagersTimeBegin": begin_time,
                "WagersTimeEnd": end_time,
                "PayoffTimeBegin": begin_time,
                "PayoffTimeEnd": end_time,
                "connectionId": self.user.info()}
        self.responseData = self.betRecordHistory.search(data)

        # Step2 進行驗證判斷回傳的PageData不為空
        self.assertNotEqual([], self.responseData[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
