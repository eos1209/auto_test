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


class ThirdPartyPaymentBaseTest(unittest.TestCase):
    """ 线上支付看板 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.thirdPartyPayment = account_management.ThirdPartyPayment(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_ThirdPartyPayment_relatedApi_status_01(self):
        """驗證 线上支付看板 - 取得頁面"""
        data = {}
        response_data = self.thirdPartyPayment.get_index_page(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayment_relatedApi_status_02(self):
        """驗證 线上支付看板 - 取得列表資料"""
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.thirdPartyPayment.load_new(data)
        status_code = response_data[0]
        self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayment_relatedApi_status_03(self):
        """驗證 线上支付看板 - 匯出"""
        data = {"isDTPP": True,
                "search": None}
        response_data = self.thirdPartyPayment.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayment_relatedApi_status_04(self):
        """驗證 线上支付看板 - 取得訂單狀態"""
        data = {}
        response_data = self.thirdPartyPayment.get_apply_states(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_ThirdPartyPayment_relatedApi_status_05(self):
    #     """驗證 线上支付看板 - 取得詳細頁面"""
    #     data = {}
    #     response_data = self.statistics.detailPage(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, Config.Status_Code)
    #
    # def test_ThirdPartyPayment_relatedApi_status_06(self):
    #     """驗證 线上支付看板 - 取得詳細資料"""
    #     data = {"count": 100,
    #             "query":
    #                 {"search": None}
    #             }
    #     response_data = self.statistics.load(data)
    #     self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
    #
    #     data = {"id": self.get_verify_deposit_id}
    #     response_data = self.statistics.getDetail(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, Config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
