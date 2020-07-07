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
        # 最主要去找注單回來的最後二個參數位置是在哪邊
        ("Verify_BBIN_Sport", 'BBINbbsport', '$ ', 1, 5),
        # ("Verify_BBIN_Lottery", 'BBINlottery', '$ ', 1, 5),
        ("Verify_BBIN_Live", 'BBINvideo', '$ ', 1, 10),
        ("Verify_BBIN_Slot", 'BBINprobability', '$ ', 1, 5),
        # ("Verify_BBIN_Fish30", 'BBINFish30', '$ ', 1, 6),
        # ("Verify_BBIN_Fish38", 'BBINFish38', '$ ', 1, 6),
        ("Verify_SABA_Sport", 'SabaSport', '$ ', 1, 10),
        # ("Verify_SABA_Number", 'SabaNumber', '$ ', 1, 5),
        ("Verify_SABA_VirtualSport", 'SabaVirtualSport', '$ ', 1, 10),
        # ("Verify_AG_Br", 'AgBr', '$ ', 1, 5),
        # ("Verify_AG_Ebr", 'AgEbr', '$ ', 1, 10),
        # ("Verify_AG_Hsr", 'AgHsr', '$ ', 1, 6),
        # ("Verify_AG_YoPlay", 'AgYoPlay', '$ ', 1, 7),
        ("Verify_MG_Real", 'Mg2Real', '$ ', 1, 10),
        ("Verify_MG_Slot", 'Mg2Slot', '$ ', 1, 10),
        ("Verify_MG_Html5", 'Mg2Html5', '$ ', 1, 10),
        # ("Verify_Pt_Real", 'Pt2Real', '$ ', 1, 7),
        ("Verify_Pt_Slot", 'Pt2Slot', '$ ', 1, 7),
        # ("Verify_3Sing_Sport", 'SingSport', '$ ', 1, 12),
        ("Verify_R8_Slot", 'GnsSlot', '$ ', 1, 4),
        ("Verify_PP_Slot", 'PrgSlot', '$ ', 1, 5),
        ("Verify_SG_Slot", 'SgSlot', '$ ', 1, 5),
        ("Verify_AB_Real", 'AllBetReal', '$ ', 1, 5),
        ("Verify_IG_Lottery", 'IgLottery', '$ ', 1, 7),
        # ("Verify_IG_Lotto", 'IgLotto', '$ ', 1, 10),
        ("Verify_GPK_Real", 'Rg2Real', '', 1, 5),
        ("Verify_GPK_Fish", 'Rg2Fish', '', 1, 4),
        ("Verify_GPK_Board", 'Rg2Board', '', 1, 4),
        ("Verify_GPK_Lottery", 'Rg2Lottery', '', 1, 4),
        # ("Verify_GPK_Lottery2", 'Rg2Lottery2', '', 1, 4),
        ("Verify_GPK_Slot", 'Rg2Slot', '', 1, 4),
        ("Verify_JDB_Slot", 'JdbSlot', '', 1, 4),
        ("Verify_JDB_Fish", 'JdbFish', '', 1, 3),
        ("Verify_JDB_Board", 'JdbBoard', '', 1, 6),
        ("Verify_HB_Slot", 'HabaSlot', '', 1, 10),
        ("Verify_CQ9_Slot", 'Cq9Slot', '', 1, 5),
        ("Verify_CQ9_Fish", 'Cq9Fish', '', 1, 5),
        ("Verify_EVO_Real", 'EvoReal', '', 1, 11),
        # ("Verify_NE_Slot", 'NetEntSlot', '', 1, 9), # 0531 sprint 已下架
        ("Verify_BG_Real", 'BgReal', '-', 1, 7),
        ("Verify_BG_Fish", 'BgFish', '-', 1, 7),
        ("Verify_GD_Real", 'GdReal', '', 1, 8),
        # ("Verify_GD_Slot", 'GdSlot', '', 1, 6),
        # ("Verify_TGP_Real", 'SunbetReal', '-', 1, 11), # 0531 sprint 已下架
        # ("Verify_TGP_Slot", 'RedTigerSlot', '-', 1, 10), # 0531 sprint 已下架
        # ("Verify_GA_Slot", 'GameArtSlot', '', 1, 2),
        ("Verify_MW_Slot", 'Mw2Slot', '', 1, 3),
        ("Verify_CMD_Sport", 'CmdSport', '', 1, 8),
        # ("Verify_TGP2_Real", 'Sunbet2Real', '-', 1, 11), # 0531 sprint 已下架
        # ("Verify_TGP2_Slot", 'RedTiger2Slot', '-', 1, 10), # 0531 sprint 已下架
        # ("Verify_ISB_Slot", 'IsbSlot', '', 100, 9),
        ("Verify_KG_Board", 'KgBoard', '', 1, 9),
        # ("Verify_LX_Lottery", 'LxLottery', '', 1, 6),
        ("Verify_SW_Slot", 'PtsSlot', '', 1, 2),
        ("Verify_EBET_Real", 'EBetReal', '', 1, 7),
        ("Verify_ESB_Esport", 'ImEsport', '', 1, 9),
        ("Verify_PNG_Slot", 'PngSlot', '', 1, 7),
        ("Verify_OG_Real", 'OgReal', '', 1, 5),
        # ("Verify_VR_Lottery", 'VrLottery', '', 1, 5),
        ("Verify_AP_Board", 'City761Board', '', 1, 5),
        ("Verify_AP_Fish", 'City761Fish', '', 1, 5),
        ("Verify_FG_Slot", 'FsSlot', '', 1, 6),
        ("Verify_FG_Fish", 'FsFish', '', 1, 6),
        ("Verify_FG_Board", 'FsBoard', '', 1, 6),
        ("Verify_FG_Arcade", 'FsArcade', '', 1, 6),
        # ("Verify_SA_Real", 'SaReal', '', 1, 3),
        ("Verify_IM_Sport", 'ImsSport', '', 1, 4),
        ("Verify_CR_Sport", 'IboSport', '', 1, 6),
        ("Verify_NW_Board", 'NwBoard', '', 1, 7),
        ("Verify_KA_Slot", 'KaSlot', '', 100, 9),
        ("Verify_JS_Board", 'JsBoard', '', 1, 6),
        ("Verify_JS_Slot", 'JsSlot', '', 1, 6),
        # ("Verify_JS_Fish", 'JsFish', '', 1, 6),
        ("Verify_GPK2_Sot", 'GtiSlot', '', 10000, 2),
        # ("Verify_RTG_Slot", 'RtgSlot', '', 1, 6),
        ("Verify_PS_Slot", 'PlsSlot', '', 100, 5),
        # ("Verify_MT_Fish", 'MtFish', '', 1, 6),
        ("Verify_MT_Slot", 'MtSlot', '', 1, 6),
        ("Verify_MT_Board", 'MtBoard', '', 1, 6),
        ("Verify_AE_Slot", 'AeSlot', '', 1, 5),
        ("Verify_CR2_Real", 'Ibo2Real', '', 1, 6),
        ("Verify_TH_Board", 'ThBoard', '', 1, 7),
        ("Verify_TH_Fish", 'ThFish', '', 1, 7),
        # ("Verify_GPK3_Lottery", 'LtLottery', '', 1, 4),
        ("Verify_PG_Slot", 'PgsSlot', '', 1, 3),
        ("Verify_RM_Board", 'DhBoard', '', 1, 3),
        # ("Verify_BF_Lottery", 'BfLottery', '', 1, 8),
        # ("Verify_DT_Esport", 'DtEsport', '', 1, 4),
        ("Verify_DT_Board", 'DtBoard', '', 1, 5),
        ("Verify_DT_Slot", 'DtSlot', '', 1, 4),
        ("Verify_VG_Board", 'VgBoard', '', 1, 3),
        # ("Verify_VG_Fish", 'VgFish', '', 1, 3),
        # ("Verify_TOG_Board", 'TogBoard', '', 1, 5),
        ("Verify_TOG_Slot", 'TogSlot', '', 1, 4),
        # ("Verify_VT_Slot", 'VtSlot', '', 1, 4),
        ("Verify_SE_Real", 'SeReal', '', 1, 2),
        ("Verify_GH_Slot", 'GhSlot', '', 1, 3),
        # ("Verify_LEG_Slot", 'LegSlot', '', 1, 7),
        ("Verify_LEG_Board", 'LegBoard', '', 1, 7),
        ("Verify_LEG_Fish", 'LegFish', '', 1, 7),
        ("Verify_PG2_Slot", 'Pg2Slot', '', 1, 7),
        # 2020/05/04 更新娛樂城清單
        # ("Verify_LB_Lottery", 'LbLottery', '', 1, 9),
        # ("Verify_Gmg_Board", 'GmgBoard', '', 1, 5), # 平台沒有打算要開啟
        ("Verify_Fbg_Slot", 'FbgSlot', '', 1, 4),
        ("Verify_Ll_Lottery", 'LlLottery', '', 1, 3),
        ("Verify_Im2_Slot", 'Im2Slot', '', 1, 7),
        ("Verify_Im2_Board", 'Im2Board', '', 1, 7),
        # SY
        ("Verify_Jl_Board", 'JlBoard', '', 1, 5),
        ("Verify_Jl_Fish", 'JlFish', '', 1, 5),
        ("Verify_Bsp_Slot", 'BspSlot', '', 1, 7),
        ("Verify_Bsp_Board", 'BspBoard', '', 1, 7),
        ("Verify_Bsp_Fish", 'BspFish', '', 1, 7),
        ("Verify_Yg_Slot", 'YgSlot', '', 1, 6),
        ("Verify_Yg_Board", 'YgBoard', '', 1, 6),
        ("Verify_Yg_Fish", 'YgFish', '', 1, 6),
        ("Verify_Icg_Slot", 'IcgSlot', '', 1, 3),
        ("Verify_Icg_Fish", 'IcgFish', '', 1, 3),
        # 2020/05/18 Jo新增娛樂城清單
        ("Verify_LEBO_Real", 'LeboReal', '', 1, 4),
        # 2020/06/22 Jo新增清單 ING棋牌、XBB真人、168彩票、A5彩票
        ("Verify_Ing_Board", 'IngBoard', '', 1, 3),
        ("Verify_Xbb_Real", 'XbbReal', '', 1, 11),
        ("Verify_Rg168_Lottery", 'Rg168Lottery', '', 1, 4),
        ("Verify_A5_Lottery", 'A5Lottery', '', 1, 5),
        # 下架
        # ("Verify_Pt3Real", 'Pt3Real', '', 1, 7),
        # ("Verify_Pt3Slot", 'Pt3Slot', '', 1, 7),
        # ("Verify_LgVirtualSport", 'LgVirtualSport', '', 1, 6),
        # ("Verify_Mg3Real", 'Mg3Real', '', 1, 13),
        # ("Verify_Mg3Slot", 'Mg3Slot', '', 1, 13),
        # ("Verify_GPI_Real", 'GpiReal', '$ ', 1, 8),
        # ("Verify_GPI_SlotR", 'GpiSlotR', '$ ', 1, 7),
    ])
    def testCase(self, name, game_type, cut_off_characters, proportion, data_location):
        # 測試案例名稱、遊戲類型、切割字元、換算比例、抓取的數值回傳位置
        def Amo(amount):
            bet_amount = Decimal(amount).quantize(Decimal('0.00'))
            return bet_amount

        def Val(value):
            value = value.lstrip(cut_off_characters)  # 切割$字號
            value = value.replace(',', '')  # 千位數會有,號 直接替換掉
            try:
                bet_value = Decimal(value).quantize(Decimal('0.00')) / proportion
                return bet_value
            except:
                print('發生錯誤，注單Id為' + str(self.betRecordId) + '請排查')

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
        self.betAmount = response_data[1]['BetAmount']  # 投注額

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
