'''
@Created by loka
@Date : 2020/06/09
'''
import unittest
from agent_api.agent_login import agent_login, connectionId
from data_config.system_config import systemSetting
from base.agent_httpReuest import Agent_Http
from data_config.agent_config import Post_Agent_Headers, Get_Agent_Headers
from base.TimeClass import betRecord_start, get_todaynow


class AgentBaseTest(unittest.TestCase):
    """代理 - 相關 API 調用狀態"""

    def setUp(self) -> None:
        self.http = Agent_Http()
        self.cookie = agent_login()
        self.config = systemSetting()
        self.beginDay = betRecord_start()
        self.endDay = get_todaynow()
        self.info = connectionId()

    def test_Agent_api_status_01(self):
        """會員搜尋"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Member/Search', data, Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_02(self):
        """會員詳細資料"""
        data = {"account": "DS_1114_test"}
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
        data = {"WagersTimeBegin": self.beginDay, "connectionId": self.info}
        response_data = self.http.post(self.config.agent_link() + '/BetRecord/Search', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_11(self):
        """會員查詢-頁面"""
        response_data = self.http.get(self.config.agent_link() + '/Member/Query', {},
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_12(self):
        """取得Agent語系"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Home/AgentLanguageKey', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_13(self):
        """取得Agent語系"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Home/GetAuthorities', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_14(self):
        """取得自訂代理"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Home/GetCustomizedLinks', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_15(self):
        """取得自訂代理"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/Bullitin/Index', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_16(self):
        """取得自訂代理"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Home/GetCustomizedAgentLink', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_17(self):
        """取得會員詳細資料頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/Member/Detail', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_18(self):
        """取得代理商查詢頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/Agent/Query', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_19(self):
        """取得所有代理等級"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Agent/GetAllLevel', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_20(self):
        """取得代理搜尋"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Agent/Search', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_21(self):
        """取得代理搜尋"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/Statistics/Index', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_22(self):
        """取得是否最後一層代理層級"""
        data = {}
        response_data = self.http.post(self.config.agent_link() + '/Statistics/IsAgentLastestLevel', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_23(self):
        """取得投注記錄查詢頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/BetRecord/Query', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_24(self):
        """取得投注詳細資料頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/BetRecord/Detail', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_25(self):
        """取得投注詳細資料"""
        data = {"id": "6286525"}
        response_data = self.http.post(self.config.agent_link() + '/BetRecord/GetDetail', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_26(self):
        """取得投注詳細資料"""
        data = {"id": "6286525"}
        response_data = self.http.post(self.config.agent_link() + '/BetRecord/GetDetail', data,
                                       Post_Agent_Headers,
                                       self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_27(self):
        """取得傭金計算頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/Commission/Index', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_28(self):
        """取得傭金計算頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/MemberTransaction/Query', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_29(self):
        """取得傭金計算頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/Statistics/GetAgentInfo', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')

    def test_Agent_api_status_30(self):
        """取得傭金計算頁面"""
        data = {}
        response_data = self.http.get(self.config.agent_link() + '/Account/SignOut', data,
                                      Get_Agent_Headers,
                                      self.cookie)
        status = response_data[0]
        self.assertEqual(status, '200')