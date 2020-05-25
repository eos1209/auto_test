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
from data_config.system_config import systemSetting
from base.CommonMethod import system_config_Setting


class YuebaoBaseTest(unittest.TestCase):
    """ 余额宝 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 參數設定
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
        """驗證 餘額寶管理 - 新增"""
        self.system = system_config_Setting()
        member_Id = self.system.getMemberLevelId()
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
                "StartTime": common_config.BeginDate,
                "EndTime": common_config.EndDate,
                "MemberLevelSettingIds": [member_Id]}
        response_data = self.yuebao.create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Yuebao_relatedApi_status_03(self):
        """驗證 餘額寶管理 - 排序"""
        Id = self.getId()
        data = {
            "Sorts": [{"Id": Id, "Order": 2}]}
        response_data = self.yuebao.sort(data)
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
        self.system = system_config_Setting()
        member_Id = self.system.getMemberLevelId_2()
        Id = self.getId()
        data = {"Id": Id, "MemberLevelSettingIds": [member_Id]}
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
