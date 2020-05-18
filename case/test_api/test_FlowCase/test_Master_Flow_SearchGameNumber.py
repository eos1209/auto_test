'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User
from data_config import common_config
from parameterized import parameterized


class SearchGameNumber(unittest.TestCase):
    """驗證局號查詢功能正常"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betting = reports.BetRecords(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @parameterized.expand([
        # ("verify_bureau_number_query_AG", 'AgBr', 2), # AG 暫時注解！
        ("verify_bureau_number_query_CQ9", 'Cq9Slot', 1),
        ("verify_bureau_number_query_PNG", 'PngSlot', 4),
        ("verify_bureau_number_query_GPK", 'Rg2Slot', 2),
    ])
    def testCase(self, name, game_type, data_location):
        self.verifyGameNumberFunctionIsNormally(game_type, data_location)

    def verifyGameNumberFunctionIsNormally(self, game_type, data_location):
        # step1 search betRecordId
        data = {"WagersTimeBegin": common_config.WagersTimeBegin,
                "GameCategories": game_type,
                "connectionId": self.user.info()}
        response_data = self.betting.search(data)
        # 判斷是否有注單存在
        self.assertNotEqual([], response_data[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')
        self.betRecordId = response_data[1]['PageData'][0]['Id']

        # step2 get GameNumber1
        data = {"id": self.betRecordId}
        response_data = self.betting.getRawData(data)
        self.gameNumber1 = response_data[1]['List'][data_location]['Value']

        # step3 search GameNumber
        data = {"WagersTimeBegin": common_config.WagersTimeBegin,
                "GameCategories": game_type,
                "Round": self.gameNumber1,
                "connectionId": self.user.info()}
        response_data = self.betting.search(data)
        self.betRecordId = response_data[1]['PageData'][0]['Id']

        # step4 get GameNumber2
        data = {"id": self.betRecordId}
        response_data = self.betting.getRawData(data)
        self.gameNumber2 = response_data[1]['List'][data_location]['Value']

        # step5 assert equal GameNumber1, GameNumber2
        self.assertEqual(str(self.gameNumber1), str(self.gameNumber2))


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
