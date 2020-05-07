'''
@Created by loka
@Date : 2020/01/20
'''

import unittest
from random import random

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement, PayoutMerchantManagement
from master_api.account_login import User
from data_config.system_config import systemSetting


class ThirdPartyPayoutBaseTest(unittest.TestCase):
    """ 代付商户管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteParameter = PayoutMerchantManagement(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    # 登出
    def tearDown(self):
        self.user.logout()

    def getApilist(self):
        items = self.siteParameter.GetApiList()
        for i in range(len(items[1]['ReturnObject'])):
            if items[1]['ReturnObject'][i]['Name'] == 'TestPayout':
                Name = items[1]['ReturnObject'][i]['Name']
                Api_id = items[1]['ReturnObject'][i]['Api_id']
                break
            else:
                Name = items[1]['ReturnObject'][i]['Name']
                Api_id = items[1]['ReturnObject'][i]['Api_id']
        return Name, Api_id

    def getPayLists(self):
        response_data = self.siteParameter.GetList()
        for i in range(len(response_data[1]['ReturnObject'])):
            Id = response_data[1]['ReturnObject'][i]['Id']
            Name = response_data[1]['ReturnObject'][i]['Name']
            AvailableMinutes = response_data[1]['ReturnObject'][i]['AvailableMinutes']
        return Id, Name, AvailableMinutes

    #
    # def getApilistxxxxx(self):
    #     """此段之後要殺掉"""
    #     xx = []
    #     items = self.siteParameter.GetApiList()
    #     for i in range(len(items[1]['ReturnObject'])):
    #         xx.append(items[1]['ReturnObject'][i]['Api_id'])
    #     return xx
    #
    # def getPayListsxxxxx(self):
    #     xx = []
    #     response_data = self.siteParameter.GetList()
    #     for i in range(len(response_data[1]['ReturnObject'])):
    #         if response_data[1]['ReturnObject'][i]['TotalPayoutLimit'] != 'None':
    #             xx.append(response_data[1]['ReturnObject'][i]['Id'])
    #     return xx

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
        item = self.getApilist()
        data = {"AvailableMinutes": 10,  # 有效分鐘數
                "IsAutoPayout": "true",  # 自动出款
                "Name": "jo_QA",
                "Api_id": item[1],
                "MerchantNo": "xian4",
                "Password": "10C36EFD68E6D4A29A62FB8AAB63A491",
                "Gateway": "http://pay.jp777.net",
                "TotalPayoutLimit": 1,  # 总出款限额
                "IsCheckFirstPayoutMember": "true",  # 首次取款會員
                "IsCheckHighRiskMember": "true",  # 高風險
                "IsCheckDangerMember": "true",
                "Memo": "test",  # 註解
                "MemberLevelSettings": [1, 2, 3, 4, 5, 6],  # MemberLevel
                "DispensingBankSettings": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                           22, 23, 24, 25, 26, 27, 28, 29]  # Bank
                }
        response_data = self.siteParameter.Create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_05(self):
        """驗證 代付商户管理 - 修改代付商戶名稱 狀態"""
        data = {"id": self.getPayLists()[0],
                "name": self.getPayLists()[1] + '1'
                }
        response_data = self.siteParameter.UpdateMerchantName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_06(self):
        """驗證 代付商户管理 - 代付商戶 - 停用 & 啟用狀態 狀態"""
        bools = ["false", "true"]
        for i in bools:
            data = {"id": self.getPayLists()[0],
                    "isEnabled": i
                    }
            response_data = self.siteParameter.UpdateStatus(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_ThirdPartyPayout_relatedApi_status_07(self):
        """驗證 代付商户管理 - 修改代付商戶有效分鐘數 狀態"""
        data = {"id": self.getPayLists()[0],
                "availableMinutes": self.getPayLists()[2]
                }
        response_data = self.siteParameter.UpdateAvailableMinutes(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_ThirdPartyPayout_relatedApi_status_(self):
    #     """驗證 代付商户管理 - 刪除 - 代付商戶狀態"""
    #     items = self.getPayLists()
    #     data = {"id": items[0]}

    # def test_ThirdPartyPayout_relatedApi_status_(self):
    #     """幫lock新增代付商戶 狀態   之後要殺掉"""
    #     # item = self.getApilist()
    #     item = self.getApilistxxxxx()
    #     print(len(item))
    #     for i in range(len(item)):
    #         data = {"AvailableMinutes": 10,  # 有效分鐘數
    #                 "IsAutoPayout": "true",  # 自动出款
    #                 "Name": "QA_JO" + str(i),
    #                 "Api_id": item[i],
    #                 "MerchantNo": "xian4",
    #                 "Password": "10C36EFD68E6D4A29A62FB8AAB63A491",
    #                 "Gateway": "http://pay.jp777.net",
    #                 "TotalPayoutLimit": 1,  # 总出款限额
    #                 "IsCheckFirstPayoutMember": "true",  # 首次取款會員
    #                 "IsCheckHighRiskMember": "true",  # 高風險
    #                 "IsCheckDangerMember": "true",
    #                 "Memo": "test",  # 註解
    #                 "MemberLevelSettings": [1, 2, 3, 4, 5, 6],  # MemberLevel
    #                 "DispensingBankSettings": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    #                                            21,
    #                                            22, 23, 24, 25, 26, 27, 28, 29]  # Bank
    #                 }
    #         print(data)
    #         response_data = self.siteParameter.Create(data)
    #         status_code = response_data[0]
    #         self.assertEqual(status_code, common_config.Status_Code)
    #
    # def test_ThirdPartyPayout_relatedApi_status_(self):
    #     """幫lock 代付商户管理 - 修改代付商戶出款金額改為無限制 之後要殺掉 狀態"""
    #     xx = self.getPayListsxxxxx()
    #     for i in range(len(xx)):
    #         data = {"id": xx[i],
    #                 "totalPayoutLimit": "null"}
    #         print(data)
    #         response_data = self.siteParameter.UpdateMerchantTotalLimit(data)
    #         print(response_data[1])
    #         status_code = response_data[0]
    #         self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
