'''
@Created by loka
@Date : 2020/01/17
'''

import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import system_management
from master_api.account_login import User


class EmailNotificationMgmtBaseTest(unittest.TestCase):
    """郵件商戶管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.emailNotificationMgmt = system_management.EmailNotificationMgmt(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        response_data = self.emailNotificationMgmt.getList({})
        num = len(response_data[1])-1
        Id = response_data[1][num]['Id']
        return Id

    def test_EmailNotificationMgmt_relatedApi_status_01(self):
        """驗證 郵件商戶管理 - 取得郵件商戶列表 狀態"""
        response_data = self.emailNotificationMgmt.getList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_02(self):
        """驗證 郵件商戶管理 - 取得服務區 狀態"""
        response_data = self.emailNotificationMgmt.getServiceZone({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_03(self):
        """驗證 郵件商戶管理 - 新增郵件商戶 狀態"""
        data = {"ServiceZone": 2, "Name": "QAautotest", "Memo": "@QA_automation", "Address": "QATest", "Key": "QATest",
                "Secret": "QATest",
                "LevelSettingIds": [58]}
        response_data = self.emailNotificationMgmt.addEmailMerchant(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_04(self):
        """驗證 郵件商戶管理 - 取得詳細資料 狀態"""
        getId = self.getId()
        data = {"id": getId}
        response_data = self.emailNotificationMgmt.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_05(self):
        """驗證 郵件商戶管理 - 更新商戶名字 狀態"""
        getId = self.getId()
        data = {"id": getId, "newValue": "QATestModify"}
        response_data = self.emailNotificationMgmt.updateName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_06(self):
        """驗證 郵件商戶管理 - 更新AccessKeySecret 狀態"""
        getId = self.getId()
        data = {"id": getId, "newValue": "QATestModify"}
        response_data = self.emailNotificationMgmt.updateSecret(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_07(self):
        """驗證 郵件商戶管理 - 更新狀態 狀態"""
        getId = self.getId()
        data = {"id": getId, "newValue": 2}
        response_data = self.emailNotificationMgmt.updateState(data)
        status_code = response_data[0]
        data = {"id": getId, "newValue": 1}
        self.emailNotificationMgmt.updateState(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_08(self):
        """驗證 郵件商戶管理 - 更新會員等級 狀態"""
        getId = self.getId()
        data = {"id": getId, "levelSettingIds": [58]}
        response_data = self.emailNotificationMgmt.updateLevelSettingIds(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_EmailNotificationMgmt_relatedApi_status_09(self):
    #     """驗證 郵件商戶管理 - 更新會員等級 狀態"""
    #     getId = self.getId()
    #     data = {"id": getId, "levelSettingIds": [58]}
    #     response_data = self.emailNotificationMgmt.updateLevelSettingIds(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_10(self):
        """驗證 郵件商戶管理 - 更新備註 狀態"""
        getId = self.getId()
        data = {"id": getId, "newValue": "QATestModify"}
        response_data = self.emailNotificationMgmt.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_EmailNotificationMgmt_relatedApi_status_11(self):
        """驗證 郵件商戶管理 - 刪除郵件商戶 狀態"""
        getId = self.getId()
        data = {"id": getId}
        # print(getId)
        response_data = self.emailNotificationMgmt.deleteEmailMerchant(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
