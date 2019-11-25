'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import unittest
from decimal import Decimal

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User
from data_config import common_config
from parameterized import parameterized


class GameCategoryRawDateForBetAmount(unittest.TestCase):
    """驗證注單投注金額與原始注單相同"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecord = reports.BetRecords(self.__http)
        self.user.login()

    @parameterized.expand([
        ("Regression_BBIN_Sport", 'BBINbbsport', '$ ', 1, 5),
        ("Regression_BBIN_Lottery", 'BBINlottery', '$ ', 1, 5),
        ("Regression_BBIN_Live", 'BBINvideo', '$ ', 1, 10),
        ("Regression_BBIN_Slot", 'BBINprobability', '$ ', 1, 5),
        ("Regression_BBIN_Fish30", 'BBINFish30', '$ ', 1, 6),
        ("Regression_BBIN_Fish38", 'BBINFish38', '$ ', 1, 6),
        ("Regression_SABA_Sport", 'SabaSport', '$ ', 1, 10),
        ("Regression_SABA_Number", 'SabaNumber', '$ ', 1, 5),
        ("Regression_SABA_VirtualSport", 'SabaVirtualSport', '$ ', 1, 10),
        ("Regression_AG_Br", 'AgBr', '$ ', 1, 5),
        ("Regression_AG_Ebr", 'AgEbr', '$ ', 1, 10),
        ("Regression_AG_Hsr", 'AgHsr', '$ ', 1, 6),
        ("Regression_AG_YoPlay", 'AgYoPlay', '$ ', 1, 7),
        ("Regression_MG_Real", 'Mg2Real', '$ ', 100, 6),
        ("Regression_MG_Slot", 'Mg2Slot', '$ ', 100, 6),
        ("Regression_MG_Html5", 'Mg2Html5', '$ ', 100, 6),
        ("Regression_Pt_Real", 'Pt2Real', '$ ', 1, 7),
        ("Regression_Pt_Slot", 'Pt2Slot', '$ ', 1, 7),
        ("Regression_3Sing_Sport", 'SingSport', '$ ', 1, 5),
        ("Regression_R8_Slot", 'GnsSlot', '$ ', 1, 4),
        ("Regression_PP_Slot", 'PrgSlot', '$ ', 1, 5),
        ("Regression_SG_Slot", 'SgSlot', '$ ', 1, 5),
        ("Regression_AB_Real", 'AllBetReal', '$ ', 1, 5),
        ("Regression_IG_Lottery", 'IgLottery', '$ ', 1, 7),
        ("Regression_IG_Lotto", 'IgLotto', '$ ', 1, 10),
        ("Regression_GPK_Real", 'Rg2Real', '', 1, 5),
        ("Regression_GPK_Fish", 'Rg2Fish', '', 1, 4),
        ("Regression_GPK_Board", 'Rg2Board', '', 1, 4),
        ("Regression_GPK_Lottery", 'Rg2Lottery', '', 1, 4),
        ("Regression_GPK_Lottery2", 'Rg2Lottery2', '', 1, 4),
        ("Regression_GPK_Slot", 'Rg2Slot', '', 1, 4),
        ("Regression_JDB_Slot", 'JdbSlot', '', 1, 4),
        ("Regression_JDB_Fish", 'JdbFish', '', 1, 3),
        ("Regression_JDB_Board", 'JdbBoard', '', 1, 6),
        ("Regression_HB_Slot", 'HabaSlot', '', 1, 10),
        ("Regression_CQ9_Slot", 'Cq9Slot', '', 1, 5),
        ("Regression_CQ9_Fish", 'Cq9Fish', '', 1, 5),
        ("Regression_EVO_Real", 'EvoReal', '', 1, 11),
        ("Regression_NE_Slot", 'NetEntSlot', '', 1, 9),
        ("Regression_BG_Real", 'BgReal', '-', 1, 7),
        ("Regression_BG_Fish", 'BgFish', '-', 1, 7),
        ("Regression_GD_Real", 'GdReal', '', 1, 8),
        ("Regression_GD_Slot", 'GdSlot', '', 1, 6),
        ("Regression_TGP_Real", 'SunbetReal', '-', 1, 11),
        ("Regression_TGP_Slot", 'RedTigerSlot', '-', 1, 10),
        ("Regression_GA_Slot", 'GameArtSlot', '', 1, 2),
        ("Regression_MW_Slot", 'Mw2Slot', '', 1, 3),
        ("Regression_CMD_Sport", 'CmdSport', '', 1, 8),
        ("Regression_TGP2_Real", 'Sunbet2Real', '-', 1, 11),
        ("Regression_TGP2_Slot", 'RedTiger2Slot', '-', 1, 10),
        ("Regression_ISB_Slot", 'IsbSlot', '', 100, 9),
        ("Regression_KG_Board", 'KgBoard', '', 1, 9),
        ("Regression_LX_Lottery", 'LxLottery', '', 1, 6),
        ("Regression_SW_Slot", 'PtsSlot', '', 1, 2),
        ("Regression_EBET_Real", 'EBetReal', '', 1, 7),
        ("Regression_ESB_Esport", 'ImEsport', '', 1, 9),
        ("Regression_PNG_Slot", 'PngSlot', '', 1, 7),
        ("Regression_OG_Real", 'OgReal', '', 1, 5),
        ("Regression_VR_Lottery", 'VrLottery', '', 1, 5),
        ("Regression_AP_Board", 'City761Board', '', 1, 5),
        ("Regression_AP_Fish", 'City761Fish', '', 1, 5),
        ("Regression_FG_Slot", 'FsSlot', '', 1, 6),
        ("Regression_FG_Fish", 'FsFish', '', 1, 6),
        ("Regression_FG_Board", 'FsBoard', '', 1, 6),
        ("Regression_FG_Arcade", 'FsArcade', '', 1, 6),
        ("Regression_SA_Real", 'SaReal', '', 1, 3),
        ("Regression_IM_Sport", 'ImsSport', '', 1, 4),
        ("Regression_CR_Sport", 'IboSport', '', 1, 6),
        ("Regression_NW_Board", 'NwBoard', '', 1, 7),
        ("Regression_KA_Slot", 'KaSlot', '', 100, 9),
        ("Regression_JS_Board", 'JsBoard', '', 1, 6),
        ("Regression_JS_Slot", 'JsSlot', '', 1, 6),
        ("Regression_JS_Fish", 'JsFish', '', 1, 6),
        ("Regression_GPK2_Sot", 'GtiSlot', '', 10000, 2),
        ("Regression_RTG_Slot", 'RtgSlot', '', 1, 6),
        ("Regression_PS_Slot", 'PlsSlot', '', 100, 5),
        ("Regression_MT_Fish", 'MtFish', '', 1, 6),
        ("Regression_MT_Slot", 'MtSlot', '', 1, 6),
        ("Regression_MT_Board", 'MtBoard', '', 1, 6),
        ("Regression_AE_Slot", 'AeSlot', '', 1, 5),
        ("Regression_CR2_Real", 'Ibo2Real', '', 1, 6),
        ("Regression_TH_Board", 'ThBoard', '', 1, 7),
        ("Regression_TH_Fish", 'ThFish', '', 1, 7),
        ("Regression_GPK3_Lottery", 'LtLottery', '', 1, 4),
        ("Regression_PG_Slot", 'PgsSlot', '', 1, 3),
        ("Regression_RM_Board", 'DhBoard', '', 1, 3),
        ("Regression_BF_Lottery", 'BfLottery', '', 1, 8),
        ("Regression_DT_Esport", 'DtEsport', '', 1, 4),
        ("Regression_DT_Board", 'DtBoard', '', 1, 5),
        ("Regression_DT_Slot", 'DtSlot', '', 1, 4),
        ("Regression_VG_Board", 'VgBoard', '', 1, 3),
        ("Regression_VG_Fish", 'VgFish', '', 1, 3),
        # ("Regression_TOG_Board", 'TogBoard', '', 1, 5),
        ("Regression_TOG_Slot", 'TogSlot', '', 1, 4),
        ("Regression_VT_Slot", 'VtSlot', '', 1, 4),
        ("Regression_SE_Real", 'SeReal', '', 1, 2),
        ("Regression_GH_Slot", 'GhSlot', '', 1, 3),
        ("Regression_LEG_Slot", 'LegSlot', '', 1, 7),
        ("Regression_LEG_Board", 'LegBoard', '', 1, 7),
        ("Regression_LEG_Fish", 'LegFish', '', 1, 7),
        ("Regression_PG2_Slot", 'Pg2Slot', '', 1, 7),
        # 下架
        # ("Regression_Pt3Real", 'Pt3Real', '', 1, 7),
        # ("Regression_Pt3Slot", 'Pt3Slot', '', 1, 7),
        # ("Regression_LgVirtualSport", 'LgVirtualSport', '', 1, 6),
        # ("Regression_Mg3Real", 'Mg3Real', '', 1, 13),
        # ("Regression_Mg3Slot", 'Mg3Slot', '', 1, 13),
        # ("Regression_GPI_Real", 'GpiReal', '$ ', 1, 8),
        # ("Regression_GPI_SlotR", 'GpiSlotR', '$ ', 1, 7),
    ])
    def testCase(self, name, game_type, cut_off_characters, proportion, data_location):
        # 測試案例名稱、遊戲類型、切割字元、換算比例、抓取的數值回傳位置
        def Amo(amount):
            bet_amount = Decimal(amount).quantize(Decimal('0.00'))
            return bet_amount

        def Val(value):
            value = value.lstrip(cut_off_characters)
            bet_value = Decimal(value).quantize(Decimal('0.00')) / proportion
            return bet_value

        self.verifyBetAmountSameOriginalAmount(game_type, data_location, Amo, Val)

    def tearDown(self):
        self.user.logout()

    # 呼叫方法
    def verifyBetAmountSameOriginalAmount(self, game_type, data_location, bet_amount_func, bet_value_func):
        # Step Start 查詢對應由遊戲注單
        data = {"GameCategories": game_type,
                "WagersTimeBegin": common_config.WagersTimeBegin,
                "Round": " ",
                "connectionId": self.user.info()}
        response_data = self.betRecord.search(data)

        # Step1 判斷是否有注單存在
        self.assertNotEqual([], response_data[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')
        self.betRecordId = response_data[1]['PageData'][0]['Id']

        # Step2 抓取詳細頁面資料
        data = {"Id": self.betRecordId}
        response_data = self.betRecord.getDetail(data)
        self.betAmount = response_data[1]['BetAmount']

        # Step3 抓取原始注單資料
        data = {"Id": self.betRecordId}
        response_data = self.betRecord.getRawData(data)
        self.betValue = response_data[1]['List'][data_location]['Value']

        # Step4 驗證下注金額與原始注單投注金額一致
        bet_amount = bet_amount_func(self.betAmount)
        bet_value = bet_value_func(self.betValue)
        self.assertEqual(str(bet_amount), str(bet_value))


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
