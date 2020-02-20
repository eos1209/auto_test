'''
@Created by yuhsiang
@Date : 2019/4/19
'''

import unittest

from base.CommonMethod import SetDelayTime
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from data_config.system_config import systemSetting


class MemberSearchBaseTest(unittest.TestCase):
    """会员查询 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = member_and_agent.MemberSearch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberSearch_relatedApi_status_01(self):
        """驗證 会员查询頁面 狀態"""
        response_data = self.memberSearch.query_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_02(self):
        """驗證 会员查询 狀態"""
        # 因修改查詢頻率限制
        SetDelayTime()
        data = {"Account": self.config.test_Member_config(),
                "connectionId": self.user.info()}
        response_data = self.memberSearch.search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_03(self):
        """驗證 会员查询 未帶 connectionId 狀態"""
        # 因修改查詢頻率限制
        SetDelayTime()
        data = {"Account": self.config.test_Member_config()}
        response_data = self.memberSearch.search(data)
        error_message = response_data[1]['ErrorMessage']
        self.assertEqual(error_message, "connectionId cannot be null.")

    def test_MemberSearch_relatedApi_status_04(self):
        """驗證 會員等級 狀態"""
        response_data = self.memberSearch.getAllMemberLevels({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_05(self):
        """驗證 反水等級 狀態"""
        response_data = self.memberSearch.getAllDiscountSettings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_06(self):
        """驗證 匯出檔案標籤 狀態"""
        response_data = self.memberSearch.getColumnForExport({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_07(self):
        """驗證 功能開關 狀態"""
        response_data = self.memberSearch.getShelfFunctionSwitch({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_08(self):
        """驗證 匯出檔案 狀態"""
        data = {"search": {"Account": self.config.test_Member_config()}, "columns": [1, 2], "connectionId": self.user.info()}
        response_data = self.memberSearch.exportMemberSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberSearch_relatedApi_status_09(self):
        """驗證 會員搜尋 - 進階 區域驗證 狀態"""
        data = {'IsNeedRegionValidate': 'true', 'connectionId': self.user.info()}
        response_data = self.memberSearch.search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_MemberSearch_relatedApi_status_10(self): # 超級會員查詢
    #     data = {"connectionId": self.user.info(), "pageIndex": 0, "search": {"advanceSearch": {
    #         "memberTransactionRequests": [
    #             {"beginTime": "2020/01/14 00:00:00", "endTime": "2020/01/15 23:59:59", "amountMin": -1,
    #              "amountMax": -10,
    #              "types": ["Payoff"], "amountIsPay": 'true'}]}, "pageIndex": 0}}
    #     response_data = self.memberSearch.superSearch(data)
    #     print(response_data[1])


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
