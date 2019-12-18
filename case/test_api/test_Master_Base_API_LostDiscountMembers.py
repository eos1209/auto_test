'''
@Created by loka
@Date : 2019/12/09
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import account_management
from master_api.account_login import User


class LostDiscountMembersBaseTest(unittest.TestCase):
    """時返異常紀錄- 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.lostDiscountMembers = account_management.LostDiscountMembers(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_LostDiscountMembers_baseApi_status_01(self):
        """驗證 時返異常紀錄 - 頁面狀態"""
        data = {'query': {'Status': [1, 2], 'IsCheckStatus': 'true'}, 'take': 100, 'skip': 0}
        response_data = self.lostDiscountMembers.getLostDiscountMembers(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
