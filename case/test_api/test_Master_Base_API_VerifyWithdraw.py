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


class VerifyWithdrawBaseTest(unittest.TestCase):
    """ 取款申请审核 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.verifyWithdraw = account_management.VerifyWithdraw(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_VerifyWithdraw_relatedApi_status_01(self):
        """驗證 取款申请审核 - 取得頁面"""
        data = {}
        response_data = self.verifyWithdraw.index(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_02(self):
        """驗證 取款申请审核 - 取得詳細資料"""
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verifyWithdraw.load(data)
        get_verify_withdraw_id = response_data[1]['Data'][0]['Id']

        data = {"id": get_verify_withdraw_id,
                "connectionId": self.user.info()}
        response_data = self.verifyWithdraw.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_03(self):
        """驗證 取款申请审核 - 匯出"""
        data = {"search": None}
        response_data = self.verifyWithdraw.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_04(self):
        """驗證 取款申请审核 - 取得訂單狀態"""
        data = {}
        response_data = self.verifyWithdraw.getApplyStates(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_05(self):
        """驗證 取款申请审核 - 取得詳細頁面"""
        data = {}
        response_data = self.verifyWithdraw.detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_06(self):
        """驗證 取款申请审核 - 取得列表資料"""
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verifyWithdraw.load(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
