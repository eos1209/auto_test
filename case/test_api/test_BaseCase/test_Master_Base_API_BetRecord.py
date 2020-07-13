'''
@Created by loka
@Date : 2020/01/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import reports
from master_api.account_login import User
from data_config.system_config import systemSetting


class BetRecordBaseTest(unittest.TestCase):
    """投注記錄查詢 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecords = reports.BetRecords(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        data = {"WagersTimeBegin": common_config.FirstDay}
        response_data = self.betRecords.search(data)
        Id = response_data[1]['PageData'][0]['Id']
        return Id

    # 混合過關注單會有錯誤
    def test_BetRecord_relatedApi_status_01(self):
        """驗證 SABA體育-混合過關 狀態"""
        data = {"parlaySportBetId": self.config.SabaSportMixParlaySubTickets_config()}  # 注單號:5852323
        response_data = self.betRecords.getSabaSportMixParlaySubTickets(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_02(self):
        """驗證 Cmd體育-混合過關 狀態"""
        data = {"socTransId": self.config.CmdParlaySubRawData_config()}  # 注單號:5852016
        response_data = self.betRecords.getCmdParlaySubRawData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_03(self):
        """驗證 CR體育(Ibo)-混合過關 狀態"""
        data = {"BetId": "13128154"}  # 注單號:5848896
        response_data = self.betRecords.getIboParlaySubRawData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_04(self):
        """驗證 3Sing體育-混合過關 狀態"""
        data = {"rawDataId": self.config.SingParlaySubRawData()}  # 注單號:5852343
        response_data = self.betRecords.getSingParlaySubRawData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_05(self):
        """驗證 IM體育-混合過關 狀態"""
        data = {"wagerId": self.config.ImsParlaySubRawData()}  # 注單號:5852017
        response_data = self.betRecords.getImsParlaySubRawData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_06(self):
        """驗證 ESB電競-混合過關 狀態"""
        data = {"BetId": self.config.ImParlaySubRawData()}  # 注單號:5852344
        response_data = self.betRecords.getImParlaySubRawData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_07(self):
    #     """驗證 投注記錄查詢-取得頁面 狀態"""
    #     response_data = self.betRecords.query({})
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_08(self):
    #     """驗證 投注记录查询-取得所有 GameType 的名稱 狀態"""
    #     response_data = self.betRecords.getGameTypeNames({})
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_09(self):
    #     """驗證 投注記錄查詢-取得各娛樂城，以及所屬的遊戲類型 狀態"""
    #     response_data = self.betRecords.getSupplierCategories({})
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_10(self):
    #     """驗證 投注記錄查詢-取得遊戲種類，以及所屬的遊戲類型 狀態"""
    #     response_data = self.betRecords.getKindCategories({})
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code,response_data[3])

    # def test_BetRecord_relatedApi_status_11(self):
    #     """驗證 投注记录查询-查詢 狀態"""
    #     data = {"WagersTimeBegin": common_config.TodayDate, "connectionId": self.user.info()}
    #     response_data = self.betRecords.search(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_12(self):
    #     """驗證 投注记录查询-匯出 狀態"""
    #     data = {"WagersTimeBegin": common_config.FirstDay}
    #     response_data = self.betRecords.export(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_13(self):
    #     """驗證 投注记录查询-取得詳細資訊頁面 狀態"""
    #     response_data = self.betRecords.detail({})
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_14(self):
    #     """驗證 投注记录查询-取得投注紀錄詳細資訊 狀態"""
    #     Id = self.getId()
    #     data = {"id": Id}
    #     response_data = self.betRecords.getDetail(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_15(self):
    #     """驗證 投注记录查询-取得注單詳細資訊 狀態"""
    #     Id = self.getId()
    #     data = {"id": Id}
    #     response_data = self.betRecords.getRawData(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_16(self):
    #     """驗證 投注记录查询-進階查詢頁面 狀態"""
    #     response_data = self.betRecords.advanced({})
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_17(self):
    #     """驗證 投注记录查询-取得所有進階顯示的種類 狀態"""
    #     response_data = self.betRecords.advancedCategories({})
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_18(self):
    #     """驗證 投注记录查询-取得進階顯示資料 狀態"""
    #     data = {"searchParams": {"WagersTimeBegin": common_config.BeginDate, "WagersTimeEnd": common_config.EndDate},
    #             "pageSize": 100}
    #     response_data = self.betRecords.advancedLoadV2(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_19(self):
    #     """驗證 投注记录查询-進階顯示匯出 狀態"""
    #     # step 1:取得要匯出的娛樂城參數
    #     data = {"searchParams": {"WagersTimeBegin": common_config.BeginDate, "WagersTimeEnd": common_config.EndDate},
    #             "pageSize": 100}
    #     response_data = self.betRecords.advancedLoadV2(data)
    #     category = response_data[1]['Category']
    #     data = {"searchParams": {"WagersTimeBegin": common_config.BeginDate, "WagersTimeEnd": common_config.EndDate},
    #             "category": category}
    #     response_data = self.betRecords.advancedExportV2(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_20(self):
        """驗證 SABA(虛擬體育)-混合過關 狀態"""
        data = {'parlaySportBetId': self.config.SabaVirtualSportMixParlaySubTickets_config()}  # 注單號:5852950
        response_data = self.betRecords.getSabaVirtualSportMixParlaySubTickets(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_21(self):
    #     """驗證 名字+遊戲名稱查詢 狀態"""
    #     data = {"WagersTimeBegin": common_config.BeginDate, "connectionId": self.user.info()}
    #     response_data = self.betRecords.search(data)
    #     account = response_data[1]['PageData'][0]['Account']
    #     game_type = response_data[1]['PageData'][0]['GameType']
    #     data = {"Account": account, "WagersTimeBegin": common_config.BeginDate, "GameTypeName": game_type,
    #             "GameTypeNameIsLike": 'false', "connectionId": self.user.info()}
    #     response_data = self.betRecords.search(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
