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
        ("Verify_EffectiveBetChangeToLow_Rg2Board", 'Rg2Board', 4, 5),  # GPK 棋牌
        ("Verify_EffectiveBetChangeToLow_JdbBoard", 'JdbBoard', 6, 9),  # JDB 奪寶棋牌
        ("Verify_EffectiveBetChangeToLow_KgBoard", 'KgBoard', 9, 10),  # KG 開元棋牌
        ("Verify_EffectiveBetChangeToLow_City761Board", 'City761Board', 5, 6),  # AP 愛棋牌
        ("Verify_EffectiveBetChangeToLow_FsBoard", 'FsBoard', 6, 7),  # 樂遊棋牌
        ("Verify_EffectiveBetChangeToLow_NwBoard", 'NwBoard', 7, 8),  # 新世界棋牌
        ("Verify_EffectiveBetChangeToLow_JsBoard", 'JsBoard', 6, 7),  # JS 金龍棋牌
        ("Verify_EffectiveBetChangeToLow_MtBoard", 'MtBoard', 6, 9),  # MT 美天棋牌
        ("Verify_EffectiveBetChangeToLow_ThBoard", 'ThBoard', 7, 8),  # TH 天豪棋牌
        ("Verify_EffectiveBetChangeToLow_DtBoard", 'DtBoard', 5, 6),  # DT 梦想棋牌
        ("Verify_EffectiveBetChangeToLow_DhBoard", 'DhBoard', 3, 4),  # RM 富豪棋牌
        ("Verify_EffectiveBetChangeToLow_VgBoard", 'VgBoard', 3, 5),  # VG 财神棋牌
        # ("Verify_EffectiveBetChangeToLow_TogBoard", 'TogBoard', 5, 6),  # TOG 星球棋牌
        ("Verify_EffectiveBetChangeToLow_LegBoard", 'LegBoard', 7, 8),  # LEG 乐棋牌
        ("Verify_EffectiveBetChangeToLow_GmgBoard", 'GmgBoard', 4, 5),  # GMG 光明棋牌
        ("Verify_EffectiveBetChangeToLow_Im2Board", 'Im2Board', 7, 8),  # IM 棋牌
        ("Verify_EffectiveBetChangeToLow_JlBoard", 'JlBoard', 5, 10),  # JL 棋牌
        ("Verify_EffectiveBetChangeToLow_BspBoard", 'BspBoard', 7, 9),  # BSP 棋牌
        ("Verify_EffectiveBetChangeToLow_YgBoard", 'YgBoard', 6, 7),  # YG 棋牌
        # 2020/06/22 jo新增ING棋牌
        ("Verify_EffectiveBetChangeToLow_INGBoard", 'IngBoard', 3, 5)
        # 尚未對接完成
        # ("Verify_SaBoard", 'SaBoard', '', 1, 6), # SA前台目前沒有棋牌類，暫時不對接
        # 停止合作
        # ("Verify_effective_bet_change_to_low_Mw2Board", 'Mw2Board', 7, 3),  # MW 棋牌
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
        try:
            self.assertNotEqual([], response_data[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')
            self.betRecordId = response_data[1]['PageData'][0]['Id']

            # Step2
            data = {"Id": self.betRecordId}
            response_data = self.betRecord.getDetail(data)
            self.commissionAble = Decimal(response_data[1]['Commissionable']).quantize(Decimal('0.00'))
            # print("有效投注:" + str(self.commissionAble))

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
            self.assertEqual(str(self.commissionAble), str(check_value))
        except:
            print(game_type + "目前查詢區間無資料，請產生測試注單!!")


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
