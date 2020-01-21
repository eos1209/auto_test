'''
@Created by loka
@Date : 2020/01/20
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement
from master_api.account_login import User


class RegisterCopyWritingBaseTest(unittest.TestCase):
    """ 會員註冊文案 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.registerCopyWriting = PortalManagement.RegisterCopywriting(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_ModifyRegisterCopywriting_relatedApi_status_01(self):
        """ 會員註冊文案 - 取得文案 狀態"""
        data = {"WebsiteId": "29"}
        response_data = self.registerCopyWriting.GetRegisterCopywriting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ModifyRegisterCopywriting_relatedApi_status_02(self):
        """ 會員註冊文案 - 修改文案 狀態"""
        # 直接取得文案
        data = {"WebsiteId": "29"}
        response_data = self.registerCopyWriting.GetRegisterCopywriting(data)
        getCopyWriting = response_data[1]['Copywriting']
        getAgreementSetting = response_data[1]['AgreementSetting']
        data = {"websiteId": "29",
                "copywriting": getCopyWriting,
                "agreementSetting": getAgreementSetting}
        response_data = self.registerCopyWriting.ModifyRegisterCopywriting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ModifyRegisterCopywriting_relatedApi_status_03(self):
        """ 會員註冊文案 - 複製到其他網站 狀態"""
        data = {"FromWebsiteId": "29", "ToWebsiteIdList": [86]}
        response_data = self.registerCopyWriting.CopyRegisterCopywriting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
