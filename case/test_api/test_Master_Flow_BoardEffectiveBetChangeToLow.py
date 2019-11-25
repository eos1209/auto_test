'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import unittest
from decimal import Decimal

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import reports
from master_api.account_login import User
from parameterized import parameterized


class BoardEffectiveBetChangeToLow(unittest.TestCase):
    """棋牌类游戏有效投注统一改为「取其低」"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecord = reports.BetRecords(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @parameterized.expand([
        ("verify_effective_bet_change_to_low_JdbBoard", 'JdbBoard', 6, 9),
        ("verify_effective_bet_change_to_low_Rg2Board", 'Rg2Board', 4, 5),
        ("verify_effective_bet_change_to_low_KgBoard", 'KgBoard', 9, 10),
        ("verify_effective_bet_change_to_low_City761Board", 'City761Board', 5, 6),
        ("verify_effective_bet_change_to_low_FsBoard", 'FsBoard', 6, 7),
        ("verify_effective_bet_change_to_low_NwBoard", 'NwBoard', 7, 8),
        ("verify_effective_bet_change_to_low_JsBoard", 'JsBoard', 6, 7),
        ("verify_effective_bet_change_to_low_MtBoard", 'MtBoard', 6, 9),
        ("verify_effective_bet_change_to_low_ThBoard", 'ThBoard', 7, 8),
        ("verify_effective_bet_change_to_low_DhBoard", 'DhBoard', 3, 4),
        ("verify_effective_bet_change_to_low_VgBoard", 'VgBoard', 3, 5),
        ("verify_effective_bet_change_to_low_LegBoard", 'LegBoard', 7, 8),
        # # ("Regression_SaBoard", 'SaBoard', '', 1, 6),
        # ("verify_effective_bet_change_to_low_TogBoard", 'TogBoard', 5, 6),
        # 停止合作
        # ("verify_effective_bet_change_to_low_Mw2Board", 'Mw2Board', 7, 3),
    ])
    def testCase(self, name, game_type, bet_amount_location, payoff_location):
        # 測試案例名稱、遊戲類型、抓取的數值回傳位置(下注金額，派彩)
        # Step1
        data = {"GameCategories": game_type,
                "WagersTimeBegin": common_config.WagersTimeBegin,
                "Round": " ",
                "connectionId": self.user.info()}
        response_data = self.betRecord.search(data)
        # 判斷注單是否有資料存在
        self.assertNotEqual([], response_data[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')
        self.betRecordId = response_data[1]['PageData'][0]['Id']

        # Step2
        data = {"Id": self.betRecordId}
        response_data = self.betRecord.getDetail(data)
        self.commissionable = Decimal(response_data[1]['Commissionable']).quantize(Decimal('0.00'))
        # print("有效投注:" + str(self.commissionable))

        # Step3
        data = {"Id": self.betRecordId}
        response_data = self.betRecord.getRawData(data)
        bet_amount = Decimal(response_data[1]['List'][bet_amount_location]['Value']).quantize(Decimal('0.00'))
        payoff = Decimal(response_data[1]['List'][payoff_location]['Value']).quantize(Decimal('0.00'))

        if game_type == 'FsBoard' or game_type == 'TogBoard':
            if payoff > bet_amount:
                payoff = payoff - bet_amount
            else:
                payoff = -bet_amount
        else:
            payoff = payoff

        # print("投注额:" + str(bet_amount))
        # print("派彩:" + str(payoff))

        # Step4
        if bet_amount > abs(payoff):
            check_value = abs(payoff)
        else:
            check_value = bet_amount
        self.assertEqual(str(self.commissionable), str(check_value))


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
