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


class YuebaoBaseTest(unittest.TestCase):
    """ 余额宝 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.yuebao = system_management.Yuebao(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        response_data = self.yuebao.list({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if response_data[1]['ReturnObject'][i]['SettingName'] == 'QA_test' + common_config.now:
                get_id = response_data[1]['ReturnObject'][i]['Id']
                return get_id

    def test_Yuebao_relatedApi_status_01(self):
        """驗證 餘額寶管理 - 取得列表"""
        response_data = self.yuebao.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_02(self):
        """驗證 餘額寶管理 - 排序"""
        data = {
            "Sorts": [{"Id": 137, "Order": 1}, {"Id": 125, "Order": 2}, {"Id": 127, "Order": 3}, {"Id": 86, "Order": 4},
                      {"Id": 126, "Order": 5}, {"Id": 135, "Order": 6}, {"Id": 116, "Order": 7},
                      {"Id": 115, "Order": 8}, {"Id": 114, "Order": 9}, {"Id": 109, "Order": 10},
                      {"Id": 117, "Order": 11}, {"Id": 107, "Order": 12}, {"Id": 106, "Order": 13},
                      {"Id": 105, "Order": 14}, {"Id": 104, "Order": 15}, {"Id": 103, "Order": 16},
                      {"Id": 102, "Order": 17}, {"Id": 101, "Order": 18}, {"Id": 100, "Order": 19},
                      {"Id": 99, "Order": 20}, {"Id": 98, "Order": 21}, {"Id": 96, "Order": 22},
                      {"Id": 95, "Order": 23}, {"Id": 94, "Order": 24}, {"Id": 92, "Order": 25},
                      {"Id": 89, "Order": 26}, {"Id": 88, "Order": 27}, {"Id": 79, "Order": 28},
                      {"Id": 78, "Order": 29}, {"Id": 77, "Order": 30}, {"Id": 76, "Order": 31},
                      {"Id": 69, "Order": 32}, {"Id": 66, "Order": 33}, {"Id": 68, "Order": 34},
                      {"Id": 72, "Order": 35}, {"Id": 71, "Order": 36}, {"Id": 70, "Order": 37},
                      {"Id": 56, "Order": 38}, {"Id": 64, "Order": 39}, {"Id": 65, "Order": 40},
                      {"Id": 51, "Order": 41}, {"Id": 61, "Order": 42}]}
        response_data = self.yuebao.sort(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_03(self):
        """驗證 餘額寶管理 - 新增"""
        data = {"Name": "QA_test" + common_config.now,
                "MinAmount": 10,
                "MaxAmount": 20,
                "SettleTime": 1,
                "Rate": 1,
                "LimitInterest": 1,
                "IsCycleSettle": 'true',
                "InterestAuditMultiple": 1,
                "LimitOrderCount": 10,
                "LimitUserOrderCount": 5,
                "limitOrderInterval": 1,
                "StartTime": common_config.BeginDate, "EndTime": common_config.EndDate,
                "MemberLevelSettingIds": [137]}
        response_data = self.yuebao.create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_04(self):
        """驗證 餘額寶管理 - 詳細資料"""
        response_data = self.yuebao.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_05(self):
        """驗證 餘額寶管理 - 更改會員等級"""
        # step 1 取Id
        Id = self.getId()
        data = {"Id": Id, "MemberLevelSettingIds": [21]}
        response_data = self.yuebao.setMemberLevelSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_06(self):
        """驗證 餘額寶管理 - 設定下架時間"""
        # step 1 取Id
        Id = self.getId()
        data = {"Id": Id, "StartTime": common_config.FirstDay, "EndTime": common_config.EndDay}
        response_data = self.yuebao.setEnableTime(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_07(self):
        """驗證 餘額寶管理 - 上下架歷程記錄"""
        # step 1 取Id
        Id = self.getId()
        data = {"Id": Id, "pageSize": 10000}
        response_data = self.yuebao.history(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_08(self):
        """驗證 餘額寶管理 - 強制贖回"""
        # step 1 取Id
        Id = self.getId()
        data = {"Id": Id}
        response_data = self.yuebao.withdraw(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
