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
from selenium import webdriver
from time import sleep
from data_config import portal_config


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
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.AgentSearch = member_and_agent.AgentSearch(self.__http)  # 搜尋代理商
        self.AgentDetail = member_and_agent.AgentDetail(self.__http)  # 代理商詳細資料
        self.memberVerify = member_and_agent.MemberVerifyPage(self.__http)  # 會員註冊審核
        self.user.login()
        self.oldMemberCount = 0

    def tearDown(self):
        self.user.logout()

    def test_AgentLink(self):
        """驗證 預設代理推廣鏈接是否有新增一位會員"""
        agent = self.getAgent()  # step 1: 先搜尋找出一位代理商
        # print(agent)
        agentLink = self.getAgentLink(agent)  # step 2: 取得該代理的預設推廣鏈接
        # print(agentLink)
        self.oldMemberCount = self.getOldMemberCount(agent)  # step 3: 取得代理商原本的代理會員數
        self.Portal_Register(agentLink)  # step 4: 前端註冊會員
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
        response_data = self.AgentDetail.get_detail(data)
        getOldMemberCount = response_data[1]['Agent']['MemberCount']
        return getOldMemberCount

    def Portal_Register(self, link):
        chrome_path = "D:\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.set_window_size(1900, 1020)
        self.driver.get(link)
        sleep(3)
        self.driver.find_element_by_xpath("//div[@id='announcement-dialog']/div[2]/div[2]/i").click()
        sleep(3)
        self.driver.find_element_by_xpath("//header[@id='header']/div/ul[2]/li[3]/a").click()
        sleep(3)
        self.driver.find_element_by_xpath("//fieldset[1]/div[2]/div[1]/input").send_keys(
            "QALink" + common_config.now)  # 會員帳號
        self.driver.find_element_by_xpath("//fieldset[1]/div[3]/div[1]/input").send_keys("a123456")  # 會員密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[4]/div[1]/input").send_keys("a123456")  # 確認密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[5]/div[1]/input").send_keys("123456")  # 取款密碼
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").send_keys(
            portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='btn-submit']").click()
        sleep(3)
        self.driver.close()

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

    def ValidateAgentLink(self, agentId):
        data = {"account": agentId}
        response_data = self.AgentDetail.get_detail(data)
        memberCount = response_data[1]['Agent']['MemberCount']
        validateData = self.oldMemberCount + 1  # 驗證資料
        # print(validateData)
        self.assertEqual(memberCount, validateData)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
