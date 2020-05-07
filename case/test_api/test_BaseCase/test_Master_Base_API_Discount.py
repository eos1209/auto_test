'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config.system_config import systemSetting
from master_api import account_management
from master_api.account_login import User
from base.TimeClass import get_yesterday as yesterday
from master_api.account_login import User
from master_api.system_management import PortalManagement


class DiscountBaseTest(unittest.TestCase):
    """ 返水计算 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.discount = account_management.Discount(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    # 取站台ID
    def getWebsiteId(self):
        response_data = self.PortalManagement.getWebsiteList({})
        for i in range(len(response_data[1]['ReturnObject'])):
            if self.config.siteName_config() == response_data[1]['ReturnObject'][i]['Name']:
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def getTempId(self):
        data = {"dateBegin": str(yesterday()),
                "dateEnd": str(yesterday()),
                "take": 500,
                "skip": 0
                }
        response_data = self.discount.calculate(data)
        return response_data[1]['TempId']

    def getHistoryID(self):
        data = {"take": 100, "skip": 0}
        response_data = self.discount.loadHistory(data)
        for i in range(len(response_data[1])):
            Id = response_data[1][i]['Id']
            Name = response_data[1][i]['Name']
        return Id, Name

    def test_discount_relatedApi_status_01(self):
        """驗證 返水计算 - 取得頁面"""
        response_data = self.discount.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_02(self):
        """驗證 返水计算 - 載入歷史資料"""
        data = {"take": 100,
                "skip": 0}
        response_data = self.discount.loadHistory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_03(self):
        """驗證 返水計算 - 清除Temp 狀態"""
        data = {}
        response_data = self.discount.ClearTemp(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_04(self):
        """驗證 - 返水計算 - 計算 狀態"""
        data = {"dateBegin": str(yesterday()),
                "dateEnd": str(yesterday()),
                "take": 500,
                "skip": 0
                }
        response_data = self.discount.calculate(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_05(self):
        """驗證 - 返水計算 - 匯出計算明細 狀態"""
        ID = self.getTempId()
        data = {"id": ID}
        response_data = self.discount.exportTemp(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_06(self):
        """驗證 - 返水計算 - 取得記錄 狀態"""
        # data = {"id": ID['Id']}
        data = {"id": self.getHistoryID()[0]}
        response_data = self.discount.getRecord(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_07(self):
        """驗證 - 返水計算 - 取得詳細記錄 狀態"""
        data = {"id": self.getHistoryID()[0],
                "connectionId": self.user.info()
                }
        response_data = self.discount.getRecordDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_08(self):
        """驗證 - 返水計算 - 取得記錄樣版 狀態"""
        data = {}
        response_data = self.discount.detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_09(self):
        """返水计算-取得返水發放已沖銷資訊"""
        data = {"id": self.getHistoryID()[0]}
        response_data = self.discount.getRevokedRecordSummary(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_10(self):
        """驗證 - 返水計算 - 取得返水發放沖銷詳細記錄 狀態"""
        data = {"id": self.getHistoryID()[0],
                "connectionId": self.user.info()
                }
        response_data = self.discount.getRevokedRecordData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_11(self):
        """驗證 - 返水計算 - 匯出(發送明細) 狀態"""
        data = {"id": self.getHistoryID()[0],
                "connectionId": self.user.info()
                }
        response_data = self.discount.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_discount_relatedApi_status_12(self):
        """驗證 - 返水計算 - 返水發送明細 修改名稱 """
        data = {"id": self.getHistoryID()[0],
                "name": self.getHistoryID()[1] + "1"
                }
        response_data = self.discount.updateDiscountRecordName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
