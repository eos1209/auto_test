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


class CheckGameDetailUrl(unittest.TestCase):
    """驗證外部注單連結"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecord = reports.BetRecords(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @parameterized.expand([
        ("verify_bet_detail_Url_Mg2Real", 'Mg2Real'),
        ("verify_bet_detail_Url_Mg2Slot", 'Mg2Slot'),
        ("verify_bet_detail_Url_Mg2Html5", 'Mg2Html5'),
        ("verify_bet_detail_Url_PrgSlot", 'PrgSlot'),
        ("verify_bet_detail_Url_GdSlot", 'GdSlot'),
        ("verify_bet_detail_Url_Cq9Slot", 'Cq9Slot'),
        ("verify_bet_detail_Url_Cq9Fish", 'Cq9Fish'),
        ("verify_bet_detail_Url_HabaSlot", 'HabaSlot'),
        ("verify_bet_detail_Url_City761Board", 'City761Board'),
        ("verify_bet_detail_Url_City761Fish", 'City761Fish'),
        ("verify_bet_detail_Url_IboSport", 'IboSport'),
        ("verify_bet_detail_Url_Ibo2Real", 'Ibo2Real'),
        ("verify_bet_detail_Url_JdbBoard", 'JdbBoard'),
        ("verify_bet_detail_Url_JdbSlot", 'JdbSlot'),
        ("verify_bet_detail_Url_JdbFish", 'JdbFish'),
        ("verify_bet_detail_Url_KaSlot", 'KaSlot'),
        ("verify_bet_detail_Url_PlsSlot", 'PlsSlot'),
        ("verify_bet_detail_Url_PngSlot", 'PngSlot'),
        ("verify_bet_detail_Url_Pt2Real", 'Pt2Real'),
        ("verify_bet_detail_Url_Pt2Slot", 'Pt2Slot'),
        ("verify_bet_detail_Url_Rg2Real", 'Rg2Real'),
        ("verify_bet_detail_Url_Rg2Board", 'Rg2Board'),
        ("verify_bet_detail_Url_Rg2Lottery2", 'Rg2Lottery2'),
        ("verify_bet_detail_Url_MtFish", 'MtFish'),
        ("verify_bet_detail_Url_MtSlot", 'MtSlot'),
        ("verify_bet_detail_Url_MtBoard", 'MtBoard'),
        ("verify_bet_detail_Url_ThBoard", 'ThBoard'),
        ("verify_bet_detail_Url_ThFish", 'ThFish'),
        ("verify_bet_detail_Url_SabaSport", 'SabaSport'),
        ("verify_bet_detail_Url_SabaNumber", 'SabaNumber'),
        ("verify_bet_detail_Url_SabaVirtualSport", 'SabaVirtualSport'),
        # ("verify_bet_detail_Url_SabaHorse", 'SabaHorse'),
        # ("verify_bet_detail_Url_SabaLiveCasino", 'SabaLiveCasino'),
        # 2019/5/29 新增
        ("verify_bet_detail_Url_BfLottery", 'BfLottery'),
        ("verify_bet_detail_Url_DhBoard", 'DhBoard'),
        ("verify_bet_detail_Url_DtBoard", 'DtBoard'),
        ("verify_bet_detail_Url_EBetReal", 'EBetReal'),
        ("verify_bet_detail_Url_KgBoard", 'KgBoard'),
        ("verify_bet_detail_Url_RedTiger2Slot", 'RedTiger2Slot'),
        ("verify_bet_detail_Url_RedTigerSlot", 'RedTigerSlot'),
        ("verify_bet_detail_Url_Sunbet2Real", 'Sunbet2Real'),
        ("verify_bet_detail_Url_SunbetReal", 'SunbetReal'),
        ("verify_bet_detail_Url_LtLottery", 'LtLottery'),
        # 下架
        # ("Regression_BetDetailUrl_Mg3Real", 'Mg3Real'),
        # ("Regression_BetDetailUrl_Mg3Slot", 'Mg3Slot'),
        # ("Regression_BetDetailUrl_Pt3Real", 'Pt3Real'),
        # ("Regression_BetDetailUrl_Pt3Slot", 'Pt3Slot'),
        # ("Regression_BetDetailUrl_LgVirtualSport", 'LgVirtualSport'),
    ])
    def testCase(self, name, game_type):
        # 測試案例名稱、遊戲类型
        # Step1 查詢注單 取得注單ID
        data = {"WagersTimeBegin": common_config.WagersTimeBegin,
                "GameCategories": [game_type],
                "connectionId": self.user.info()}
        response_data = self.betRecord.search(data)
        # 判斷注單是否有資料存在
        self.assertNotEqual([], response_data[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')
        self.betRecordId = response_data[1]['PageData'][0]['Id']

        # Step2 用注單ID 找到BetDetailUrl
        data = {"id": self.betRecordId,
                "rawDataType": game_type}
        response_data = self.betRecord.getBetDetailUrl(data)
        self.actualResultStatue = response_data[0]

        # Step3 確認狀態是否為 200 並且有回傳值
        if common_config.Status_Code == str(self.actualResultStatue) and (not response_data[1] is None):
            flag_status1 = True
        else:
            flag_status1 = False

        # Step4 驗證
        self.assertEqual(flag_status1, True)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
