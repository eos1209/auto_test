'''
@Created by loka
@Date : 2019/11/08
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User


class AgentSearchBaseTest(unittest.TestCase):
    """代理商查询 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.agentSearch = member_and_agent.AgentSearch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_AgentSearch_relatedApi_status_01(self):
        """驗證 代理商查询頁面 狀態"""
        response_data = self.agentSearch.query({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentSearch_relatedApi_status_02(self):
        """驗證 代理商查詢頁面 取得所有會員等級"""
        response_data = self.agentSearch.get_all_member_levels({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentSearch_relatedApi_status_03(self):
        """驗證 代理商查詢頁面 取得所有返水設定"""
        response_data = self.agentSearch.get_all_discount_settings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentSearch_relatedApi_status_04(self):
        """驗證 代理商查詢頁面 取得所有佣金設定"""
        response_data = self.agentSearch.get_all_commission_settings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentSearch_relatedApi_status_05(self):
        """驗證 代理商查詢頁面 取得所有代理商等級"""
        response_data = self.agentSearch.getAllLevel({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentSearch_relatedApi_status_06(self):
        """驗證 代理商查詢頁面 取得所有代理商等級"""
        response_data = self.agentSearch.search({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentSearch_relatedApi_status_07(self):
        """驗證 代理商查詢頁面 匯出Excel"""
        response_data = self.agentSearch.export({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
