'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import account_management
from master_api.account_login import User
from data_config.system_config import systemSetting
from base.CommonMethod import SetDelayTime


class MemberTransactionBaseTest(unittest.TestCase):
    """交易記錄查詢 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberTransaction = account_management.MemberTransaction(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def searchDataId(self, mode):
        # 取得單筆交易Id(交易單號) - 單一會員紀錄
        if mode == 1:
            # 撈全部
            searchData = {"Account": self.config.test_Member_config(),
                          "Types": ["Account", "ThirdPartyPayment", "OnlineWithdraw", "Manual", "Bonus", "Discount",
                                    "Payoff", "AnyTimeDiscount", "Yuebao", "Other"]}
            return self.memberTransaction.search(searchData)
        elif mode == 2:
            # 實際存提資料
            searchData = {"Account": self.config.test_Member_config(),
                          "Types": ["Account", "ThirdPartyPayment", "OnlineWithdraw", "Manual"]
                          }
            return self.memberTransaction.search(searchData)
        elif mode == 3:
            # 時返明細
            searchData = {"Types": ["AnyTimeDiscount"]}
            return self.memberTransaction.search(searchData)

    def test_MemberTransaction_baseApi_status_01(self):
        """驗證 交易記錄查詢頁面狀態"""
        response_data = self.memberTransaction.query({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_02(self):
        """驗證 取得交易紀錄類型狀態"""
        response_data = self.memberTransaction.queryInit({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_03(self):
        """驗證 交易紀錄搜尋狀態"""
        data = {"Types": [
            "Account",
            "ThirdPartyPayment",
            "OnlineWithdraw",
            "Manual",
            "Bonus",
            "Discount",
            "Payoff",
            "AnyTimeDiscount",
            "Other"
        ]}
        response_data = self.memberTransaction.search(data)
        status_code = response_data[0]
        SetDelayTime()
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_04(self):
        """驗證 取得交易記錄詳細頁面狀態"""
        response_data = self.memberTransaction.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_05(self):
        """驗證 取得單筆紀錄明細狀態"""
        detailId = self.searchDataId(1)
        data = {"id": detailId[1]['PageData'][0]['Id']}
        response_data = self.memberTransaction.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_06(self):
        """驗證 更新實際存提狀態 2019/12/03"""
        searchData = {"Account": self.config.test_Member_config(),
                      "Types": ["Account", "ThirdPartyPayment", "OnlineWithdraw", "Manual"]}  # 篩選有實際存提的資料
        search = self.memberTransaction.search(searchData)
        SetDelayTime()
        data = {"id": search[1]['PageData'][0]['Id'],
                "isReal": True}
        response_data = self.memberTransaction.updateIsReal(data)
        # print(response_data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_07(self):
        """驗證 匯出狀態"""
        data = {"Account": self.config.test_Member_config(),
                "TimeBegin": common_config.BeginDate,
                "Types": ["Account",
                          "ThirdPartyPayment",
                          "OnlineWithdraw",
                          "Manual",
                          "Bonus",
                          "Discount",
                          "Payoff",
                          "AnyTimeDiscount",
                          "Other"]}
        response_data = self.memberTransaction.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTransaction_baseApi_status_08(self):
        """驗證 更新實際存提-是否成功 -2019/12/03"""
        # Step 1
        searchData = self.searchDataId(2)
        print(searchData[1])
        # Step 2
        SetDelayTime()
        data = {"id": searchData[1]['PageData'][0]['Id']}
        response_data = self.memberTransaction.getDetail(data)
        print(response_data[1])
        self.assertEqual(response_data[1]['Detail']['IsReal'], True)

    def test_MemberTransaction_baseApi_status_09(self):
        """驗證 時返明細狀態 - 2019/12/03"""
        searchData = self.searchDataId(3)
        SetDelayTime()
        data = {"id": searchData[1]['PageData'][0]['Id']}
        response_data = self.memberTransaction.getAnytimeDiscountDetail(data)
        status_code = response_data[0]
        print(response_data[1])
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
