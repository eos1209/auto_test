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
from base.CommonMethod import UploadFile


class GroupAccountBaseTest(unittest.TestCase):
    """ 公司入款帐户 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.groupAccount = system_management.GroupAccount(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def GetNewGroupAccountId(self, PersonName):
        response_data = self.groupAccount.getList({})
        for i in range(len(response_data[1]['Accounts'])):
            if response_data[1]['Accounts'][i]['PersonName'] == PersonName:
                get_id = response_data[1]['Accounts'][i]['Id']
                return get_id

    def get_QRcode_Url(self):
        # 取得商戶的上傳URL
        self.upload = UploadFile('image/png/groupAccount.png',  # 檔案路徑
                                 'qrCodeFile',  # 上傳欄位
                                 'groupAccount.png'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.groupAccount.updateImage(data)
        self.upload.Close_file()
        return response_data[1]['QrCodeUrl']

    def create_groupAccount(self, account_type):
        # 其他方式建立商戶
        QRCodeUrl = self.get_QRcode_Url()
        data = {
            'Type': account_type,
            'PersonName': '@QA_automation-' + account_type,
            'QRCodeUrlFile': {'$ngfBlobUrl': 'blob:http://master.fnjtd.com/' + self.user.info()},
            'Memo': '@QA_automation',
            'AvailableMinutes': 1,
            'MemberLevelSettingIds': [21],
            'QRCodeUrl': QRCodeUrl}
        return data

    def test_GroupAccount_relatedApi_status_01(self):
        """驗證 公司入款帐户管理 - 取得頁面"""
        response_data = self.groupAccount.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_02(self):
        """驗證 公司入款帐户管理 - 取得公司入款帳戶列表"""
        response_data = self.groupAccount.getList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_03(self):
        """驗證 公司入款帐户管理 - 取得所有公司入款帳戶類型"""
        response_data = self.groupAccount.getAllGroupAccountType({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_04(self):
        """驗證 公司入款帐户管理 - 取得新增頁面"""
        response_data = self.groupAccount.create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_05(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(微信支付)"""
        data = self.create_groupAccount('wechat')
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_06(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(微信支付)是否存在"""
        PersonName = '@QA_automation-wechat'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_07(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(微信支付)"""
        PersonName = '@QA_automation-wechat'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_08(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(支付寶)"""
        data = self.create_groupAccount('Alipay')
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_09(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(支付寶)是否存在"""
        PersonName = '@QA_automation-Alipay'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_10(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(支付寶)"""
        PersonName = '@QA_automation-Alipay'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_11(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(財付通)"""
        data = self.create_groupAccount('Tenpay')
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_12(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(財付通)是否存在"""
        PersonName = '@QA_automation-Tenpay'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_13(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(財付通)"""
        PersonName = '@QA_automation-Tenpay'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_14(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(QQ掃碼)"""
        data = self.create_groupAccount('QQWallet')
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_15(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(QQ掃碼)是否存在"""
        PersonName = '@QA_automation-QQWallet'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_16(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(QQ掃碼)"""
        PersonName = '@QA_automation-QQWallet'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_17(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(東京)"""
        data = self.create_groupAccount('JD')
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_18(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(東京)是否存在"""
        PersonName = '@QA_automation-JD'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_19(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(東京)"""
        PersonName = '@QA_automation-JD'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_20(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(銀聯)"""
        data = self.create_groupAccount('UnionPay')
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_21(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(銀聯)是否存在"""
        PersonName = '@QA_automation-UnionPay'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_22(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(銀聯)"""
        PersonName = '@QA_automation-UnionPay'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_23(self):
        """驗證 公司入款帐户管理 - 新增公司入款帳戶(百度)"""
        data = self.create_groupAccount('BaiduWallet')
        response_data = self.groupAccount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_24(self):
        """驗證 公司入款帐户管理 - 公司入款帳戶(百度)是否存在"""
        PersonName = '@QA_automation-BaiduWallet'
        getId = self.GetNewGroupAccountId(PersonName)
        data = {"id": getId}
        Name = self.groupAccount.getDetail(data)
        self.assertEqual(Name[1]['Detail']['PersonName'], PersonName)

    def test_GroupAccount_relatedApi_status_25(self):
        """驗證 公司入款帐户管理 - 刪除公司入款帳戶(百度)"""
        PersonName = '@QA_automation-BaiduWallet'
        getId = self.GetNewGroupAccountId(PersonName)
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
        getId = self.GetNewGroupAccountId('API - 測試')
        data = {"id": getId}
        response_data = self.groupAccount.broadcastSumInfoUpdated(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_28(self):
        """驗證 公司入款帐户管理 - 確認 CDN 上 QRCode 圖片"""
        response_data = self.groupAccount.confirmAllCdnQrCodeImage({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_29(self):
        """驗證 公司入款帐户管理 - 停用公司入款帳戶"""
        getId = self.GetNewGroupAccountId('API - 測試')
        data = {"id": getId}
        response_data = self.groupAccount.disable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_30(self):
        """驗證 公司入款帐户管理 - 啟用公司入款帳戶"""
        getId = self.GetNewGroupAccountId('API - 測試')
        data = {"id": getId}
        response_data = self.groupAccount.active(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_31(self):
        """驗證 公司入款帐户管理 - 取得詳細頁面"""
        response_data = self.groupAccount.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_32(self):
        """驗證 公司入款帐户管理 - 取得公司入款帳戶詳細資料"""
        getId = self.GetNewGroupAccountId('API - 測試')
        data = {"id": getId}
        response_data = self.groupAccount.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_33(self):
        """驗證 公司入款帐户管理 - 取得修改頁面"""
        response_data = self.groupAccount.modify({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_34(self):
        """驗證 公司入款帐户管理 - 變更目前累積(調整)(歸零)"""
        getNewCreateGroupAccountId = self.GetNewGroupAccountId('API - 測試')
        data = {"Id": getNewCreateGroupAccountId,
                "targetNumber": 10}
        response_data = self.groupAccount.adjustSum(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_35(self):
        """驗證 公司入款帐户管理 - 更新有效分鐘數"""
        getNewCreateGroupAccountId = self.GetNewGroupAccountId('API - 測試')
        data = {"Id": getNewCreateGroupAccountId,
                "args": 10}
        response_data = self.groupAccount.updateAvailableMinutes(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_36(self):
        """驗證 公司入款帐户管理 - 修改公司入款帳戶詳細資料"""
        getNewCreateGroupAccountId = self.GetNewGroupAccountId('API - 測試')
        data = {"Id": getNewCreateGroupAccountId,
                "BankName": "API - 銀行-modify",
                "PersonName": "API - 測試 -modify",
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
        getNewCreateGroupAccountId = self.GetNewGroupAccountId('API - 測試 -modify')
        data = {"id": getNewCreateGroupAccountId}
        response_data = self.groupAccount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GroupAccount_relatedApi_status_38(self):
        """驗證 公司入款帐户管理 - 更新圖片"""
        self.upload = UploadFile('image/png/groupAccount_api.png',  # 檔案路徑
                                 'qrCodeFile',  # 上傳欄位
                                 'groupAccount_api.png'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.groupAccount.updateImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
