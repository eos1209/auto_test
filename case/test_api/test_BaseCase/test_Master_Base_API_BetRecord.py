'''
@Created by loka
@Date : 2020/01/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from data_config import master_config
from master_api import reports
from master_api.account_login import User


class BetRecordBaseTest(unittest.TestCase):
    """投注記錄查詢 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecords = reports.BetRecords(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_BetRecord_relatedApi_status_01(self):
        """驗證 SABA體育-混合過關 狀態"""
        data = {"parlaySportBetId": "333"}  # 注單號:5852323
        response_data = self.betRecords.getSabaSportMixParlaySubTickets(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_02(self):
        """驗證 Cmd體育-混合過關 狀態"""
        data = {"socTransId": "620678450"}  # 注單號:5852016
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
        data = {"rawDataId": "179"}  # 注單號:5852343
        response_data = self.betRecords.getSingParlaySubRawData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BetRecord_relatedApi_status_05(self):
        """驗證 IM體育-混合過關 狀態"""
        data = {"wagerId": "2001062222418848"}  # 注單號:5852017
        response_data = self.betRecords.getImsParlaySubRawData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_BetRecord_relatedApi_status_06(self):
    #     """驗證 ESB電競-混合過關 狀態"""

if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
