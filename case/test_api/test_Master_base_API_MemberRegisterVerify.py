'''
@Created by loka
@Date : 2019/11/15
'''

import unittest
from data_config import master_config
from data_config import common_config
from data_config import portal_config
import random
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from selenium import webdriver
from time import sleep


class MemberRegisterVerifyTest(unittest.TestCase):
    """會員註冊審核 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberVerify = member_and_agent.MemberVerifyPage(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def PortalExecutionMemberRegister(self):
        chrome_path = "D:\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_path)
        # self.driver = webdriver.Chrome()
        self.driver.set_window_size(1900, 1020)
        self.driver.get("http://www.fnjtd.com/Register")
        self.driver.find_element_by_id("parentAccount").send_keys("QA_Test11070110")
        self.driver.find_element_by_xpath("//fieldset[1]/div[2]/div[1]/input").send_keys("QAtest" + common_config.now)  # 會員帳號
        self.driver.find_element_by_xpath("//fieldset[1]/div[3]/div[1]/input").send_keys("a123456")  # 會員密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[4]/div[1]/input").send_keys("a123456")  # 確認密碼
        self.driver.find_element_by_xpath("//fieldset[1]/div[5]/div[1]/input").send_keys("123456")  # 取款密碼
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").send_keys(portal_config.PortalCheckCode)  # 萬用碼
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='checkcode-input-group']/input").click()
        sleep(3)
        self.driver.close()

    def test_MemberRegisterVerify_baseApi_status_01(self):
        """驗證 會員註冊審核-取得各站台資訊"""
        response_data = self.memberVerify.getSetting({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_02(self):
        """驗證 會員註冊審核-取得所有狀態"""
        response_data = self.memberVerify.getAllStatus({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_03(self):
        """驗證 會員註冊審核-取得看板資料"""
        data = {'take': 100, 'search': {}}
        response_data = self.memberVerify.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_04(self):
        """驗證 會員註冊審核-取得詳細資料"""
        getData = {'take': 100, 'search': {}}
        getlist = self.memberVerify.getList(getData)
        getlist_Id = getlist[1]['Data'][0]['Id']
        data = {'id': getlist_Id, 'connectionId': self.user.info()}
        response_data = self.memberVerify.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_05(self):
        """驗證 會員註冊審核-取得設定資料"""
        response_data = self.memberVerify.getSetting({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_06(self):
        """驗證 會員註冊審核-更新審核有效分鐘數"""
        minute = random.randint(1, 60)  # 亂數決定有效分鐘數
        data = {'availableMinutes': minute}
        response_data = self.memberVerify.updateAvailableMinutes(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_07(self):
        """驗證 會員註冊審核-更新會員註冊審核開關"""
        data = {'webSiteId': 29, 'status': 'false'}  # 29為AB005
        response_data = self.memberVerify.updateWebSiteMemberRegisterVerifySwitch(data)
        status_code = response_data[0]
        trueData = {'webSiteId': 29, 'status': 'true'}
        self.memberVerify.updateWebSiteMemberRegisterVerifySwitch(trueData)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_08(self):
        """驗證 會員註冊審核-更新域名狀態"""
        data = {'status': 'true'}
        response_data = self.memberVerify.updateDomainNameStatus(data)
        status_code = response_data[0]
        falseData = {'status': 'false'}
        self.memberVerify.updateDomainNameStatus(falseData)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_09(self):
        """驗證 會員註冊審核-新增域名"""
        data = {"item": 'QAtest' + common_config.now + '.com'}
        response_data = self.memberVerify.createDomainNameItem(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_10(self):
        """驗證 會員註冊審核-刪除域名"""
        response = self.memberVerify.getSetting({})
        getDomainName_id = response[1]['ReturnObject']['DomainNamesSetting']['Item'][0]['Id']
        getDomainName_value = response[1]['ReturnObject']['DomainNamesSetting']['Item'][0]['Url']
        data = {'id': getDomainName_id, 'value': getDomainName_value}
        # print(getDomainName_value)
        response_data = self.memberVerify.deleteDomainNameItem(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_11(self):
        """驗證 會員註冊審核-更新代理商狀態"""
        data = {'status': 'true'}
        response_data = self.memberVerify.updateAgentStatus(data)
        status_code = response_data[0]
        falseData = {'status': 'false'}
        self.memberVerify.updateAgentStatus(falseData)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_12(self):
        """驗證 會員註冊審核-新增代理商項目"""
        data = {'item': master_config.exist_agent}
        response_data = self.memberVerify.createAgentItem(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_13(self):
        """驗證 會員註冊審核-刪除代理商項目"""
        response = self.memberVerify.getSetting({})
        getAgentItem_Id = response[1]['ReturnObject']['AgentsSetting']['Item'][0]['Id']
        getAgentItem_value = response[1]['ReturnObject']['AgentsSetting']['Item'][0]['Account']
        data = {'id': getAgentItem_Id, 'value': getAgentItem_value}
        response_data = self.memberVerify.deleteAgentItem(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_14(self):
        """驗證 會員註冊審核-審核會員"""
        self.PortalExecutionMemberRegister()  # 前端執行
        sleep(1)
        listData = {'take': 100, 'search': {}}
        getData = self.memberVerify.getList(listData)
        account = getData[1]['Data'][0]['SubmitAccount']
        data = {'account': account}
        response_data = self.memberVerify.checkAccountIsInUse(data)
        status_code = response_data[0]
        deny_id = getData[1]['Data'][0]['Id']  # 驗證完成後拒絕帳號
        data = {'Id': deny_id}  # 拒絕帶入id
        self.memberVerify.deny(data)  # 拒絕
        self.assertEqual(status_code, common_config.Status_Code)
        sleep(1)

    def test_MemberRegisterVerify_baseApi_status_15(self):
        """驗證 會員註冊審核-會員註冊審核設定歷史紀錄"""
        listData = {'take': 100, 'skip': 0, 'search': {}}
        response_data = self.memberVerify.getHistoryList(listData)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_16(self):
        """驗證 會員註冊審核-同意"""
        self.PortalExecutionMemberRegister()  # 前端執行
        listData = {'take': 100, 'search': {}}
        getData = self.memberVerify.getList(listData)
        Id = getData[1]['Data'][0]['Id']
        verifyAccount = getData[1]['Data'][0]['SubmitAccount']
        # print(verifyAccount)
        data = {'Id': Id, 'verifyAccount': verifyAccount}
        response_data = self.memberVerify.approve(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_17(self):
        """驗證 會員註冊審核-更新備註"""
        listData = {'take': 100, 'search': {}}
        getData = self.memberVerify.getList(listData)
        Id = getData[1]['Data'][0]['Id']
        data = {'id': Id, 'newMemo': '@QA_automation'}
        response_data = self.memberVerify.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberRegisterVerify_baseApi_status_18(self):
        """驗證 會員註冊審核-拒絕"""
        self.PortalExecutionMemberRegister()  # 前端執行
        listData = {'take': 100, 'search': {}}
        getData = self.memberVerify.getList(listData)
        accountId = getData[1]['Data'][0]['Id']
        data = {'Id': accountId}
        response_data = self.memberVerify.deny(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        sleep(1)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
