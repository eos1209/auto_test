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


class SiteParameterBaseTest(unittest.TestCase):
    """ 聯絡資訊 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = PortalManagement.SiteParameter(self.__http)
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

    def test_ModifyRegisterCopywriting_relatedApi_status_01(self):
        """ 聯絡資訊 - 取得聯絡資訊 狀態"""
        data = {"WebsiteId": self.getWebsiteId()}
        response_data = self.siteParameter.GetSiteParameter(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ModifyRegisterCopywriting_relatedApi_status_02(self):
        """ 聯絡資訊 - 更新聯絡資訊 狀態"""
        data = {"WebsiteId": self.getWebsiteId(),
                "Parameters": [{"Key": "Live800Link", "Value": "http://tw.yahoo.com", "Memo": "在线客服123"},
                               {"Key": "Live800LinkReview", "Value": "https://www.mobile01.com/", "Memo": "12test"},
                               {"Key": "Live800LinkComputer", "Value": "http://www.fnjtd.com/", "Memo": ""},
                               {"Key": "TEL", "Value": "123456", "Memo": "客服专线75435435"},
                               {"Key": "QQ", "Value": "40037457",
                                "Memo": "QQ號碼http://wpa.qq.com/msgrd?v=3&uin=40037457&site=qq&menu=yes"},
                               {"Key": "Email", "Value": "http://www.google.com.tw", "Memo": "客服Email"},
                               {"Key": "Skype", "Value": "", "Memo": "Skype"},
                               {"Key": "OfficialEmail", "Value": "", "Memo": ""},
                               {"Key": "ComplaintsEmail", "Value": "", "Memo": ""},
                               {"Key": "ComplaintsTEL", "Value": "", "Memo": ""},
                               {"Key": "ComplaintsQQ", "Value": "9876543210", "Memo": "test"},
                               {"Key": "HttpWeibo", "Value": "", "Memo": ""},
                               {"Key": "HttpWhatsapp", "Value": "", "Memo": ""},
                               {"Key": "AgentQQ", "Value": "https://www.yahoo.com.tw", "Memo": ""},
                               {"Key": "PartnerQQ", "Value": "333", "Memo": ""},
                               {"Key": "Live800LinkAgent", "Value": "", "Memo": ""},
                               {"Key": "AgentLogin", "Value": "", "Memo": ""},
                               {"Key": "AgentEmail", "Value": "555", "Memo": ""},
                               {"Key": "AgentWechat", "Value": "", "Memo": ""},
                               {"Key": "AgentSkype", "Value": "", "Memo": ""},
                               {"Key": "Dialog",
                                "Value": "https://cdn2.igsttech.com/Web.Portal/CJ001-01.Portal/Upload/Dialog/25.png",
                                "Memo": ""},
                               {"Key": "DialogFooter", "Value": "<center>測試</center>", "Memo": ""},
                               {"Key": "DialogPage", "Value": "/test", "Memo": "/"},
                               {"Key": "DialogTitle", "Value": "<center>最新公告</center>", "Memo": ""},
                               {"Key": "HttpInformation", "Value": "20190515", "Memo": ""},
                               {"Key": "HttpMobileDeposit", "Value": "http://www.yahoo.com", "Memo": "線上存款"},
                               {"Key": "HttpMobilePromotion", "Value": "/HorizontalMobile/Promotion", "Memo": ""},
                               {"Key": "HttpVIP", "Value": "http://www.google.com.tw", "Memo": "VIP金管家 -- K版"},
                               {"Key": "HttpLive", "Value": "http://www.yahoo.com", "Memo": "真人金庫 -- K版"},
                               {"Key": "MobileDomain", "Value": "123456", "Memo": ""},
                               {"Key": "TestKey", "Value": "TestKey", "Memo": "145"},
                               {"Key": "HttpMobile2Deposit", "Value": "http://tw.yahoo.com", "Memo": "123"},
                               {"Key": "Skpye", "Value": "bb@bb.bb1126", "Memo": "94 使該ㄆ"},
                               {"Key": "新的 KEY-1", "Value": "9999", "Memo": ""}]}

        response_data = self.siteParameter.UpdateSiteParameter(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
