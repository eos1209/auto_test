'''
@Created by JO
@Date : 2020/07/06
'''

import unittest
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement, GPKRewardRecords
from master_api.Home import Home
from master_api.account_login import User
from data_config.system_config import systemSetting
from base import TimeClass


class GPKRewardRecordsBaseTest(unittest.TestCase):
    """ GPK2打賞匯出 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.home = Home(self.__http)
        self.siteParameter = GPKRewardRecords(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    # 登出
    def tearDown(self):
        self.user.logout()

    def test_GPKRewardRecords_relatedApi_status_01(self):
        """驗證 匯出 - GPK2打賞Excel 狀態"""
        data = {
            "dateBegin": TimeClass.betRecord_start(),
            "dateEnd": TimeClass.betRecord_end()
        }
        response_data = self.siteParameter.getExcel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
