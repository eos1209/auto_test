'''
@Created by loka
@Date : 2020/01/20
'''

import unittest
import random
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement, PayoutMerchantManagement
from master_api.Home import Home
from master_api.account_login import User
from data_config.system_config import systemSetting


class ThirdPartyPayoutBaseTest(unittest.TestCase):
    """ 代付商户管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.home = Home(self.__http)
        self.siteParameter = PayoutMerchantManagement(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    # 登出
    def tearDown(self):
        self.user.logout()

    def getApilist(self):
        """取一筆代付商戶"""
        items = self.siteParameter.GetApiList()
        for i in range(len(items[1]['ReturnObject'])):
            if items[1]['ReturnObject'][i]['Name'] == 'TestPayout':
                Name = items[1]['ReturnObject'][i]['Name']
                Api_id = items[1]['ReturnObject'][i]['ApiId']
                break
            else:
                Name = items[1]['ReturnObject'][i]['Name']
                Api_id = items[1]['ReturnObject'][i]['ApiId']
        return Name, Api_id

    def getPayLists(self):
        response_data = self.siteParameter.GetList()
        for i in range(len(response_data[1]['ReturnObject'])):
            Id = response_data[1]['ReturnObject'][i]['Id']
            Name = response_data[1]['ReturnObject'][i]['Name']
            AvailableMinutes = response_data[1]['ReturnObject'][i]['AvailableMinutes']
        return Id, Name, AvailableMinutes

    def getNewPayLists(self):
        """取自動化新增的那一筆商戶"""
        response_data = self.siteParameter.GetList()
        for i in range(len(response_data[1]['ReturnObject'])):
            if response_data[1]['ReturnObject'][i]['Name'] == "QAtest":
                Id = response_data[1]['ReturnObject'][i]['Id']
                Name = response_data[1]['ReturnObject'][i]['Name']
                AvailableMinutes = response_data[1]['ReturnObject'][i]['AvailableMinutes']
        return Id, Name, AvailableMinutes

    def getDelPayLists(self):
        """取自動化新增的那一筆商戶 - 刪除"""
        response_data = self.siteParameter.GetList()
        for i in range(len(response_data[1]['ReturnObject'])):
            if response_data[1]['ReturnObject'][i]['Name'] == "QAtest1":
                Id = response_data[1]['ReturnObject'][i]['Id']
        return Id

    def getAllMemberLevels(self):
        response_data = self.home.getAllMemberLevels({})
        item = []
        for i in range(len(response_data[1])):
            item.append(response_data[1][i]['Value'])
        return item

    def getAllBanks(self):
        response_data = self.home.getAllBanks()
        item = []
        for i in range(len(response_data[1])):
            item.append(response_data[1][i]['Id'])
        return item

    # @unittest.skip('測試直接跳過測試用')
    def test_ThirdPartyPayout_relatedApi_status_01(self):
        """驗證 代付商户管理 - 取得代付商戶列表 狀態"""
        response_data = self.siteParameter.GetList()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_02(self):
        """驗證 代付商户管理 - 取得代付商戶詳細資料 狀態"""
        data = {"id": self.getPayLists()[0]}
        response_data = self.siteParameter.GetDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_03(self):
        """驗證 代付商户管理 - 取得代付商戶api列表 狀態"""
        response_data = self.siteParameter.GetApiList()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_04(self):
        """驗證 代付商户管理 - 新增代付商戶 狀態"""
        item = self.getApilist()  # 取api代付商戶
        data = {
            "AvailableMinutes": 1,  # 有效分鐘數
            "IsAutoPayout": 'true',  # 自动出款
            "ApiId": item[1],
            "Name": "QAtest",
            "MerchantNo": "xian4",
            "Password": "10C36EFD68E6D4A29A62FB8AAB63A491",
            "Gateway": "http://gpkpay.fnjtd.com",
            "TotalPayoutLimit": 1,  # 总出款限额
            "IsCheckFirstPayoutMember": "false",  # 首次取款會員
            "IsCheckHighRiskMember": "false",  # 高風險
            "IsCheckDangerMember": 'false',
            "PayoutLimitStart": 1,
            "PayoutLimitEnd": 2,
            "Memo": "註解",  # 註解
            "MemberLevelSettings": self.getAllMemberLevels(),  # MemberLevel
            "DispensingBankSettings": self.getAllBanks()  # Bank
        }
        response_data = self.siteParameter.Create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_05(self):
        """驗證 代付商户管理 - 修改代付商戶資料 狀態"""
        IDdata = {"id": self.getNewPayLists()[0]}
        ID_data = self.siteParameter.GetDetail(IDdata)
        data = {
            "id": ID_data[1]['ReturnObject']['Id'],
            "updateMerchantData": {
                "ApiId": ID_data[1]['ReturnObject']['ApiId'],
                "MerchantNo": ID_data[1]['ReturnObject']['MerchantNo'] + "1",
                "Password": "10C36EFD68E6D4A29A62FB8AAB63A491",
                "Gateway": "http://gpkpay.fnjtd.com"
            }
        }
        response_data = self.siteParameter.UpdateMerchantData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_06(self):
        """驗證 代付商户管理 - 代付商戶 - 停用 & 啟用狀態 狀態"""
        bools = ["false", "true"]
        for i in bools:
            data = {"id": self.getNewPayLists()[0],
                    "isEnabled": i
                    }
            response_data = self.siteParameter.UpdateStatus(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_07(self):
        """驗證 代付商户管理 - 修改代付商戶有效分鐘數 狀態"""
        data = {"id": self.getNewPayLists()[0],
                "availableMinutes": self.getPayLists()[2]
                }
        response_data = self.siteParameter.UpdateAvailableMinutes(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_08(self):
        """驗證 代付商户管理 - 代付商戶目前累計歸0 狀態"""
        IDdata = {"id": self.getNewPayLists()[0]}
        ID_data = self.siteParameter.GetDetail(IDdata)
        data = {
            "id": ID_data[1]['ReturnObject']['Id']
        }
        response_data = self.siteParameter.UpdateCurrentSumToZero(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_09(self):
        """驗證 代付商户管理 - 修改代付商戶總出款限額 1元&無限制 狀態"""
        IDdata = {"id": self.getNewPayLists()[0]}
        ID_data = self.siteParameter.GetDetail(IDdata)
        TotalLimit = [1, "null"]
        for i in range(len(TotalLimit)):
            data = {
                "id": ID_data[1]['ReturnObject']['Id'],
                "totalPayoutLimit": TotalLimit[i]
            }
            response_data = self.siteParameter.UpdateMerchantTotalLimit(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_10(self):
        """驗證 代付商户管理 - 修改代付商戶自動出款設置 停用 狀態"""
        data = {"id": self.getNewPayLists()[0],
                "isOpen": 'false'
                }
        response_data = self.siteParameter.UpdateAutoPayoutSwitch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_11(self):
        """驗證 代付商户管理 - 修改代付商戶自動出款設置 啟用 狀態"""
        data = {"id": self.getNewPayLists()[0],
                "isOpen": 'true'
                }
        response_data = self.siteParameter.UpdateAutoPayoutSwitch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_12(self):
        """驗證 代付商户管理 - 修改代付商戶禁止使用 狀態  狀態"""
        data = {
            "id": self.getNewPayLists()[0],
            "updateCondition": {
                "IsCheckFirstPayoutMember": 'false',
                "IsCheckHighRiskMember": 'false',
                "IsCheckDangerMember": 'false'
            }
        }
        response_data = self.siteParameter.UpdateCondition(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_13(self):
        """ 驗證 代付商户管理 - 修改代付商戶會員等級 狀態"""
        data = {
            "id": self.getNewPayLists()[0],
            "memberLevelSettings": self.getAllMemberLevels()[1]
        }
        response_data = self.siteParameter.UpdateMemberLevelSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_14(self):
        """ 驗證 代付商户管理 - 修改代付商戶出款銀行 狀態"""
        data = {
            "id": self.getNewPayLists()[0],
            "dispensingBankIds": self.getAllBanks()
        }
        response_data = self.siteParameter.UpdateDispensingBankSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_15(self):
        """ 驗證 代付商户管理 - 修改代付商戶出款限額 狀態"""
        data = {"id": self.getNewPayLists()[0],
                "payoutLimitStart": 'null',
                "payoutLimitEnd": 'null'
                }
        response_data = self.siteParameter.UpdateMerchantLimitRange(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_16(self):
        """ 驗證 代付商户管理 - 修改代付商戶備註 狀態"""
        desc = 'QA自動化測試備註上限100QA自動化測試備註上限100QA自動化測試備註上限100QA自動化測試備註上限100QA自動化測試備註上限100QA自動化測試備註上限100QA自動化測試備註上限100QA自動化測試備註上限100QA自動化測試備註上限100完'
        data = {
            "id": self.getNewPayLists()[0],
            "memo": desc
        }
        response_data = self.siteParameter.UpdateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_17(self):
        """驗證 代付商户管理 - 修改代付商戶名稱 狀態"""
        data = {"id": self.getNewPayLists()[0],
                "name": self.getNewPayLists()[1] + '1'
                }
        response_data = self.siteParameter.UpdateMerchantName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_18(self):
        """驗證 代付商户管理 - 刪除 - 代付商戶狀態"""
        data = {"id": self.getDelPayLists()}
        response_data = self.siteParameter.Delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)



if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
