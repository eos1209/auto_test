'''
@Created by loka
@Date : 2020/01/07
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api.account_login import User
from master_api import system_management


class GameHallgetBackofficeUrl(unittest.TestCase):
    """娛樂城管理 - 針對 BB、IG、GPK、LX、VR、GPK2、LL這些娛樂城進行回傳網址驗證"""

    # 驗證步驟
    # step 1: 針對回傳網址做驗證，未來如果有相關Task需要回來補上

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.GameHailManagement = system_management.GameHallManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_BB_Link(self):
        """BB進入後台驗證"""
        data = {"gameSupplierType": 1}
        response_data = self.GameHailManagement.getBackofficeUrl(data)
        validateData = 'https://ag.fjieojio.com'
        self.assertEqual(validateData, response_data[1]['Url'])

    def test_IG_Link(self):
        """IG進入後台驗證"""
        data = {"gameSupplierType": 21}
        response_data = self.GameHailManagement.getBackofficeUrl(data)
        validateData = 'http://cag.ppkp88.com'
        self.assertEqual(validateData, response_data[1]['Url'])

    def test_GPK_Link(self):
        """GPK進入後台驗證"""  # 禮拜四例行地進行維護，會有錯誤是正常的
        data = {"gameSupplierType": 25}
        response_data = self.GameHailManagement.getBackofficeUrl(data)
        validateData = 'https://webapi.machplay.cc/lotteryAgent_ssoLogin'
        self.assertEqual(validateData, response_data[1]['Url'][:48])

    def test_LX_Link(self):
        """LX進入後台驗證"""
        data = {"gameSupplierType": 44}
        response_data = self.GameHailManagement.getBackofficeUrl(data)
        validateData = 'http://gpkapiqt.ying036.com/home/ApiLogin'
        self.assertEqual(validateData, response_data[1]['Url'][:41])

    def test_GPK2_Link(self):
        """GPK2進入後台驗證"""
        data = {"gameSupplierType": 59}
        response_data = self.GameHailManagement.getBackofficeUrl(data)
        validateData = 'http://gtibackend.dhdcl.com/auth_login'
        self.assertEqual(validateData, response_data[1]['Url'][:38])

    def test_LL_Link(self):
        """LL進入後台驗證"""
        data = {"gameSupplierType": 82}
        response_data = self.GameHailManagement.getBackofficeUrl(data)
        validateData = 'https://api.fhll.online/admin/autoLogin.html'
        self.assertEqual(validateData, response_data[1]['Url'][:44])


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
