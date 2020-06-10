'''
@Created by loka
@Date : 2020/06/09
'''
import unittest
from agent_api.agent_login import agent_login
from data_config.system_config import systemSetting
from base.agent_httpReuest import Agent_Http
from data_config.agent_config import Post_Agent_Headers
from base.TimeClass import betRecord_start,get_todaynow

class AgentBaseTest(unittest.TestCase):
    """代理 - 相關 API 調用狀態"""

    def setUp(self) -> None:
        self.http = Agent_Http()
        self.cookie = agent_login()
        self.config = systemSetting()
        self.beginDay = betRecord_start()
        self.endDay = get_todaynow()

    def test_Agent_api_status_01(self):
        """會員搜尋"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Member/Search', data, Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_02(self):
        """會員詳細資料"""
        data = {"account": "QATEST"}
        response_data = self.http.post(self.config.agent_link() + '/Member/GetDetail', data, Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_03(self):
        """交易紀錄查詢類型"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/MemberTransaction/QueryInit', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_04(self):
        """交易紀錄查詢"""
        data = {"Types": ["Account", "ThirdPartyPayment", "OnlineWithdraw", "Manual", "Bonus", "Discount",
                          "AnyTimeDiscount", "Yuebao"]}
        response_data = self.http.post(self.config.agent_link() + '/MemberTransaction/Search', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_05(self):
        """傭金計算"""
        data = {"beginDate": self.beginDay, "endDate": self.endDay}
        response_data = self.http.post(self.config.agent_link() + '/Commission/GetCommission', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_06(self):
        """匯出傭金計算"""
        data = {"beginDate": self.beginDay, "endDate": self.endDay}
        response_data = self.http.post(self.config.agent_link() + '/Commission/GetCommission', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        getId = response_data[1]['RecordId']
        data = {"RecordId": getId}
        response_data = self.http.post(self.config.agent_link() + '/Commission/Export', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_07(self):
        """取得娛樂城"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/BetRecord/GetSupplierCategories', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_08(self):
        """取得娛樂城種類"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/BetRecord/GetKindCategories', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_09(self):
        """確認是否為最後一層代理"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Statistics/IsAgentLastestLevel', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_10(self):
        """投注記錄查詢"""
        data = {"WagersTimeBegin": self.beginDay, "connectionId": "968616a9-b757-4ef6-8374-dbfdd8eb9741"}
        response_data = self.http.post(self.config.agent_link() + '//BetRecord/Search', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')
