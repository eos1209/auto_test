'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import account_management
from master_api.account_login import User


class TransferUnknownMoneyBaseTest(unittest.TestCase):
    """ 转帐额度确认 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.transfer_unknown_money = account_management.TransferUnknownMoney(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_transfer_unknown_money_relatedApi_status_01(self):
        """驗證 转帐额度确认 - 取得頁面"""
        response_data = self.transfer_unknown_money.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_transfer_unknown_money_relatedApi_status_02(self):
        """驗證 转帐额度确认 - 取得列表資料"""
        data = {"count": 100, "minId": None, "query": {}}
        response_data = self.transfer_unknown_money.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_transfer_unknown_money_relatedApi_status_03(self):
        """驗證 转帐额度确认 - 取得詳細頁面"""
        response_data = self.transfer_unknown_money.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_transfer_unknown_money_relatedApi_status_04(self):
        """驗證 转帐额度确认 - 取得資料詳細"""
        data = {"count": 100, "minId": None, "query": {}}
        response_data = self.transfer_unknown_money.getList(data)
        get_data_id = response_data[1]['Data'][0]['Id']
        data = {"id": get_data_id}
        response_data = self.transfer_unknown_money.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_transfer_unknown_money_relatedApi_status_05(self):
        """驗證 转帐额度确认 - 取得娛樂城列表 2019/12/12"""
        response_data = self.transfer_unknown_money.getGameHallSearchList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_transfer_unknown_money_relatedApi_status_06(self):
        """驗證 转帐额度确认 - 取得轉帳額度狀態 2019/12/12"""
        response_data = self.transfer_unknown_money.getStates({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_transfer_unknown_money_relatedApi_status_07(self):
        """驗證 转帐额度确认 - 取得詳細資料狀態列 2019/12/12"""
        data = {"count": 100, "minId": None, "query": {}}
        response_data = self.transfer_unknown_money.getList(data)
        get_data_id = response_data[1]['Data'][0]['Id']
        data = {"id": get_data_id}
        response_data = self.transfer_unknown_money.getDetailStatusBar(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_transfer_unknown_money_relatedApi_status_08(self):
        """驗證 转帐额度确认 - 手動補額度 2019/12/12"""
        data = {"count": 100, "minId": None, "query": {}}
        response_data = self.transfer_unknown_money.getList(data)
        get_data_id = response_data[1]['Data'][0]['Id']
        data = {"MaxId": get_data_id, "query": {"IsCheckSuppliers": 'true',
                                                "Suppliers": []}}
        response_data = self.transfer_unknown_money.fillMoneyCount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
