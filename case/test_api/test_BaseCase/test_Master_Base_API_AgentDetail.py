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
import random
from data_config import master_config
from data_config.system_config import systemSetting


class AgentDetailTest(unittest.TestCase):
    """代理商詳細資料 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.agentDetail = member_and_agent.AgentDetail(self.__http)
        self.AgentSearch = member_and_agent.AgentSearch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def GetAgentId(self):
        data = {'account': self.config.agentLv4()}
        response_data = self.agentDetail.get_detail(data)
        agentId = response_data[1]['Agent']['Id']
        return agentId

    def getCommissionSettingId(self):
        response_data = self.agentDetail.getAllCommissionSettings({})
        for i in range(len(response_data[1])):
            if self.config.commissionSetting_2_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def getDiscountSettingId(self):
        response_data = self.agentDetail.getAllDiscountSettings({})
        for i in range(len(response_data[1])):
            if self.config.DiscountSetting_2_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def getMemberLevelId(self):
        response_data = self.agentDetail.getAllMemberLevels({})
        for i in range(len(response_data[1])):
            if self.config.MemberLevelSetting_2_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def test_AgentDetail_baseApi_status_01(self):
        """驗證 代理商詳細資料 - 頁面狀態"""
        response_data = self.agentDetail.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_02(self):
        """驗證 代理商詳細資料 - 取得所有返水設定"""
        response_data = self.agentDetail.getAllDiscountSettings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_03(self):
        """驗證 代理商詳細資料 - 取得所有會員等級"""
        response_data = self.agentDetail.getAllMemberLevels({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_04(self):
        """驗證 代理商詳細資料 - 取得所有佣金設定"""
        response_data = self.agentDetail.getAllCommissionSettings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_05(self):
        """驗證 代理商詳細資料 - 取得詳細資料"""
        data = {'account': self.config.agentLv4()}
        response_data = self.agentDetail.get_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_06(self):
        """驗證 代理商詳細資料 - 停用代理商"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2 將測試代理商狀態改為停用
        data = {'id': agentId}
        response_data = self.agentDetail.disable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_07(self):
        """驗證 代理商詳細資料 - 啟用代理商"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()

        # Step2 將測試代理商狀態改為啟用
        data = {'id': agentId}
        response_data = self.agentDetail.active(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_08(self):
        """驗證 代理商詳細資料 - 修改自訂推廣鏈接"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2 呼叫修改 推廣鏈接的 API
        data = {
            "agentId": agentId,
            "links": [{"Sort": 1, "Url": "xxxxx"}]
        }
        response_data = self.agentDetail.updateCustomizedAgentLinks(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_09(self):
        """驗證 代理商詳細資料 - 修改推廣鏈接"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {"id": agentId,
                "agentLink": "http://" + common_config.now}
        response_data = self.agentDetail.updateAgentLink(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_10(self):
        """驗證 代理商詳細資料 - 更新代理推廣鏈接"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'id': agentId,
                'status': 'true'}
        response_data = self.agentDetail.updateAgentLinkStatus(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_11(self):
        """驗證 代理商詳細資料 - 修改更新佣金設定"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'agentId': agentId,
                'commissionSettingId': self.getCommissionSettingId()}
        response_data = self.agentDetail.updateCommissionSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_12(self):
        """驗證 代理商詳細資料 - 更新預設會員等級"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'agentId': agentId,
                'memberLevelSettingId': self.getMemberLevelId()}
        response_data = self.agentDetail.updateDefaultMemberLevelSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_13(self):
        """驗證 代理商詳細資料 - 更新預設返水等級"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'agentId': agentId,
                'discountSettingId': self.getDiscountSettingId()}
        response_data = self.agentDetail.updateDefaultDiscountSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_14(self):
        """驗證 代理商詳細資料 - 檢查更新代理商權限"""
        data = {'account': self.config.agentLv4()}
        response_data = self.agentDetail.checkUpdateAgentAuthority(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_15(self):
        """驗證 代理商詳細資料 - 取得修改代理商基本資料頁面"""
        response_data = self.agentDetail.modifyAgentInfo({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_16(self):
        """驗證 代理商詳細資料 - 更新代理商基本資料"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {
            'Id': agentId,
            'Name': 'QATest',
            'Mobile': '987654312',
            'Sex': 'false',
            'Email': 'aa@qq.com',
            'Birthday': '2019/11/04',
            'IdNumber': 'a1234567',
            'QQAccount': 'QA_Test' + common_config.now
        }
        response_data = self.agentDetail.updateAgentInfo(data)
        status_code = response_data[0]
        data = {'account': self.config.agentLv4()}
        response_data = self.agentDetail.get_detail(data)
        validateData = response_data[1]['Agent']['QQ']  # 驗證資料
        self.assertEqual(bool(status_code == common_config.Status_Code),
                         bool(validateData == 'QA_Test' + common_config.now))

    def test_AgentDetail_baseApi_status_17(self):
        """驗證 代理商詳細資料 - 取得所有銀行"""
        response_data = self.agentDetail.getAllBanks({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_18(self):
        """驗證 代理商詳細資料 - 取得修改銀行基本資料頁面"""
        response_data = self.agentDetail.modifyBankAccount({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_19(self):
        """驗證 代理商詳細資料 - 更新銀行基本資料"""
        # Step1 取得銀行資訊並隨機獲取欲修改的id
        response_data = self.agentDetail.getAllBanks({})
        bank_Count = len(response_data[1]) - 1
        bankId = random.randint(1, bank_Count)
        # Step2 更新銀行基本資料
        data = {
            'agentAccount': self.config.agentLv4(),
            'GroupBankId': bankId,
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
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'id': agentId}
        response_data = self.agentDetail.getBankHistories(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_21(self):
        """驗證 代理商詳細資料 - 更新備註"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'id': agentId,
                'memo': common_config.now + '@auto_test'}
        response_data = self.agentDetail.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_22(self):
        """驗證 代理商詳細資料 - 重設密碼"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'id': agentId}
        response_data = self.agentDetail.resetPassword(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_23(self):
        """驗證 代理商詳細資料 - 代理商歷史紀錄頁面"""
        response_data = self.agentDetail.history({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_24(self):
        """驗證 代理商詳細資料 - 歷史紀錄資訊"""
        data = {'account': self.config.agentLv4()}
        response_data = self.agentDetail.historyInit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentDetail_baseApi_status_25(self):
        """驗證 代理商詳細資料 - 讀取歷史紀錄"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'id': agentId,
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
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {"agentId": agentId,
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
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        dataLinkStatus = {'id': agentId, 'status': 'false'}
        self.agentDetail.updateAgentLinkStatus(dataLinkStatus)  # 停用推廣鏈接狀態
        dataDisable = {'id': agentId}
        self.agentDetail.disable(dataDisable)  # 停用代理商狀態
        # Step2 啟用代理商狀態
        self.agentDetail.active(dataDisable)  # 停用代理商狀態
        response_data = self.agentDetail.updateAgentLinkStatus(dataLinkStatus)
        errorMessage = response_data[1]['ErrorMessage']
        dataLinkStatus = {'id': agentId, 'status': 'true'}
        self.agentDetail.updateAgentLinkStatus(dataLinkStatus)  # 停用推廣鏈接狀態
        self.assertEqual(errorMessage, '此代理链接已经是停用状态')

    def test_AgentDetail_baseApi_status_29(self):
        """驗證 代理商詳細資料 - 佣金為不存在時是否更新成功"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'agentId': agentId,
                'commissionSettingId': '-1'}
        response_data = self.agentDetail.updateCommissionSetting(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, 'CommissionSetting.Id=-1 不存在或已删除')

    def test_AgentDetail_baseApi_status_30(self):
        """驗證 代理商詳細資料 - 會員等級為不存在時是否更新成功"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'agentId': agentId,
                'memberLevelSettingId': '-1'}
        response_data = self.agentDetail.updateDefaultMemberLevelSetting(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '找不到此会员等级')

    def test_AgentDetail_baseApi_status_31(self):
        """驗證 代理商詳細資料 - 返水等級為不存在時是否更新成功"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'agentId': agentId,
                'discountSettingId': '-1'}
        response_data = self.agentDetail.updateDefaultDiscountSetting(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '找不到此返水设定')

    def test_AgentDetail_baseApi_status_32(self):
        """驗證 代理商詳細資料 - 更新代理商基本資料-手機為空"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'Id': agentId,
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
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'Id': agentId,
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
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'Id': agentId,
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

    def test_AgentDetail_baseApi_status_35(self):
        """驗證 代理商詳細資料 - 更新代理商基本資料-真實姓名混入非中英文"""
        # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
        agentId = self.GetAgentId()
        # Step2
        data = {'Id': agentId,
                'Name': 'QA_Test' + common_config.now,
                'Mobile': '1234567',
                'Sex': 'false',
                'Email': 'aa@qq.com',
                'Birthday': '2019/11/04',
                'IdNumber': 'a123456',
                'QQAccount': 'a123456'
                }
        response_data = self.agentDetail.updateAgentInfo(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '姓名只允许中英文，與全、半形英文句號')

    def test_AgentDetail_baseApi_status_36(self):
        """驗證 代理商詳細資料 - 讀取代理資料"""
        data = {'account': self.config.agentLv1()}
        response_data = self.agentDetail.getAgentLayerDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_AgentDetail_baseApi_status_36(self):
    #     """驗證 代理商詳細資料 - 是否可以設定相同的代理鏈接"""
    #     # Step1 取得代理商的 Agent Id(需從詳細資料中取得)
    #     agentId = self.GetAgentId()
    #     # Step2
    #     data = {"id": agentId,
    #             "agentLink": "http://4444"}
    #     response_data = self.agentDetail.updateAgentLink(data)
    #     validateData = response_data[1]['ErrorMessage']
    #     self.assertEqual(validateData, '代理推广链结不可与 QA_Test11070110 相同')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
