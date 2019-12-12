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


class GroupAccountBaseTest(unittest.TestCase):
    """ 公司入款帐户 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.groupAccount = system_management.GroupAccount(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_GroupAccount_relatedApi_status_01(self):
        """驗證 公司入款帐户管理 - 取得頁面"""
        data = {}
        response_data = self.groupAccount.list(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_02(self):
        """驗證 公司入款帐户管理 - 取得公司入款帳戶列表"""
        data = {}
        response_data = self.groupAccount.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_03(self):
        """驗證 公司入款帐户管理 - 取得所有公司入款帳戶類型"""
        data = {}
        response_data = self.groupAccount.getAllGroupAccountType(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_04(self):
        """驗證 公司入款帐户管理 - 取得新增頁面"""
        data = {}
        response_data = self.groupAccount.create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_05(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶"""
        data = {"Type": "General",
                "BankName": "API - 銀行",
                "PersonName": "API - 測試",
                "NetPoint": "吉林省松原市",
                "Account": "12345678987654321",
                "Memo": "新增測試",
                "AvailableMinutes": 20,
                "MemberLevelSettingIds": [21]}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_06(self):
        """驗證 公司入款帐户管理 - 廣播更新"""
        self.get_new_group_account_id()
        data = {"id": self.get_new_create_group_account_id}
        response_data = self.groupAccount.broadcastSumInfoUpdated(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_07(self):
        """驗證 公司入款帐户管理 - 確認 CDN 上 QRCode 圖片"""
        data = {}
        response_data = self.groupAccount.confirmAllCdnQrCodeImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_08(self):
        """驗證 公司入款帐户管理 - 停用公司入款帳戶"""
        self.get_new_group_account_id()
        data = {"id": self.get_new_create_group_account_id}
        response_data = self.groupAccount.disable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_09(self):
        """驗證 公司入款帐户管理 - 啟用公司入款帳戶"""
        self.get_new_group_account_id()
        data = {"id": self.get_new_create_group_account_id}
        response_data = self.groupAccount.active(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_10(self):
        """驗證 公司入款帐户管理 - 取得詳細頁面"""
        data = {}
        response_data = self.groupAccount.detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_11(self):
        """驗證 公司入款帐户管理 - 取得公司入款帳戶詳細資料"""
        self.get_new_group_account_id()
        data = {"id": self.get_new_create_group_account_id}
        response_data = self.groupAccount.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_12(self):
        """驗證 公司入款帐户管理 - 取得修改頁面"""
        data = {}
        response_data = self.groupAccount.modify(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_13(self):
        """驗證 公司入款帐户管理 - 變更目前累積(調整)(歸零)"""
        get_new_create_group_account_id = self.get_new_group_account_id()
        data = {"Id": get_new_create_group_account_id,
                "targetNumber": 10}
        response_data = self.groupAccount.adjustSum(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_14(self):
        """驗證 公司入款帐户管理 - 更新有效分鐘數"""
        get_new_create_group_account_id = self.get_new_group_account_id()
        data = {"Id": get_new_create_group_account_id,
                "args": 10}
        response_data = self.groupAccount.updateAvailableMinutes(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_15(self):
        """驗證 公司入款帐户管理 - 修改公司入款帳戶詳細資料"""
        get_new_create_group_account_id = self.get_new_group_account_id()
        data = {"Id": get_new_create_group_account_id,
                "BankName": "API - 銀行-modify",
                "PersonName": "API - 測試",
                "NetPoint": "吉林省松原市",
                "Account": "12345678987654321",
                "IsDisabled": False,
                "Memo": "新增測試",
                "IsDeleted": False,
                "LevelSettings": [{"Id": 21, "Name": "QA_Test"}],
                "Sum": 0,
                "Type": "General",
                "QRCodeUrl": None, "CdnIsValid": True, "AvailableMinutes": 20,
                "typeSetting": {"Key": "General",
                                "Value": "ENUM_GroupAccountType_General",
                                "PropertyList": [{"Type": 1,
                                                  "PropertyName": "BankName",
                                                  "PropertyLangKey": "GROUPACCOUNT_Bank",
                                                  "InputType": 1,
                                                  "PlaceholderLangKey": "GROUPACCOUNT_BankPlaceHolder", "MaxLength": 50,
                                                  "Required": True,
                                                  "Sort": 1},
                                                 {"Type": 1, "PropertyName": "PersonName",
                                                  "PropertyLangKey": "PAYMENT_Payee", "InputType": 1,
                                                  "PlaceholderLangKey": "GROUPACCOUNT_PayeePlaceHolder",
                                                  "MaxLength": 50, "Required": True,
                                                  "Sort": 2},
                                                 {"Type": 1, "PropertyName": "NetPoint",
                                                  "PropertyLangKey": "GROUPACCOUNT_BankBranch",
                                                  "InputType": 1,
                                                  "PlaceholderLangKey": "GROUPACCOUNT_BankBranchPlaceHolder",
                                                  "MaxLength": 50, "Required": True, "Sort": 3},
                                                 {"Type": 1, "PropertyName": "Account",
                                                  "PropertyLangKey": "GROUPACCOUNT_BankAccount",
                                                  "InputType": 1,
                                                  "PlaceholderLangKey": "GROUPACCOUNT_BankAccountPlaceHolder",
                                                  "MaxLength": 50,
                                                  "Required": True, "Sort": 4},
                                                 {"Type": 1, "PropertyName": "Memo",
                                                  "PropertyLangKey": "MEMBERTRAN_ExportColumeNote",
                                                  "InputType": 2, "PlaceholderLangKey": "", "MaxLength": 50,
                                                  "Required": False, "Sort": 5}],
                                "isSelected": True},
                "MemberLevelSettingIds": [21]}
        response_data = self.groupAccount.updateSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_16(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶詳細資料"""
        get_new_create_group_account_id = self.get_new_group_account_id()
        data = {"id": get_new_create_group_account_id}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_GroupAccount_relatedApi_status_019(self):
    #     """驗證 公司入款帐户管理 - 更新圖片"""
    #     image_file_descriptor = open('C:/Users/admin/Downloads/貼圖/1.png', 'rb')
    #     filtes = {'media': image_file_descriptor}
    #     response_data = self.groupAccount.broadcastSumInfoUpdated(filtes)
    #     image_file_descriptor.close()
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, Config.Status_Code)

    def get_new_group_account_id(self):
        data = {}
        response_data = self.groupAccount.getList(data)
        for i in range(len(response_data[1]['Accounts'])):
            if response_data[1]['Accounts'][i]['BankName'] == "API - 銀行":
                self.get_new_create_group_account_id = response_data[1]['Accounts'][i]['Id']
            elif response_data[1]['Accounts'][i]['BankName'] == "API - 銀行-modify":
                self.get_new_create_group_account_id = response_data[1]['Accounts'][i]['Id']
        return self.get_new_create_group_account_id


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
