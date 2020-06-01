'''
@Created by Jo
@Date : 2020/06/01
'''

import unittest
import random
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api.system_management import PortalManagement, SmsMerchantManagement
from master_api.Home import Home
from master_api.account_login import User
from data_config.system_config import systemSetting


class SmsNotificationMgmtBaseTest(unittest.TestCase):
    """ 簡訊商户管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.home = Home(self.__http)
        self.siteParameter = SmsMerchantManagement(self.__http)
        self.user.login()

    # 登出
    def tearDown(self):
        self.user.logout()

    def getListdesc(self):
        response_data = self.siteParameter.GetList()
        for i in range(len(response_data[1])):
            if response_data[1][i]["Name"] == "QA_test":
                QAid = response_data[1][i]["Id"]
                QAsecret = response_data[1][i]["AppSecret"]
                TemplateId = response_data[1][i]["TemplateId"]
                Name = response_data[1][i]["Name"]
            else:
                QAid = response_data[1][i]["Id"]
                QAsecret = response_data[1][i]["AppSecret"]
                TemplateId = response_data[1][i]["TemplateId"]
                Name = response_data[1][i]["Name"]
        return QAid, QAsecret, TemplateId, Name

    def getAllMemberLevels(self):
        response_data = self.home.getAllMemberLevels({})
        item = []
        for i in range(len(response_data[1])):
            item.append(response_data[1][i]['Value'])
        return item

    def test_SmsNotificationMgmt_relatedApi_status_01(self):
        """驗證 簡訊商户管理 - 取得商戶列表 狀態"""
        response_data = self.siteParameter.GetList()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_02(self):
        """驗證 簡訊商户管理 - 新增商戶列狀態"""
        data = {
            "Name": "QA_test",
            "Memo": "5566",
            "AppKey": "key",
            "AppSecret": "secret",
            "TemplateId": "56",
            "LevelSettingIds": self.getAllMemberLevels()
        }
        response_data = self.siteParameter.AddSmsMerchant(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_03(self):
        """驗證 簡訊商户管理 - 取得商戶詳細 狀態"""
        data = {
            "id": self.getListdesc()[0]
        }
        response_data = self.siteParameter.GetDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_04(self):
        """驗證 簡訊商户管理 - 修改商戶資料 狀態"""
        data = {
            "id": self.getListdesc()[0],
            "newValue": self.getListdesc()[1] + "1"
        }
        response_data = self.siteParameter.UpdateSecret(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_05(self):
        """驗證 簡訊商户管理 - 修改模板ID_關&開 狀態"""
        datavalue = [1, 2]
        for i in range(len(datavalue)):
            data = {"id": self.getListdesc()[0],
                    "newValue": datavalue[i]
                    }
            response_data = self.siteParameter.UpdateState(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_06(self):
        """驗證 簡訊商户管理 - 變更可使用會員等級 狀態"""
        data = {
            "id": self.getListdesc()[0],
            "levelSettingIds": self.getAllMemberLevels()[1]
        }
        response_data = self.siteParameter.UpdateLevelSettingIds(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_07(self):
        """驗證 簡訊商户管理 - 變更備註 狀態"""
        data = {
            "id": self.getListdesc()[0],
            "newValue": "這是個測試備註"
        }
        response_data = self.siteParameter.UpdateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_08(self):
        """驗證 簡訊商户管理 - 變更名稱 狀態"""
        data = {
            "id": self.getListdesc()[0],
            "newValue": self.getListdesc()[3] + "9"
        }
        response_data = self.siteParameter.UpdateName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SmsNotificationMgmt_relatedApi_status_09(self):
        """驗證 簡訊商户管理 - 刪除商戶 狀態"""
        data = {
            "id": self.getListdesc()[0],
        }
        response_data = self.siteParameter.DeleteSmsMerchant(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
