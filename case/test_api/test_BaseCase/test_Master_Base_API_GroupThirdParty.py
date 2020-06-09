'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest
from pprint import pprint

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

    def test_GroupThirdParty_relatedApi_status_01(self):
        """驗證 线上支付商户管理 - 取得列表頁面"""
        response_data = self.groupThirdParty.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_02(self):
        """驗證 线上支付商户管理 - 取得線上支付商戶列表"""
        response_data = self.groupThirdParty.get_list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_03(self):
        """驗證 线上支付商户管理 - 取得新增頁面"""
        response_data = self.groupThirdParty.create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_04(self):
        """驗證 线上支付商户管理 - 取得線上商戶類型"""
        response_data = self.groupThirdParty.get_types({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_05(self):
        """驗證 线上支付商户管理 - 取得目前支付種類"""
        response_data = self.groupThirdParty.get_third_party_type_list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_06(self):
        """驗證 线上支付商户管理 - 新增金流公司商戶資料"""
        data = {"AvailableMinutes": 20,
                "Name": "QA - 測試API",
                "Type": "96",
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

    def test_GroupThirdParty_relatedApi_status_07(self):
        """驗證 线上支付商户管理 - 取得金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的詳細資料
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.get_dtpp_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_08(self):
        """驗證 线上支付商户管理 - 停用金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的停用
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dtpp_disable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_09(self):
        """驗證 线上支付商户管理 - 啟用金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的啟用
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dtpp_active(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_10(self):
        """驗證 线上支付商户管理 - 歸零目前商戶累計金額"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的累計金額
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dtpp_reset(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_11(self):
        """驗證 线上支付商户管理 - 更新商戶名稱"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的更新資料
        data = {"id": groupThirdPartyId,
                "args": "QA - 測試API-modify"}
        response_data = self.groupThirdParty.update_dtpp_name(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_12(self):
        """驗證 線上支付商戶管理 - 新增商戶取得支付商戶類型"""
        response_data = self.groupThirdParty.getDTPPTypeList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_13(self):
        """驗證 線上支付商戶管理 - 新增商戶取得支付商戶列表"""
        response_data = self.groupThirdParty.getValidDTPP({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_14(self):
        """驗證 線上支付商戶管理 - 取得商戶詳細設定資料"""
        # Step1 取得 支付金流Id
        response_data = self.groupThirdParty.getValidDTPP({})
        getId = response_data[1]['ReturnObject'][0]['Value']
        data = {"Id": getId}
        response_data = self.groupThirdParty.getSettingDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_15(self):
        """驗證 線上支付商戶管理 - 取得商戶簡體中文限制"""
        # Step1 取得 支付金流Id
        response_data = self.groupThirdParty.getValidDTPP({})
        getId = response_data[1]['ReturnObject'][0]['Value']
        data = {'Id': getId}
        response_data = self.groupThirdParty.getDepositLimitsCn(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_16(self):
        """驗證 線上支付商戶管理 - 更新商戶資料"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 取得 支付金流Id
        response_data = self.groupThirdParty.getValidDTPP({})
        Type = response_data[1]['ReturnObject'][0]['Value']  # 新金流Id
        typeValue = response_data[1]['ReturnObject'][0]['TypeValue']  # 新金流Id
        data = {"id": groupThirdPartyId, "args": {
            "Settings": [{"key": "Account", "value": "11333"},
                         {"key": "Password", "value": "33"},
                         {"key": "Gateway", "value": "http://tw"}],
            "Type": Type, "TypeValue": typeValue}}
        response_data = self.groupThirdParty.updateDTPPMerchantData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_18(self):
        """驗證 線上支付商戶管理 - 更新更新單次存款限額"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        data = {'id': groupThirdPartyId, 'args': {'Min': 1, 'Max': 10}}
        response_data = self.groupThirdParty.updateDTPPRange(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_19(self):
        """驗證 線上支付商戶管理 - 更新推薦說明"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        data = {'id': groupThirdPartyId, 'args': '@QA_automation'}
        response_data = self.groupThirdParty.updateDTPPRecommendationMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_20(self):
        """驗證 線上支付商戶管理 - 更新推薦金額鎖"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        data = {'id': groupThirdPartyId, 'args': 'true'}
        response_data = self.groupThirdParty.updateDTPPAmountLock(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_21(self):
        """驗證 線上支付商戶管理 - 更新推薦金額"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        data = {'id': groupThirdPartyId, 'args': [{'Sort': 1, 'Amount': 10}, {'Sort': 2, 'Amount': 20}]}
        response_data = self.groupThirdParty.updateDTPPRecommendationAmountSettings(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_22(self):
        """驗證 線上支付商戶管理 - 更新總存款額度"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        data = {'id': groupThirdPartyId, 'args': 1}
        response_data = self.groupThirdParty.updateDTPPRecommendationAmountSettings(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_23(self):
        """驗證 線上支付商戶管理 - 更新有效分鐘數"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        data = {'id': groupThirdPartyId, 'args': 4}
        response_data = self.groupThirdParty.updateDTPPAvailableMinutes(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_24(self):
        """驗證 線上支付商戶管理 - 更新備註"""
        # Step1 取得商戶Id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        data = {'id': groupThirdPartyId, 'args': 'QA_automation'}
        response_data = self.groupThirdParty.updateDTPPMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_25(self):
        """驗證 线上支付商户管理 - 自訂商戶開關 - 開&關 狀態"""
        types = ["false", "true"]
        for i in range(len(types)):
            data = {"id": self.GetGroupThirdPartyId(),
                    "isShow": types[i]
                    }
            response_data = self.groupThirdParty.UpdateDTPPIsShowCustomMerchant(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_26(self):
        """驗證 线上支付商户管理 - 前台顯示順序改為 自訂 狀態"""
        data = {"mode": "1"}
        response_data = self.groupThirdParty.SetDtppSortingMode(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_27(self):
        """驗證 线上支付商户管理 - 前台顯示順序改為 隨機 狀態"""
        data = {"mode": "2"}
        response_data = self.groupThirdParty.SetDtppSortingMode(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_28(self):
        """驗證 线上支付商户管理 - 刪除金流公司商戶資料"""
        # Step1 取得欲驗證的金流公司商戶id
        groupThirdPartyId = self.GetGroupThirdPartyId()
        # Step2 驗證呼叫該商戶的刪除
        data = {"id": groupThirdPartyId}
        response_data = self.groupThirdParty.dTPPDelete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupThirdParty_relatedApi_status_29(self):
        """驗證 线上支付商户管理 - 线上支付看板-取得商户使用占比与成功率列表 - 昨日 + 近7日 + 近30日"""
        days = [1, 7, 30]
        for i in range(len(days)):
            data = {
                "date": days.pop(),
                "name": "",
                "take": 100,
                "skip": 0,
                "descType": 1,
                "isDesc": 'false'
            }
            response_data = self.groupThirdParty.GetList(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
