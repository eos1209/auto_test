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


class VerifyDepositBaseTest(unittest.TestCase):
    """ 公司入款审核 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 參數設定
        # self.__http = HttpRequest()
        # self.user = User(self.__http)

    def tearDown(self):
        self.user.logout()

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.verify_deposit = account_management.VerifyDeposit(cls.__http)
        cls.user.login()

    def test_VerifyDeposit_relatedApi_status_01(self):
        """驗證 公司入款审核 - 取得頁面"""
        # response_data = self.verifyDeposit.index(data)
        # self.Portal_VerifyDeposit()
        VerifyDepositBaseTest.Master_login()
        response_data = self.verify_deposit.get_index_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_02(self):
        """驗證 公司入款审核 - 取得列表資料"""
        VerifyDepositBaseTest.Master_login()
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verify_deposit.get_load_data(data)
        status_code = response_data[0]
        self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_03(self):
        """驗證 公司入款审核 - 匯出"""
        VerifyDepositBaseTest.Master_login()
        data = {"search": None}
        response_data = self.verify_deposit.export_data(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_04(self):
        """驗證 公司入款审核 - 取得訂單狀態"""
        VerifyDepositBaseTest.Master_login()
        response_data = self.verify_deposit.get_apply_states({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_05(self):
        """驗證 公司入款审核 - 取得詳細頁面"""
        VerifyDepositBaseTest.Master_login()
        response_data = self.verify_deposit.get_detail_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_06(self):
        """驗證 公司入款审核 - 取得詳細資料"""
        VerifyDepositBaseTest.Master_login()
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verify_deposit.get_load_data(data)
        self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
        data = {"id": self.get_verify_deposit_id}
        response_data = self.verify_deposit.get_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_07(self):
        """驗證 公司入款审核 - 拒絕"""
        # getId = VerifyDepositBaseTest.Portal()
        self.portal = Portal_test()
        self.portal.CompanyDeposit(self.config.test_Member_config(), self.config.test_Password_config())
        VerifyDepositBaseTest.Master_login()
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verify_deposit.get_load_data(data)
        self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
        data = {"id": self.get_verify_deposit_id}
        response_data = self.verify_deposit.order_deny(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyDeposit_relatedApi_status_08(self):
        """驗證 公司入款审核 - 同意"""
        self.portal = Portal_test()
        self.portal.CompanyDeposit(self.config.test_Member_config(), self.config.test_Password_config())
        VerifyDepositBaseTest.Master_login()
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verify_deposit.get_load_data(data)
        self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
        data = {"id": self.get_verify_deposit_id}
        response_data = self.verify_deposit.order_allow(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
