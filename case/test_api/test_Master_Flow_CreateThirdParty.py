'''
@Created by yuhsiang
@Date : 2018/12/7
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import system_management
from master_api.account_login import User


class MasterCreateThirdParty(unittest.TestCase):
    """創建線上支付商戶"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.groupThirdParty = system_management.GroupThirdParty(self.__http)
        self.user.login()

    def test_master_flow_create_DTTP(self):
        # Step1 創建金流商戶 API 調用
        data = {"AvailableMinutes": 20,
                "Name": "QA - 微信13",
                "Type": "12355",
                "TypeValue": 4,
                "Min": 1,
                "Max": 10,
                "Limit": 20,
                "RecommendationMemo": "測試",
                "Memo": "微信測試",
                "RecommendationAmountSettings": [{
                    "Sort": 1,
                    "Amount": 5
                },
                    {
                        "Sort": 2,
                        "Amount": 10
                    }],
                "MemberLevelSettingIds": [14],
                "Settings": [{
                    "key": "Account",
                    "value": "201908024"
                },
                    {
                        "key": "Password",
                        "value": "GFHGFDGFHDFGHGF"
                    },
                    {
                        "key": "Gateway",
                        "value": "http://www.baidu.com/"
                    }]}
        self.submit = self.groupThirdParty.create_dtpp_submit(data)

    def tearDown(self):
        self.user.logout()


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
