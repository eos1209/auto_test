'''
@Created by loka
@Date : 2019/12/23
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import system_management
from master_api.account_login import User


class CommissionSettingBaseTest(unittest.TestCase):
    """ 佣金設定 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.CommissionSetting = system_management.CommissionSetting(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        # 取得ID
        getId = 0
        response_data = self.CommissionSetting.getList({})
        print("QA_automation" + common_config.now)
        length = len(response_data[1]['CommissionSettings'])
        for i in range(length):
            if response_data[1]['CommissionSettings'][i]['Name'] == "QA_automation" + common_config.now:
                getId = response_data[1]['CommissionSettings'][i]['Id']
                return getId

    def getDeleteId(self):
        # 取得ID
        getId = 0
        response_data = self.CommissionSetting.getList({})
        length = len(response_data[1]['CommissionSettings'])
        for i in range(length):
            if response_data[1]['CommissionSettings'][i]['Name'] == 'QA_automation_Modify' + common_config.now:
                getId = response_data[1]['CommissionSettings'][i]['Id']
                return getId

    def test_CommissionSetting_relatedApi_status_01(self):
        """驗證 佣金設定 - 取得列表頁面"""
        response_data = self.CommissionSetting.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_02(self):
        """驗證 佣金設定 - 取得列表"""
        response_data = self.CommissionSetting.getList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_03(self):
        """驗證 佣金設定 - 新增傭金等級頁面"""
        response_data = self.CommissionSetting.create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_04(self):
        """驗證 佣金設定 - 新增傭金等級"""
        data = {
            "commissionSetting": {
                "Name": "QA_automation" + common_config.now,
                "MinWager": 1,
                "DepositPercent": 1,
                "DepositMax": 1,
                "WithdrawPercent": 1,
                "WithdrawMax": 1,
                "DepositThreshold": 1
            }
        }
        # print("QA_automation" + common_config.now)
        response_data = self.CommissionSetting.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_05(self):
        """驗證 佣金設定 - 傭金等級詳細資料頁面"""
        response_data = self.CommissionSetting.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_06(self):
        """驗證 佣金設定 - 傭金等級詳細資料"""
        # Step 1 取得ID
        getId = self.getId()
        data = {"id": getId}
        response_data = self.CommissionSetting.getDetail(data)
        print(response_data[1])
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_07(self):
        """驗證 佣金設定 - 更新佣金設定狀態"""
        # Step 1 取得ID
        getId = self.getId()
        data = {"id": getId}
        response_data = self.CommissionSetting.changeState(data)
        # print(response_data[1])
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.CommissionSetting.changeState(data)

    def test_CommissionSetting_relatedApi_status_08(self):
        """驗證 佣金設定 - 修改傭金設定頁面"""
        response_data = self.CommissionSetting.modify({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_09(self):
        """驗證 佣金設定 - 更新佣金設定"""
        # Step 1 取得ID
        getId = self.getId()
        data = {"commissionSetting": {"Id": getId, "Name": 'QA_automation_Modify' + common_config.now,
                                      "IsDisabled": 'false',
                                      "MinWager": 1,
                                      "DepositThreshold": 1, "DepositPercent": 1, "DepositMax": 1, "WithdrawPercent": 2,
                                      "WithdrawMax": 1, "SettingDetails": [], "AgentCount": 0}}
        response_data = self.CommissionSetting.update(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CommissionSetting_relatedApi_status_10(self):
        """驗證 佣金設定 - 刪除佣金設定"""
        # Step 1 取得ID
        getId = self.getDeleteId()
        data = {"id": getId}
        response_data = self.CommissionSetting.delete(data)
        # print(response_data[1])
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
