# '''# 已更新到新專案-故此註解 done 2020/07/17
# @Created by yuhsiang
# @Date : 2018/12/7
# '''
#
# import unittest
#
# from base.HTMLTestReportCN import HTMLTestRunner
# from base.httpRequest import HttpRequest
# from master_api import reports
# from master_api.account_login import User
# from data_config import common_config
# from parameterized import parameterized
#
#
# class CheckGameDetailUrl(unittest.TestCase):
#     """驗證外部注單連結(當發生key Error:'Url')，表示該娛樂城小紅有問題"""
#
#     def setUp(self):
#         self.__http = HttpRequest()
#         self.user = User(self.__http)
#         self.betRecord = reports.BetRecords(self.__http)
#         self.user.login()
#
#     def tearDown(self):
#         self.user.logout()
#
#     @parameterized.expand([
#         ("Verify_BetDetailUrl_Mg2Real", 'Mg2Real'),
#         ("Verify_BetDetailUrl_Mg2Slot", 'Mg2Slot'),
#         ("Verify_BetDetailUrl_Mg2Html5", 'Mg2Html5'),
#         ("Verify_BetDetailUrl_PrgSlot", 'PrgSlot'),
#         ("Verify_BetDetailUrl_GdSlot", 'GdSlot'),
#         ("Verify_BetDetailUrl_Cq9Slot", 'Cq9Slot'),
#         ("Verify_BetDetailUrl_Cq9Fish", 'Cq9Fish'),
#         ("Verify_BetDetailUrl_HabaSlot", 'HabaSlot'),
#         ("Verify_BetDetailUrl_City761Board", 'City761Board'),
#         ("Verify_BetDetailUrl_City761Fish", 'City761Fish'),
#         ("Verify_BetDetailUrl_IboSport", 'IboSport'),
#         ("Verify_BetDetailUrl_Ibo2Real", 'Ibo2Real'),
#         ("Verify_BetDetailUrl_JdbBoard", 'JdbBoard'),
#         ("Verify_BetDetailUrl_JdbSlot", 'JdbSlot'),
#         ("Verify_BetDetailUrl_JdbFish", 'JdbFish'),
#         ("Verify_BetDetailUrl_KaSlot", 'KaSlot'),
#         ("Verify_BetDetailUrl_PlsSlot", 'PlsSlot'),
#         ("Verify_BetDetailUrl_PngSlot", 'PngSlot'),
#         ("Verify_BetDetailUrl_Pt2Real", 'Pt2Real'),
#         ("Verify_BetDetailUrl_Pt2Slot", 'Pt2Slot'),
#         ("Verify_BetDetailUrl_Rg2Real", 'Rg2Real'),
#         ("Verify_BetDetailUrl_Rg2Board", 'Rg2Board'),
#         # ("Verify_BetDetailUrl_Rg2Lottery2", 'Rg2Lottery2'),
#         ("Verify_BetDetailUrl_MtFish", 'MtFish'),
#         ("Verify_BetDetailUrl_MtSlot", 'MtSlot'),
#         ("Verify_BetDetailUrl_MtBoard", 'MtBoard'),
#         ("Verify_BetDetailUrl_ThBoard", 'ThBoard'),
#         ("Verify_BetDetailUrl_ThFish", 'ThFish'),
#         ("Verify_BetDetailUrl_SabaSport", 'SabaSport'),
#         ("Verify_BetDetailUrl_SabaNumber", 'SabaNumber'),
#         ("Verify_BetDetailUrl_SabaVirtualSport", 'SabaVirtualSport'),
#         # ("Verify_BetDetailUrl_SabaHorse", 'SabaHorse'),
#         # ("Verify_BetDetailUrl_SabaLiveCasino", 'SabaLiveCasino'),
#         # 2019/5/29 新增
#         # ("Verify_BetDetailUrl_BfLottery", 'BfLottery'),
#         ("Verify_BetDetailUrl_DhBoard", 'DhBoard'),
#         ("Verify_BetDetailUrl_DtBoard", 'DtBoard'),
#         ("Verify_BetDetailUrl_EBetReal", 'EBetReal'),
#         ("Verify_BetDetailUrl_KgBoard", 'KgBoard'),
#         ("Verify_BetDetailUrl_RedTiger2Slot", 'RedTiger2Slot'),
#         ("Verify_BetDetailUrl_RedTigerSlot", 'RedTigerSlot'),
#         ("Verify_BetDetailUrl_Sunbet2Real", 'Sunbet2Real'),
#         ("Verify_BetDetailUrl_SunbetReal", 'SunbetReal'),
#         ("Verify_BetDetailUrl_LlLottery", 'LlLottery'),
#         ("Verify_BetDetailUrl_Im2Slot", 'Im2Slot'),
#         ("Verify_BetDetailUrl_Im2Board", 'Im2Board'),
#         ("Verify_BetDetailUrl_JlFish", 'JlFish'),
#         ("Verify_BetDetailUrl_JlBoard", 'JlBoard'),
#         ("Verify_BetDetailUrl_BspBoard", 'BspBoard'),
#         ("Verify_BetDetailUrl_BspSlot", 'BspSlot'),
#         ("Verify_BetDetailUrl_BspFish", 'BspFish'),
#         ("Verify_BetDetailUrl_YgFish", 'YgFish'),
#         ("Verify_BetDetailUrl_YgBoard", 'YgBoard'),
#         ("Verify_BetDetailUrl_YgSlot", 'YgSlot'),
#         ("Verify_BetDetailUrl_IcgSlot", 'IcgSlot'),
#         ("Verify_BetDetailUrl_IcgFish", 'IcgFish'),
#         # 2020/06/20 新增清單 A5彩票
#         ("Verify_BetDetailUrl_A5Lottery", 'A5Lottery'),
#         # 2020/06/22 新增清單 ING棋牌、XBB真人
#         ("Verify_BetDetailUrl_IngBoard", 'IngBoard'),  # 需掛VPN才能看到正確小紅
#         ("Verify_BetDetailUrl_XbbReal", 'XbbReal'),
#         # 下架
#         # ("Verify_BetDetailUrl_Mg3Real", 'Mg3Real'),
#         # ("Verify_BetDetailUrl_Mg3Slot", 'Mg3Slot'),
#         # ("Verify_BetDetailUrl_Pt3Real", 'Pt3Real'),
#         # ("Verify_BetDetailUrl_Pt3Slot", 'Pt3Slot'),
#         # ("Verify_BetDetailUrl_LgVirtualSport", 'LgVirtualSport'),
#     ])
#     def testCase(self, name, game_type):
#         # 測試案例名稱、遊戲类型
#         # Step1 查詢注單 取得注單ID
#         data = {"WagersTimeBegin": common_config.WagersTimeBegin,
#                 "GameCategories": [game_type],
#                 "connectionId": self.user.info()}
#         response_data = self.betRecord.search(data)
#         # 判斷注單是否有資料存在
#         try:
#             self.assertNotEqual([], response_data[1]['PageData'], '目前查詢區間無資料，請產生測試注單!!')
#             self.betRecordId = response_data[1]['PageData'][0]['Id']
#             # Step2 用注單ID 找到BetDetailUrl
#             data = {"id": self.betRecordId,
#                     "rawDataType": game_type}
#             response_data = self.betRecord.getBetDetailUrl(data)
#             self.actualResultStatue = response_data[0]
#
#             # Step3 確認狀態是否為 200 並且有回傳值
#             if common_config.Status_Code == str(self.actualResultStatue) and (not response_data[1]['Url'] is None):
#                 flag_status1 = True
#             else:
#                 flag_status1 = False
#
#             # Step4 驗證
#             self.assertEqual(flag_status1, True)
#         except:
#             print(game_type + "目前查詢區間無資料，請產生測試注單!!")
#
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HTMLTestRunner())
