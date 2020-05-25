'''
@Created by loka
@Date : 2019/12/19
'''

import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import system_management
from master_api.account_login import User


class PortalSettingBaseTest(unittest.TestCase):
    """ 會員端設定 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.PortalSetting = system_management.PortalSetting(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getPortalSettingId(self):
        # 取得設定Id
        response_data = self.PortalSetting.getList({})
        length = len(response_data[1]) - 1  # 取最新的新增最後一筆Id
        getPortalSettingId = response_data[1][length]['Id']
        return getPortalSettingId

    def test_PortalSetting_relatedApi_status_01(self):
        """驗證 會員端管理 - 取得列表頁面"""
        response_data = self.PortalSetting.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_02(self):
        """驗證 會員端管理 - 取得列表"""
        response_data = self.PortalSetting.getList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_03(self):
        """驗證 會員端管理 - 新增頁面"""
        response_data = self.PortalSetting.create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_04(self):
        """驗證 會員端管理 - 新增"""
        data = {'CompanyDepositEnabled': 'true', 'WithdrawEnabled': 'true', 'WalletDepositEnabled': 'true',
                'WalletWithdrawEnabled': 'true', 'WalletRemittancePortalEnabled': 'true', 'IsYuebaoEnabled': 'true',
                'IsShow_MoneyPassword': 'true', 'IsRequired_MoneyPassword': 'true', 'Name': 'QAautomation'}
        response_data = self.PortalSetting.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_05(self):
        """驗證 會員端管理 - 詳細資料頁面"""
        response_data = self.PortalSetting.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_06(self):
        """驗證 會員端管理 - 詳細資料"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId}
        response_data = self.PortalSetting.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_07(self):
        """驗證 會員端管理 - 更新餘額寶顯示開關"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId, 'status': 'false'}  # 關閉
        response_data = self.PortalSetting.updateIsYuebaoToggle(data)
        status_code = response_data[0]
        data = {'id': settingId, 'status': 'true'}  # 開啟
        self.PortalSetting.updateIsYuebaoToggle(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_08(self):
        """驗證 會員端管理 - 更新取款申請顯示開關"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId, 'status': 'false'}  # 關閉
        response_data = self.PortalSetting.updateWithdrawToggle(data)
        status_code = response_data[0]
        data = {'id': settingId, 'status': 'true'}  # 開啟
        self.PortalSetting.updateWithdrawToggle(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_09(self):
        """驗證 會員端管理 - 更新公司入款顯示開關"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId, 'status': 'false'}
        response_data = self.PortalSetting.updateCompanyDepositToggle(data)
        status_code = response_data[0]
        data = {'id': settingId, 'status': 'true'}  # 開啟
        self.PortalSetting.updateCompanyDepositToggle(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_10(self):
        """驗證 會員端管理 - 更新會員端設定名稱"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId, 'args': 'QA' + common_config.now}
        response_data = self.PortalSetting.updateName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_11(self):
        """驗證 會員端管理 - 更新取款提示訊息"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId, 'args': 'QA'}
        response_data = self.PortalSetting.updateWithdrawMessage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_12(self):
        """驗證 會員端管理 - 更新會員註冊設定"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {"id": settingId,
                "args": {'IsShow_Name': 'true', 'IsRequired_Name': 'true', "IsCheckDuplicated_Name": 'false',
                         'IsShow_Mobile': 'true', 'IsRequired_Mobile': 'true',
                         "IsCheckDuplicated_Mobile": 'false',
                         'IsShow_Email': 'true', 'IsRequired_Email': 'false',
                         "IsCheckDuplicated_Email": 'false',
                         'IsShow_Sex': 'true', 'IsRequired_Sex': 'false', 'IsShow_Birthday': 'true',
                         'IsRequired_Birthday': 'false', 'IsShow_IdNumber': 'false',
                         "IsRequired_IdNumber": 'false',
                         'IsCheckDuplicated_IdNumber': 'false', 'IsShow_QQ': 'true', 'IsRequired_QQ': 'false',
                         'IsCheckDuplicated_QQ': 'false', 'IsShow_Referrer': 'true',
                         'IsRequired_Referrer': 'false',
                         'IsShow_MoneyPassword': 'true', 'IsRequired_MoneyPassword': 'true',
                         'IsShow_BankInfo': 'true', 'IsRequired_BankInfo': 'false'}}
        response_data = self.PortalSetting.updateRegisterSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_13(self):
        """驗證 會員端管理 - 更新代理商註冊設定"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {"id": settingId,
                "args": {'IsShow_AgentName': 'true',
                         'IsRequired_AgentName': 'false',
                         'IsCheckDuplicated_AgentName': 'false',
                         'IsShow_AgentMobile': 'true',
                         'IsRequired_AgentMobile': 'false',
                         'IsCheckDuplicated_AgentMobile': 'false',
                         'IsShow_AgentEmail': 'true',
                         'IsRequired_AgentEmail': 'false',
                         "IsCheckDuplicated_AgentEmail": 'false',
                         "IsShow_AgentSex": 'true',
                         "IsRequired_AgentSex": 'false', "IsShow_AgentBirthday": 'true',
                         "IsRequired_AgentBirthday": 'false',
                         "IsShow_AgentIdNumber": 'false', "IsRequired_AgentIdNumber": 'false',
                         "IsCheckDuplicated_AgentIdNumber": 'false', "IsShow_AgentQQ": 'false',
                         "IsRequired_AgentQQ": 'false',
                         "IsCheckDuplicated_AgentQQ": 'false', "IsShow_AgentBankInfo": 'false',
                         "IsRequired_AgentBankInfo": 'false', "IsCheckDuplicated_AgentBankInfo": 'false'}
                }
        response_data = self.PortalSetting.updateAgentRegisterSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_14(self):
        """驗證 會員端管理 - 更新備註"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId,
                'args': 'QA'}
        response_data = self.PortalSetting.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_PortalSetting_relatedApi_status_15(self):
        """驗證 會員端管理 - 刪除"""
        # step1 取得會員端設定Id
        settingId = self.getPortalSettingId()
        data = {'id': settingId}
        response_data = self.PortalSetting.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
