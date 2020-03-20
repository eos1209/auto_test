'''
@Created by loka
@Date : 2019/11/15
'''

import unittest
from data_config import common_config
import random
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from time import sleep
from base.CommonMethod import PortalExecution
from data_config.system_config import systemSetting


class MemberRegisterVerifyTest(unittest.TestCase):
    """會員註冊審核 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        # self.__http = HttpRequest()
        # self.user = User(self.__http)
        # self.memberVerify = member_and_agent.MemberVerifyPage(self.__http)
        # self.user.login()

    def tearDown(self):
        self.user.logout()

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.memberVerify = member_and_agent.MemberVerifyPage(cls.__http)
        cls.user.login()

    @classmethod
    def Portal(cls):
        account = 'QATest' + common_config.now
        cls.portal = PortalExecution()
        cls.portal.Register(account)

    def test_MemberRegisterVerify_baseApi_status_01(self):
        """驗證 會員註冊審核-取得各站台資訊"""
        MemberRegisterVerifyTest.Master_login()  # 登入
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
        data = {'item': self.config.agentLv4()}
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
        MemberRegisterVerifyTest.Portal()
        MemberRegisterVerifyTest.Master_login()  # 登入
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
        MemberRegisterVerifyTest.Portal()
        MemberRegisterVerifyTest.Master_login()  # 登入
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
        MemberRegisterVerifyTest.Portal()
        MemberRegisterVerifyTest.Master_login()  # 登入
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
