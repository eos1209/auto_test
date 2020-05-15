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
from data_config.system_config import systemSetting
from base.CommonMethod import Portal_test


class ThirdPartyPaymentBaseTest(unittest.TestCase):
    """ 线上支付看板 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = account_management.ThirdPartyPayment(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.thirdPartyPayment = account_management.ThirdPartyPayment(cls.__http)
        cls.user.login()

    def getId(self):
        data = {"count": 25, "query": {"isDTPP": 'true', "search": 'null'}}
        response_data = self.thirdPartyPayment.load_new(data)
        getId = response_data[1]['Data'][0]['Id']
        return getId

    def test_ThirdPartyPayment_relatedApi_status_01(self):
        """驗證 线上支付看板 - 取得頁面"""
        ThirdPartyPaymentBaseTest.Master_login()
        response_data = self.thirdPartyPayment.get_index_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayment_relatedApi_status_02(self):
        """驗證 线上支付看板 - 取得列表資料"""

        data = {"count": "25",
                "query": {"isDTPP": "true",
                          "search": "null"
                          }
                }
        response_data = self.siteParameter.load_new(data)
        status_code = response_data[0]
        # self.get_verify_deposit_id = response_data[1]['Data'][0]['Id'] # 暫時拿掉
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayment_relatedApi_status_03(self):
        """驗證 线上支付看板 - 匯出"""
        data = {"isDTPP": "true",
                "search": "null"
                }
        response_data = self.siteParameter.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayment_relatedApi_status_04(self):
        """驗證 线上支付看板 - 取得訂單狀態"""
        response_data = self.thirdPartyPayment.get_apply_states({})
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

    def test_ThirdPartyPayment_relatedApi_status_07(self):
        """驗證 线上支付看板 - 拒絕 狀態"""
        self.portal = Portal_test()
        self.portal.OnlineDeposit_Create_V2(self.config.test_Member_config(), self.config.test_Password_config())
        self.portal.OnlineDeposit_Send_V2(self.config.test_Member_config(), self.config.test_Password_config())
        ThirdPartyPaymentBaseTest.Master_login()
        Id = self.getId()
        data = {'id': Id}
        response_data = self.thirdPartyPayment.cancel_dtpp_order(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayment_relatedApi_status_08(self):
        """驗證 线上支付看板 - 同意 狀態"""
        self.portal = Portal_test()
        self.portal.OnlineDeposit_Create_V2(self.config.test_Member_config(), self.config.test_Password_config())
        self.portal.OnlineDeposit_Send_V2(self.config.test_Member_config(), self.config.test_Password_config())
        Id = self.getId()
        data = {'id': Id}
        response_data = self.thirdPartyPayment.allow_dTPP_manual(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
