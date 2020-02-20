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
from data_config.system_config import systemSetting


class RegisterCopyWritingBaseTest(unittest.TestCase):
    """ 會員註冊文案 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.registerCopyWriting = PortalManagement.RegisterCopywriting(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.siteName_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def getOtherWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.other_Website_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def test_ModifyRegisterCopywriting_relatedApi_status_01(self):
        """ 會員註冊文案 - 取得文案 狀態"""
        data = {"WebsiteId": self.getWebsiteId()}
        response_data = self.registerCopyWriting.GetRegisterCopywriting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ModifyRegisterCopywriting_relatedApi_status_02(self):
        """ 會員註冊文案 - 修改文案 狀態"""
        # 直接取得文案
        data = {"WebsiteId": self.getWebsiteId()}
        response_data = self.registerCopyWriting.GetRegisterCopywriting(data)
        getCopyWriting = response_data[1]['Copywriting']
        getAgreementSetting = response_data[1]['AgreementSetting']
        data = {"websiteId": self.getWebsiteId(),
                "copywriting": getCopyWriting,
                "agreementSetting": getAgreementSetting}
        response_data = self.registerCopyWriting.ModifyRegisterCopywriting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ModifyRegisterCopywriting_relatedApi_status_03(self):
        """ 會員註冊文案 - 複製到其他網站 狀態"""
        data = {"FromWebsiteId": self.getWebsiteId(),
                "ToWebsiteIdList": [self.getOtherWebsiteId()]}
        response_data = self.registerCopyWriting.CopyRegisterCopywriting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
