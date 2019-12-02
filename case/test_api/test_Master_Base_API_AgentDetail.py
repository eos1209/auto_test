'''
@Created by loka
@Date : 2019/11/08
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import memeber_and_agent
from master_api.account_login import User
import random
from data_config import master_config


class AgentDetailTest(unittest.TestCase):
    """代理商詳細資料 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.agentDetail = memeber_and_agent.AgentDetail(self.__http)
        self.AgentSearch = memeber_and_agent.AgentSearchPage(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_AgentDetail_baseApi_status_01(self):
        """驗證 代理商詳細資料 - 頁面狀態"""
        response_data = self.agentDetail.detail()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_02(self):
        """驗證 代理商詳細資料 - 取得所有返水設定"""
        response_data = self.agentDetail.getAllDiscountSettings()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_03(self):
        """驗證 代理商詳細資料 - 取得所有會員等級"""
        response_data = self.agentDetail.getAllMemberLevels()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_04(self):
        """驗證 代理商詳細資料 - 取得所有佣金設定"""
        response_data = self.agentDetail.getAllCommissionSettings()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_05(self):
        """驗證 代理商詳細資料 - 取得詳細資料"""
        data = {'account': master_config.exist_agent}
        response_data = self.agentDetail.get_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_06(self):
        """驗證 代理商詳細資料 - 停用代理商"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'id': account_Id[1]['Agent']['Id']}
        response_data = self.agentDetail.disable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_07(self):
        """驗證 代理商詳細資料 - 啟用代理商"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'id': account_Id[1]['Agent']['Id']}
        response_data = self.agentDetail.active(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_08(self):
        """驗證 代理商詳細資料 - 修改自訂推廣鏈接"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {
            "agentId": account_Id[1]['Agent']['Id'],
            "links": [{"Sort": 1, "Url": "xxxxx"}]
        }
        response_data = self.agentDetail.updateCustomizedAgentLinks(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_09(self):
        """驗證 代理商詳細資料 - 修改推廣鏈接"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {"id": account_Id[1]['Agent']['Id'], "agentLink": "http://4444"}
        response_data = self.agentDetail.updateAgentLink(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_10(self):
        """驗證 代理商詳細資料 - 更新代理推廣鏈接"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'id': account_Id[1]['Agent']['Id'], 'status': 'true'}
        response_data = self.agentDetail.updateAgentLinkStatus(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_11(self):
        """驗證 代理商詳細資料 - 修改更新佣金設定"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'agentId': account_Id[1]['Agent']['Id'], 'commissionSettingId': '37'}
        response_data = self.agentDetail.updateCommissionSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_12(self):
        """驗證 代理商詳細資料 - 更新預設會員等級"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'agentId': account_Id[1]['Agent']['Id'], 'memberLevelSettingId': '21'}
        response_data = self.agentDetail.updateDefaultMemberLevelSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_13(self):
        """驗證 代理商詳細資料 - 更新預設返水等級"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'agentId': account_Id[1]['Agent']['Id'], 'discountSettingId': '137'}
        response_data = self.agentDetail.updateDefaultDiscountSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_14(self):
        """驗證 代理商詳細資料 - 檢查更新代理商權限"""
        data = {'account': master_config.exist_agent}
        response_data = self.agentDetail.checkUpdateAgentAuthority(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_15(self):
        """驗證 代理商詳細資料 - 取得修改代理商基本資料頁面"""
        response_data = self.agentDetail.modifyAgentInfo()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_16(self):
        """驗證 代理商詳細資料 - 更新代理商基本資料"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {
            'Id': account_Id[1]['Agent']['Id'],
            'Name': 'QA_Test' + common_config.now,
            'Mobile': '987654312',
            'Sex': 'false',
            'Email': 'aa@qq.com',
            'Birthday': '2019/11/04',
            'IdNumber': 'a123456',
            'QQAccount': 'a123456'
        }
        response_data = self.agentDetail.updateAgentInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_17(self):
        """驗證 代理商詳細資料 - 取得所有銀行"""
        response_data = self.agentDetail.getAllBanks()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_18(self):
        """驗證 代理商詳細資料 - 取得修改銀行基本資料頁面"""
        response_data = self.agentDetail.modifyBankAccount()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_19(self):
        """驗證 代理商詳細資料 - 更新銀行基本資料"""
        allBank = self.agentDetail.getAllBanks()
        print(allBank)
        bank_Count = len(allBank[1])
        bank_Id = random.randint(1, bank_Count)
        data = {
            'agentAccount': master_config.exist_agent,
            'GroupBankId': bank_Id,
            'Province': 'abc',
            'City': 'efg',
            'Account': '456546',
            'Memo': common_config.now + '@auto_test'
        }
        response_data = self.agentDetail.updateBankAccount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_20(self):
        """驗證 代理商詳細資料 - 銀行修改紀錄"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'id': account_Id[1]['Agent']['Id']}
        response_data = self.agentDetail.getBankHistories(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_21(self):
        """驗證 代理商詳細資料 - 更新備註"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'id': account_Id[1]['Agent']['Id'], 'memo': common_config.now + '@auto_test'}
        response_data = self.agentDetail.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_22(self):
        """驗證 代理商詳細資料 - 重設密碼"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'id': account_Id[1]['Agent']['Id']}
        response_data = self.agentDetail.resetPassword(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_23(self):
        """驗證 代理商詳細資料 - 代理商歷史紀錄頁面"""
        response_data = self.agentDetail.history()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_24(self):
        """驗證 代理商詳細資料 - 歷史紀錄資訊"""
        data = {'account': master_config.exist_agent}
        response_data = self.agentDetail.historyInit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_25(self):
        """驗證 代理商詳細資料 - 讀取歷史紀錄"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {
            'id': account_Id[1]['Agent']['Id'],
            'take': 100,
            'skip': 0,
            'query': {}
        }
        response_data = self.agentDetail.loadHistory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_26(self):
        """驗證 代理商詳細資料 - 取得不存在代理商"""
        data = {'account': master_config.no_exist_agent}
        response_data = self.agentDetail.get_detail(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '找不到此代理商')

    def test_AgentDetail_baseApi_status_27(self):
        """驗證 代理商詳細資料 - 超過10個自訂代理鏈接是否可以新增"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {
            "agentId": account_Id[1]['Agent']['Id'],
            "links": [
                {"Sort": 1, "Url": "aaaaa"},
                {"Sort": 2, "Url": "aaaaa"},
                {"Sort": 3, "Url": "ccccc"},
                {"Sort": 4, "Url": "vvvvvv"},
                {"Sort": 5, "Url": "dddddd"},
                {"Sort": 6, "Url": "xxxxxxxxxxxx"},
                {"Sort": 7, "Url": "vvvedfvfvdev"},
                {"Sort": 8, "Url": "sdvsvdsvs"},
                {"Sort": 9, "Url": "sdvsdvsdvsdvsv"},
                {"Sort": 10, "Url": "dhawrthqthwth"},
                {"Sort": 11, "Url": "dhffffawrthqthwth"}]
        }
        response_data = self.agentDetail.updateCustomizedAgentLinks(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '最多只可设定10个链结')

    def test_AgentDetail_baseApi_status_28(self):
        """驗證 代理商詳細資料 - 已停用推廣鏈接是否再次停用"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        dataLinkStatus = {'id': account_Id[1]['Agent']['Id'], 'status': 'false'}
        self.agentDetail.updateAgentLinkStatus(dataLinkStatus)  # 停用推廣鏈接狀態
        dataDisable = {'id': account_Id[1]['Agent']['Id']}
        self.agentDetail.disable(dataDisable)  # 停用代理商狀態
        response_data = self.agentDetail.updateAgentLinkStatus(dataLinkStatus)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '此代理链接已经是停用状态')

    def test_AgentDetail_baseApi_status_29(self):
        """驗證 代理商詳細資料 - 佣金為不存在時是否更新成功"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'agentId': account_Id[1]['Agent']['Id'], 'commissionSettingId': '-1'}
        response_data = self.agentDetail.updateCommissionSetting(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, 'CommissionSetting.Id=-1 不存在或已删除')

    def test_AgentDetail_baseApi_status_30(self):
        """驗證 代理商詳細資料 - 會員等級為不存在時是否更新成功"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'agentId': account_Id[1]['Agent']['Id'], 'memberLevelSettingId': '-1'}
        response_data = self.agentDetail.updateDefaultMemberLevelSetting(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '找不到此会员等级')

    def test_AgentDetail_baseApi_status_31(self):
        """驗證 代理商詳細資料 - 返水等級為不存在時是否更新成功"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {'agentId': account_Id[1]['Agent']['Id'], 'discountSettingId': '-1'}
        response_data = self.agentDetail.updateDefaultDiscountSetting(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '找不到此返水设定')

    def test_AgentDetail_baseApi_status_32(self):
        """驗證 代理商詳細資料 - 更新代理商基本資料-手機為空"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {
            'Id': account_Id[1]['Agent']['Id'],
            'Name': 'QA_Test' + common_config.now,
            'Mobile': '',
            'Sex': 'false',
            'Email': 'aa@qq.com',
            'Birthday': '2019/11/04',
            'IdNumber': 'a123456',
            'QQAccount': 'a123456'
        }
        response_data = self.agentDetail.updateAgentInfo(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '手机不得为空值')

    def test_AgentDetail_baseApi_status_33(self):
        """驗證 代理商詳細資料 - 更新代理商基本資料-手機有數字以外的字元"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {
            'Id': account_Id[1]['Agent']['Id'],
            'Name': 'QA_Test' + common_config.now,
            'Mobile': '123456@',
            'Sex': 'false',
            'Email': 'aa@qq.com',
            'Birthday': '2019/11/04',
            'IdNumber': 'a123456',
            'QQAccount': 'a123456'
        }
        response_data = self.agentDetail.updateAgentInfo(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '手机只能为数字')

    def test_AgentDetail_baseApi_status_34(self):
        """驗證 代理商詳細資料 - 更新代理商基本資料-真實姓名為空"""
        account = {'account': master_config.exist_agent}
        account_Id = self.agentDetail.get_detail(account)
        data = {
            'Id': account_Id[1]['Agent']['Id'],
            'Name': '',
            'Mobile': '1234567',
            'Sex': 'false',
            'Email': 'aa@qq.com',
            'Birthday': '2019/11/04',
            'IdNumber': 'a123456',
            'QQAccount': 'a123456'
        }
        response_data = self.agentDetail.updateAgentInfo(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '姓名不得为空值')


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
