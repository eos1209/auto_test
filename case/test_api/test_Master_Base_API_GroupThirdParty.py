'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import system_management
from master_api.account_login import User


class GroupThirdPartyBaseTest(unittest.TestCase):
    """ 线上支付商户管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.groupThirdParty = system_management.GroupThirdParty(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def GetGroupThirdPartyId(self):
        response_data = self.groupThirdParty.get_list({})
        for i in range(len(response_data[1]['Settings'])):
            if response_data[1]['Settings'][i]['Name'] == "QA - 測試API":
                self.getNewCreateGroupThirdPartyId = response_data[1]['Settings'][i]['Id']
            elif response_data[1]['Settings'][i]['Name'] == "QA - 測試API-modify":
                self.getNewCreateGroupThirdPartyId = response_data[1]['Settings'][i]['Id']
        return self.getNewCreateGroupThirdPartyId

    def test_GroupAccount_relatedApi_status_01(self):
        """驗證 线上支付商户管理 - 取得列表頁面"""
        response_data = self.groupThirdParty.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_02(self):
        """驗證 线上支付商户管理 - 取得線上支付商戶列表"""
        response_data = self.groupThirdParty.get_list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_03(self):
        """驗證 线上支付商户管理 - 取得新增頁面"""
        response_data = self.groupThirdParty.create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_04(self):
        """驗證 线上支付商户管理 - 取得線上商戶類型"""
        response_data = self.groupThirdParty.get_types({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_05(self):
        """驗證 线上支付商户管理 - 取得目前支付種類"""
        response_data = self.groupThirdParty.get_third_party_type_list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_06(self):
        """驗證 线上支付商户管理 - 新增金流公司商戶資料"""
        data = {"AvailableMinutes": 20,
                "Name": "QA - 測試API",
                "Type": "12355",
                "TypeValue": 4,
                "Min": 1,
                "Max": 10,
                "Limit": 20,
                "RecommendationMemo": "測試",
                "Memo": "微信測試",
                "RecommendationAmountSettings": [{
                    "Sort": 1,
                    "Amount": 5
                },
                    {
                        "Sort": 2,
                        "Amount": 10
                    }],
                "MemberLevelSettingIds": [21],
                "Settings": [{
                    "key": "Account",
                    "value": "201908024"
                },
                    {
                        "key": "Password",
                        "value": "GFHGFDGFHDFGHGF"
                    },
                    {
                        "key": "Gateway",
                        "value": "http://www.baidu.com/"
                    }]}
        response_data = self.groupThirdParty.create_dtpp_submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_07(self):
        """驗證 线上支付商户管理 - 取得金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的詳細資料
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.get_dtpp_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_08(self):
        """驗證 线上支付商户管理 - 停用金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的停用
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dtpp_disable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_09(self):
        """驗證 线上支付商户管理 - 啟用金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的啟用
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dtpp_active(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_10(self):
        """驗證 线上支付商户管理 - 歸零目前商戶累計金額"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的累計金額
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dtpp_reset(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_11(self):
        """驗證 线上支付商户管理 - 更新商戶名稱"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的更新資料
        data = {"id": groupThirdPartyId,
                "args": "QA - 測試API-modify"}
        response_data = self.groupThirdParty.update_dtpp_name(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_25(self):
        """驗證 线上支付商户管理 - 刪除金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的刪除
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dTPPDelete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
