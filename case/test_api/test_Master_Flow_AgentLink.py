# '''
# @Created by loka
# @Date : 2019/12/23
# '''
# import unittest
# from data_config import common_config
# from base.HTMLTestReportCN import HTMLTestRunner
# from base.httpRequest import HttpRequest
# from master_api import member_and_agent
# from master_api.account_login import User
# from data_config import master_config
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from data_config import portal_config
#
#
# class AgentLink(unittest.TestCase):
#     """代理推廣鏈接 - 預設推廣鏈接是否有效讓新增的會員納入該代理底下"""
#
#     # 驗證步驟
#     # step 1: 先搜尋找出一位代理商
#     # step 2: 取得該代理的預設推廣鏈接
#     # step 3: 前端註冊會員
#     # step 4: 審核該會員
#     # step 5: 驗證該代理是否有增加底下會員
#     def setUp(self):
#         self.__http = HttpRequest()
#         self.user = User(self.__http)
#         self.AgentSearch = member_and_agent.AgentSearch(self.__http)  # 搜尋代理商
#         self.AgentDetail = member_and_agent.AgentDetail(self.__http)  # 代理商詳細資料
#         self.memberVerify = member_and_agent.MemberVerifyPage(self.__http)  # 會員註冊審核
#         self.user.login()
#
#     def tearDown(self):
#         self.user.logout()
#
#     def test_AgentLink(self):
#         """驗證 預設代理推廣鏈接是否有新增一位會員"""
#         agent = self.getAgent()  # step 1: 先搜尋找出一位代理商
#         print(agent)
#         agentlink = self.getAgentLink(agent)  # step 2: 取得該代理的預設推廣鏈接
#         print(agentlink)
#         self.Portal_Register(agentlink)  # step 3: 前端註冊會員
#         # self.Member_Verifty()  # step 4: 審核該會員
#         # self.Validateagentlink(agent) # step 5: 驗證該代理是否有增加底下會員
#
#     def getAgent(self):
#         data = {"AgentLevelId": "4"}
#         response_data = self.AgentSearch.search(data)
#         getAgentlist = response_data[1]['PageData'][0]['Account']
#         return getAgentlist
#
#     def getAgentLink(self, agent):
#         data = {"account": agent}
#         response_data = self.AgentDetail.get_detail(data)
#         getAgentLink = response_data[1]['Agent']['AgentLinkOriginal']
#         return getAgentLink
#
#     def Portal_Register(self, link):
#         chrome_path = "D:\chromedriver.exe"
#         self.driver = webdriver.Chrome(chrome_path)
#         self.driver.set_window_size(1900, 1020)
#         self.driver.get(link)
#         sleep(5)
#         self.driver.find_element(By.CSS_SELECTOR, ".join > a").click()
#         self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .control-div > .ng-invalid").click()
#         self.driver.find_element(By.CSS_SELECTOR, ".control-div > .ng-dirty").send_keys("ffff")
#         self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .ng-invalid").click()
#         self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .ng-dirty").send_keys("fffff")
#         self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) .form-control").click()
#         self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) .form-control").send_keys("ffff")
#         self.driver.find_element(By.CSS_SELECTOR, ".control-div > .ng-invalid").click()
#         self.driver.find_element(By.CSS_SELECTOR, ".ng-scope > .control-div > .ng-dirty").send_keys("ffff")
#         self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(3)").click()
#         self.driver.find_element(By.CSS_SELECTOR, "#checkcode-input-group > .ng-pristine").click()
#         self.driver.find_element(By.CSS_SELECTOR, "#checkcode-input-group > .ng-dirty").send_keys("ffff")
#         self.driver.find_element(By.ID, "btn-submit").click()
#
#     def Member_Verifty(self):
#         listData = {'take': 100, 'search': {}}
#         getData = self.memberVerify.getList(listData)
#         Id = getData[1]['Data'][0]['Id']
#         verifyAccount = getData[1]['Data'][0]['SubmitAccount']
#         # print(verifyAccount)
#         data = {'Id': Id, 'verifyAccount': verifyAccount}
#         self.memberVerify.approve(data)
#
#     def Validateagentlink(self, agentId):
#         data = {"account": agentId}
#         response_data = self.AgentDetail.get_detail(data)
