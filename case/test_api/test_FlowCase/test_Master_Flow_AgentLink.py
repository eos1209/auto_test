'''
@Created by loka
@Date : 2019/12/23
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from base.CommonMethod import PortalExecution


class AgentLink(unittest.TestCase):
    """代理推廣鏈接 - 預設推廣鏈接是否有效讓新增的會員納入該代理底下"""

    # 驗證步驟
    # step 1: 先搜尋找出一位代理商
    # step 2: 取得該代理的預設推廣鏈接
    # step 3: 取得代理商原本的代理會員數
    # step 4: 前端註冊會員
    # step 5: 審核該會員
    # step 6: 驗證該代理是否有增加底下會員
    def setUp(self):
        self.oldMemberCount = 0

    def tearDown(self):
        self.user.logout()

    @classmethod
    def Master_Login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.AgentSearch = member_and_agent.AgentSearch(cls.__http)  # 搜尋代理商
        cls.AgentDetail = member_and_agent.AgentDetail(cls.__http)  # 代理商詳細資料
        cls.memberVerify = member_and_agent.MemberVerifyPage(cls.__http)  # 會員註冊審核
        cls.user.login()

    def test_AgentLink(self):
        """驗證 預設代理推廣鏈接是否有新增一位會員"""
        AgentLink.Master_Login()
        agent = self.getAgent()  # step 1: 先搜尋找出一位代理商
        # print(agent)
        agentLink = self.getAgentLink(agent)  # step 2: 取得該代理的預設推廣鏈接
        # print(agentLink)
        self.oldMemberCount = self.getOldMemberCount(agent)  # step 3: 取得代理商原本的代理會員數

        self.portal = PortalExecution()
        Account = 'QA_Link' + common_config.now
        self.portal.AgentLink(agentLink, Account)  # step 4: 前端註冊會員
        AgentLink.Master_Login()
        self.Member_Verify()  # step 5: 審核該會員
        self.ValidateAgentLink(agent)  # step 6: 驗證該代理是否有增加底下會員

    def getAgent(self):
        data = {"AgentLevelId": "4"}
        response_data = self.AgentSearch.search(data)
        getAgentList = response_data[1]['PageData'][0]['Account']
        return getAgentList

    def getAgentLink(self, agent):
        data = {"account": agent}
        response_data = self.AgentDetail.get_detail(data)
        getAgentLink = response_data[1]['Agent']['AgentLinkOriginal']
        return getAgentLink

    def getOldMemberCount(self, agent):
        data = {"account": agent}
        response_data = self.AgentDetail.getAgentLayerDetail(data)
        getOldMemberCount = response_data[1]['AgentLayerInfo']['MemberCount']
        return getOldMemberCount

    def Member_Verify(self):
        listData = {'take': 100, 'search': {}}
        getData = self.memberVerify.getList(listData)
        Id = getData[1]['Data'][0]['Id']
        verifyAccount = getData[1]['Data'][0]['SubmitAccount']
        # print(verifyAccount)
        data = {'Id': Id, 'verifyAccount': verifyAccount}  # 審核通過該會員
        self.memberVerify.approve(data)
        data = {'id': Id, 'newMemo': '@QA_AgentLinkTest'}
        self.memberVerify.updateMemo(data)

    def ValidateAgentLink(self, agent):
        data = {"account": agent}
        response_data = self.AgentDetail.getAgentLayerDetail(data)
        # print(response_data[1])
        memberCount = response_data[1]['AgentLayerInfo']['MemberCount']
        validateData = self.oldMemberCount + 1  # 驗證資料
        # print(validateData)
        self.assertEqual(memberCount, validateData)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
