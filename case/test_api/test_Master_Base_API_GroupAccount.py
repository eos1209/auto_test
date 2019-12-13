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

    def get_new_group_account_id(self, bankName):
        response_data = self.groupAccount.getList()
        for i in range(len(response_data[1]['Accounts'])):
            if response_data[1]['Accounts'][i]['PersonName'] == bankName:
                get_id = response_data[1]['Accounts'][i]['Id']
                return get_id
                break

    def get_QRcode_Url(self):
        # 取得商戶的上傳URL
        upload_file = common_config.file_Path + 'test_data/groupAccount.png'  # 檔案
        mime_Type = 'image/jpeg'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'qrCodeFile': ('groupAccount.png', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.groupAccount.updateImage(data)
        open_file.close()  # 關閉
        return response_data[1]['QrCodeUrl']

    def test_GroupAccount_relatedApi_status_01(self):
        """驗證 公司入款帐户管理 - 取得頁面"""
        response_data = self.groupAccount.list()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_02(self):
        """驗證 公司入款帐户管理 - 取得公司入款帳戶列表"""
        response_data = self.groupAccount.getList()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_03(self):
        """驗證 公司入款帐户管理 - 取得所有公司入款帳戶類型"""
        response_data = self.groupAccount.getAllGroupAccountType()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_04(self):
        """驗證 公司入款帐户管理 - 取得新增頁面"""
        response_data = self.groupAccount.create()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_05(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(微信支付)"""
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': 'WeChat',
            'PersonName': '@QA_automation-wechat',
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_06(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(微信支付)是否存在"""
        PersonName = '@QA_automation-wechat'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_07(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(微信支付)"""
        PersonName = '@QA_automation-wechat'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_08(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(支付寶)"""
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': 'Alipay',
            'PersonName': '@QA_automation-Alipay',
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_09(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(支付寶)是否存在"""
        PersonName = '@QA_automation-Alipay'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_10(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(支付寶)"""
        PersonName = '@QA_automation-Alipay'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_11(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(財付通)"""
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': 'Tenpay',
            'PersonName': '@QA_automation-Tenpay',
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_12(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(財付通)是否存在"""
        PersonName = '@QA_automation-Tenpay'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_13(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(財付通)"""
        PersonName = '@QA_automation-Tenpay'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_14(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(QQ掃碼)"""
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': 'QQWallet',
            'PersonName': '@QA_automation-QQWallet',
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_15(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(QQ掃碼)是否存在"""
        PersonName = '@QA_automation-QQWallet'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_16(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(QQ掃碼)"""
        PersonName = '@QA_automation-QQWallet'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_17(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(東京)"""
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': 'JD',
            'PersonName': '@QA_automation-JD',
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_18(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(東京)是否存在"""
        PersonName = '@QA_automation-JD'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_19(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(東京)"""
        PersonName = '@QA_automation-JD'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_20(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(銀聯)"""
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': 'UnionPay',
            'PersonName': '@QA_automation-UnionPay',
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_21(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(銀聯)是否存在"""
        PersonName = '@QA_automation-UnionPay'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_22(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(銀聯)"""
        PersonName = '@QA_automation-UnionPay'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_23(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(百度)"""
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': 'BaiduWallet',
            'PersonName': '@QA_automation-BaiduWallet',
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_24(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(百度)是否存在"""
        PersonName = '@QA_automation-BaiduWallet'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_25(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(百度)"""
        PersonName = '@QA_automation-BaiduWallet'
        getId = self.get_new_group_account_id(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_26(self):
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

    def test_GroupAccount_relatedApi_status_27(self):
        """驗證 公司入款帐户管理 - 廣播更新"""
        get_Id = self.get_new_group_account_id('API - 銀行')
        data = {"id": get_Id}
        response_data = self.groupAccount.broadcastSumInfoUpdated(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_28(self):
        """驗證 公司入款帐户管理 - 確認 CDN 上 QRCode 圖片"""
        data = {}
        response_data = self.groupAccount.confirmAllCdnQrCodeImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_29(self):
        """驗證 公司入款帐户管理 - 停用公司入款帳戶"""
        getId = self.get_new_group_account_id('API - 測試')
        data = {"id": getId}
        response_data = self.groupAccount.disable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_30(self):
        """驗證 公司入款帐户管理 - 啟用公司入款帳戶"""
        getId = self.get_new_group_account_id('API - 銀行')
        data = {"id": getId}
        response_data = self.groupAccount.active(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_31(self):
        """驗證 公司入款帐户管理 - 取得詳細頁面"""
        response_data = self.groupAccount.detail()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_32(self):
        """驗證 公司入款帐户管理 - 取得公司入款帳戶詳細資料"""
        getId = self.get_new_group_account_id('API - 銀行')
        data = {"id": getId}
        response_data = self.groupAccount.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_33(self):
        """驗證 公司入款帐户管理 - 取得修改頁面"""
        response_data = self.groupAccount.modify()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_34(self):
        """驗證 公司入款帐户管理 - 變更目前累積(調整)(歸零)"""
        get_new_create_group_account_id = self.get_new_group_account_id('API - 銀行')
        data = {"Id": get_new_create_group_account_id,
                "targetNumber": 10}
        response_data = self.groupAccount.adjustSum(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_35(self):
        """驗證 公司入款帐户管理 - 更新有效分鐘數"""
        get_new_create_group_account_id = self.get_new_group_account_id('API - 銀行')
        data = {"Id": get_new_create_group_account_id,
                "args": 10}
        response_data = self.groupAccount.updateAvailableMinutes(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_36(self):
        """驗證 公司入款帐户管理 - 修改公司入款帳戶詳細資料"""
        get_new_create_group_account_id = self.get_new_group_account_id('API - 銀行')
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

    def test_GroupAccount_relatedApi_status_37(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶詳細資料"""
        get_new_create_group_account_id = self.get_new_group_account_id('API - 銀行-modify')
        data = {"id": get_new_create_group_account_id}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_38(self):
        """驗證 公司入款帐户管理 - 更新圖片"""
        upload_file = common_config.file_Path + 'test_data/groupAccount_api.png'  # 檔案
        mime_Type = 'image/jpeg'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'qrCodeFile': ('groupAccount_api.png', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.groupAccount.updateImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
