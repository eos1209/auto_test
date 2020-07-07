'''
@Created by loka
@Date : 2019/11/01
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from data_config import master_config
from data_config.system_config import systemSetting


class MemberCreateTest(unittest.TestCase):
    """新增會員 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberCreate = member_and_agent.MemberCreate(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberCreate_baseApi_status_01(self):
        """驗證 新增會員 - 頁面狀態"""
        response_data = self.memberCreate.createPage({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberCreate_baseApi_status_02(self):
        """ 驗證 是否為新增會員頁面 """
        response_data = self.memberCreate.isEnableAddMemberSite({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberCreate_baseApi_status_03(self):
        # 驗證 是否能夠取得預設密碼
        response_data = self.memberCreate.getDefaultPasswords({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberCreate_baseApi_status_04(self):
        """驗證 驗證使用者是否能夠新增"""
        # 帳號格式為: QA_Test月份+日期+分鐘+秒數 EX:QA_test10310501
        account = "QA_Test" + common_config.now
        data = {"account": account}
        response_data = self.memberCreate.checkAccountIsInUse(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberCreate_baseApi_status_05(self):
        """驗證 欄位驗證中使用者已有帳號時失敗"""
        data = {"account": self.config.test_Member_config()}  # Config.exist_account = QATEST
        response_data = self.memberCreate.checkAccountIsInUse(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '帐号' + '"' + self.config.test_Member_config() + '"' + '已存在')  # 帳號"QATEST"已存在

    def test_MemberCreate_baseApi_status_06(self):
        """ 驗證 預設會員密碼是否為123456"""
        response_data = self.memberCreate.getDefaultPasswords({})
        defaultPassword = response_data[1]['DefaultPassword']
        self.assertEqual(defaultPassword, '123456')

    def test_MemberCreate_baseApi_status_07(self):
        """驗證 預設取款密碼是否為123456"""
        response_data = self.memberCreate.getDefaultPasswords({})
        defaultMoneyPassword = response_data[1]['DefaultMoneyPassword']
        self.assertEqual(defaultMoneyPassword, '123456')

    def test_MemberCreate_baseApi_status_08(self):
        """驗證 代理商是否能夠空白"""
        # 帳號格式為: QA_Test月份+日期+分鐘+秒數 EX:QA_test10310501
        account = "QA_Test" + common_config.now
        data = {"Account": account}
        response_data = self.memberCreate.createSubmit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '代理商不可能空白')

    def test_MemberCreate_baseApi_status_09(self):
        """驗證 代理商是否存在"""
        # 帳號格式為: QA_Test月份+日期+分鐘+秒數 EX:QA_test10310501
        account = "QA_Test" + common_config.now
        data = {"Account": account,
                "Agent": master_config.no_exist_agent}  # Config.no_exist_agent = DS_a_player
        response_data = self.memberCreate.createSubmit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '找不到此代理商')

    def test_MemberCreate_baseApi_status_10(self):
        """驗證 提交表單中 已有帳號時失敗"""
        data = {"Account": self.config.test_Member_config(),
                "Agent": self.config.agentLv4()}
        response_data = self.memberCreate.createSubmit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '帐号' + '"' + self.config.test_Member_config() + '"' + '已存在')  # 帳號"QATEST"已存在

    def test_MemberCreate_baseApi_status_11(self):
        """驗證 使用者是否能夠新增"""
        # 帳號格式為: QA_Test月份+日期+分鐘+秒數 EX:QA_test10310501
        account = "QA_Test" + common_config.now
        agent = self.config.agentLv4()
        data = {'Account': account,
                'Agent': agent,
                'memo': '@QA_automation'}
        response_data = self.memberCreate.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberCreate_baseApi_status_12(self):
        """會員新增 - 真實姓名混入非中英文 狀態"""
        account = "QATest" + common_config.now
        agent = self.config.agentLv4()
        data = {'Account': account,
                'Agent': agent,
                'Name': account,
                'memo': '@QA_automation'}
        response_data = self.memberCreate.createSubmit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '真实姓名只接受中英文字与全、半型英文句号')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
