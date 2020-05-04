'''
@Created by loka
@Date : 2019/12/12
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import account_management
from master_api.account_login import User
from master_api import Home
import time


class YuebaoBoardBaseTest(unittest.TestCase):
    """ 余额宝看板 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.yuebaoBoard = account_management.YuebaoBoard(self.__http)
        self.AllMemberLevels = Home.Home(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def IdList(self):
        IDs = {'Id': '', 'OuterId': ''}
        data = {"pageSize": 5,
                "search": {}}
        response_data = self.yuebaoBoard.list(data)
        for i in range(len(response_data[1]['ReturnObject']['BoardListItems'])):
            IDs['Id'] = response_data[1]['ReturnObject']['BoardListItems'][i]['Id']
            IDs['OuterId'] = response_data[1]['ReturnObject']['BoardListItems'][i]['OuterId']
        return IDs

    def GetAllMemberLevels(self):
        data = {}
        response_data = self.AllMemberLevels.getAllMemberLevels(data)
        return response_data[1]

    def test_YuebaoBoard_relatedApi_status_01(self):
        """驗證 余额宝 - 取得看板頁面"""
        response_data = self.yuebaoBoard.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_YuebaoBoard_relatedApi_status_02(self):
        """驗證 余额宝 - 取得看板列表資料"""
        data = {"pageSize": 100,
                "search": {}}
        response_data = self.yuebaoBoard.list(data)

        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_YuebaoBoard_relatedApi_status_03(self):
        """驗證 余额宝 - 取得總計數據"""
        data = {"search": {}}
        response_data = self.yuebaoBoard.summary(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_YuebaoBoard_relatedApi_status_04(self):
        """驗證 餘額寶看板 - 匯出Excel"""
        items = self.GetAllMemberLevels()
        for i in range(len(items)):
            data = {'MemberLevelSettingIds': [items[i]['Value']], "_": time.time()}
            response_data = self.yuebaoBoard.export(data)
            print(response_data[1])
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_YuebaoBoard_relatedApi_status_05(self):
        """驗證 餘額寶看板 - 匯出Excel-未帶搜尋條件匯出Excel"""
        data = {"_": time.time()}
        response_data = self.yuebaoBoard.export(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '请带入搜寻条件')

    def test_YuebaoBoard_relatedApi_status_06(self):
        """驗證 餘額寶看板 - 余额宝看板明细"""
        IDs = self.IdList()
        data = {"outerId": IDs['OuterId'],
                "id": IDs['Id']
                }
        response_data = self.yuebaoBoard.detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
