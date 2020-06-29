'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import system_management
from master_api.account_login import User


class MemberLevelSettingBaseTest(unittest.TestCase):
    """会员等级管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberLevelSetting = system_management.MemberLevelSetting(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    '''
    @方法：取得會員等級的最後一筆 id
    '''

    def GetMemberLevelSettingId(self):
        getData = self.memberLevelSetting.getList({})
        dataLength = len(getData[1]['Levels']) - 1  # 取得最後一筆資料
        getMemberLevelSettingId = getData[1]['Levels'][dataLength]['Id']
        return getMemberLevelSettingId

    def test_Member_Level_Setting_relatedApi_status_01(self):
        """驗證 会员等级管理 - 取得頁面"""
        response_data = self.memberLevelSetting.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_02(self):
        """驗證 会员等级管理 - 取得列表清單"""
        response_data = self.memberLevelSetting.getList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_03(self):
        """驗證 会员等级管理 - 取得各等級的會員數"""
        response_data = self.memberLevelSetting.getMemberCount({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_05(self):
        """驗證 会员等级管理 - 新增等級頁面"""
        response_data = self.memberLevelSetting.create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_06(self):
        """驗證 会员等级管理 - 新增等級"""
        data = {"Name": "API測試Level", "GroupDepositMin": 1, "GroupDepositMax": 100, "AlipayWithdrawMin": 1,
                "AlipayWithdrawMax": 100, "WithdrawMin": 1, "WithdrawMax": 100, "Fee": 1, "FeeType": "Discount",
                "FreeFeeHours": 1, "FreeFeeTimes": 1, "Memo": "1",
                "MemberLevelSettingGroupAccountDiscounts": [{"Amount": 1, "Percent": 1, "AuditTimes": 1, "Max": 1}],
                "MemberLevelSettingThirdPartyPaymentDiscounts": [
                    {"Id": 0, "Name": "预设", "Sort": -1, "isSelected": 'true',
                     "DepositSettings": [
                         {"Amount": 1, "Percent": 1, "AuditTimes": 1,
                          "Max": 1}]}], "DepositAuditPercent_Account": 1,
                "DepositAuditPercent_ThirdPartyPayment": 1, "DepositAuditPercent_PointCard": 1, "FinePercent": 20,
                "RegisterBonus": {"IsEnabled": 'true', "Amount": 1, "AuditAmount": 1, "IsWithMaster": 'true'},
                "PointCardFee": {"IsEnabled": 'true', "Percent": 1, "FeeMax": 1}, "AlipayWithdrawEnable": 'false',
                "ExternalPayment": {"IsEnabled": 'true', "Title": "1", "Description": "1",
                                    "Url": "https://www.youtube.com/?gl=TW&tab=r1"},
                "MemberLevelSettingGpeDepositDiscounts": [{"Amount": 1, "Percent": 1, "AuditTimes": 1, "Max": 1}],
                "WithdrawTypeStates": [{"Id": 1, "Enable": 'true'}, {"Id": 2, "Enable": 'true'},
                                       {"Id": 3, "Enable": 'true'}]}
        response_data = self.memberLevelSetting.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_07(self):
        """驗證 会员等级管理 - 取得設定詳細資料頁面"""
        response_data = self.memberLevelSetting.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_08(self):
        """驗證 会员等级管理 - 取得設定詳細資料"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId}
        response_data = self.memberLevelSetting.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_09(self):
        """驗證 会员等级管理 - 取得修改頁面"""
        response_data = self.memberLevelSetting.modify({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_10(self):
        """驗證 会员等级管理 - 修改等級(更新)"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId,
                "Name": "API測試Level", "GroupDepositMin": 1, "GroupDepositMax": 100, "AlipayWithdrawMin": 1,
                "AlipayWithdrawMax": 100, "WithdrawMin": 1, "WithdrawMax": 100, "Fee": 1, "FeeType": "Discount",
                "FreeFeeHours": 1, "FreeFeeTimes": 1, "Memo": "1",
                "MemberLevelSettingGroupAccountDiscounts": [{"Amount": 1, "Percent": 1, "AuditTimes": 1, "Max": 1}],
                "MemberLevelSettingThirdPartyPaymentDiscounts": [{"Id": 0, "Name": "预设", "DepositSettings": [
                    {"Amount": 1, "Percent": 1, "AuditTimes": 1, "Max": 1}]}], "DepositAuditPercent_Account": 1,
                "DepositAuditPercent_ThirdPartyPayment": 1, "DepositAuditPercent_PointCard": 1, "FinePercent": 20,
                "RegisterBonus": {"IsEnabled": 'true', "IsWithMaster": 'true', "Amount": 1, "AuditAmount": 1},
                "PointCardFee": {"IsEnabled": 'true', "Percent": 1, "FeeMax": 1}, "AlipayWithdrawEnable": 'false',
                "IsAlipayWithdrawDefault": 'false',
                "ExternalPayment": {"Title": "1", "IsEnabled": 'false', "Url": "https://www.youtube.com/?gl=TW&tab=r1",
                                    "Description": "1"},
                "MemberLevelSettingGpeDepositDiscounts": [{"Amount": 1, "Percent": 1, "AuditTimes": 1, "Max": 1}],
                "WithdrawTypeStates": [{"Id": "1", "Enable": 'true'}, {"Id": "2", "Enable": 'true'},
                                       {"Id": "3", "Enable": 'true'}]}
        response_data = self.memberLevelSetting.update(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_11(self):
        """驗證 会员等级管理 - 取得該等級會員數"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId}
        response_data = self.memberLevelSetting.getMemberCount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_12(self):
        """驗證 会员等级管理 - 更改危險等級設定 - 危險等級"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId,
                "isDangerous": True}
        response_data = self.memberLevelSetting.updateIsDangerous(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_13(self):
        """驗證 会员等级管理 - 更改危險等級設定 - 安全等級"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId,
                "isDangerous": False}
        response_data = self.memberLevelSetting.updateIsDangerous(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_14(self):
        """驗證 会员等级管理 - 驗證自動化建立等級是否是- API 測試"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId}
        response_data = self.memberLevelSetting.getDetail(data)
        self.assertEqual(response_data[1]['Detail']['Name'], 'API測試Level')

    def test_Member_Level_Setting_relatedApi_status_15(self):
        """驗證 会员等级管理 - 刪除等級"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId}
        response_data = self.memberLevelSetting.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_16(self):
        """驗證 会员等级管理 - 取得各等級的參加活動數量"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId}
        response_data = self.memberLevelSetting.getEventList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Member_Level_Setting_relatedApi_status_17(self):
        """驗證 会员等级管理 - 取得該等級會員數"""
        # Step1
        memberLevelSettingId = self.GetMemberLevelSettingId()
        # Step2
        data = {"id": memberLevelSettingId}
        response_data = self.memberLevelSetting.getDetailMemberCount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
