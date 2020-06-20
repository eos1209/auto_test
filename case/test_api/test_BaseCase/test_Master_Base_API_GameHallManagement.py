'''
@Created by loka
@Date : 2019/12/25
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api.account_login import User
from data_config import common_config
from master_api import system_management
from base.TimeClass import get_todaynow, get_yesterdayS


class GameHailManagementBaseTest(unittest.TestCase):
    """ 娛樂城管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.GameHailManagement = system_management.GameHallManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getGameHailList(self):  # 取得娛樂城名稱+Id 清單
        response_data = self.GameHailManagement.getGameHallList({})
        gameHall = {'Id': {}, 'Text': {}}
        for i in range(len(response_data[1])):
            gameHall['Id'][i] = response_data[1][i]['GameHallId']
            gameHall['Text'][i] = response_data[1][i]['GameHallUrlText']
        return gameHall

    def test_GameHallManagement_relatedApi_status_01(self):
        """驗證 娛樂城管理 - 取得列表頁面"""
        response_data = self.GameHailManagement.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_02(self):
        """驗證 娛樂城管理 - 取得娛樂城列表"""
        response_data = self.GameHailManagement.getGameHallList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_03(self):
        """驗證 娛樂城管理 - 娛樂城列表資訊"""
        response_data = self.GameHailManagement.getGameHallListInfo({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_04(self):
        """驗證 娛樂城管理 - 娛樂城詳細資料頁面"""
        response_data = self.GameHailManagement.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_05(self):
        """驗證 娛樂城管理 - 娛樂城詳細資料"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城詳細資料
        for i in range(len(getData['Id'])):
            data = {'gameHallUrlText': getData['Text'][i]}
            response_data = self.GameHailManagement.getGameHallDetail(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_06(self):
        """驗證 娛樂城管理 - 把url的Text改成要顯示的Text"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城url的Text改成要顯示的Text
        for i in range(len(getData['Id'])):
            data = {'gameHallUrlText': getData['Text'][i], "jaguar": 'null'}
            response_data = self.GameHailManagement.transferGameHallUrlText(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_07(self):
        """驗證 娛樂城管理 - 取得娛樂城歷史紀錄頁面"""
        response_data = self.GameHailManagement.history({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_08(self):
        """驗證 娛樂城管理 - 娛樂城歷史紀錄"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城歷史紀錄
        for i in range(len(getData['Id'])):
            data = {'gameHallUrlText': getData['Text'][i], "take": 100, "skip": 0, "query": {}}
            response_data = self.GameHailManagement.loadHistory(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_09(self):
        """驗證 娛樂城管理 - 踢除所有會員"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城踢除所有會員
        for i in range(len(getData['Id'])):
            data = {"gameHallUrlText": getData['Text'][i]}
            detailList = self.GameHailManagement.getGameHallDetail(data)
            getIsable = detailList[1]['ExitGameHallEnable']
            if getIsable and True:
                data = {"gameSupplierType": getData['Id'][i]}
                response_data = self.GameHailManagement.exitGameHall(data)
                status_code = response_data[0]
                self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_10(self):
        """驗證 娛樂城管理 - 取回所有錢包"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城取回所有錢包
        for i in range(len(getData['Id'])):
            data = {"gameHallUrlText": getData['Text'][i]}
            detailList = self.GameHailManagement.getGameHallDetail(data)
            getIsable = detailList[1]['TransferMoneyBackEnable']
            if getIsable and True:
                data = {"gameSupplierType": getData['Id'][i]}
                response_data = self.GameHailManagement.transferMoneyBack(data)
                status_code = response_data[0]
                self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_11(self):
        """驗證 娛樂城管理 - 更新所有錢包"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城取回所有錢包
        for i in range(len(getData['Id'])):
            data = {"gameHallUrlText": getData['Text'][i]}
            detailList = self.GameHailManagement.getGameHallDetail(data)
            getIsable = detailList[1]['UpdateAllWalletEnable']
            if getIsable and True:
                data = {"gameSupplierType": getData['Id'][i]}
                response_data = self.GameHailManagement.updateAllWallet(data)
                status_code = response_data[0]
                self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_12(self):
        """驗證 娛樂城管理 - 進入後台"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城進入後台
        for i in range(len(getData['Id'])):
            data = {"gameHallUrlText": getData['Text'][i]}
            detailList = self.GameHailManagement.getGameHallDetail(data)
            getIsable = detailList[1]['EnterBackofficeEnable']
            if getIsable and True:
                data = {"gameSupplierType": getData['Id'][i]}
                response_data = self.GameHailManagement.getBackofficeUrl(data)
                status_code = response_data[0]
                self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_13(self):
        """驗證 娛樂城管理 - 開啟/關閉狀態"""
        # Step 1 : 取得娛樂城名單
        getData = self.getGameHailList()
        # Step 2:用迴圈方式走訪每個娛樂城開啟關閉
        for i in range(len(getData['Id'])):
            if (getData['Id'][i] == 67 or getData['Id'][i] == 78 or getData['Id'][i] == 34
                    or getData['Id'][i] == 39):
                continue
            else:
                data = {"gameSupplierType": getData['Id'][i], "isEnterable": 'false'}  # 娛樂城關閉
                response_data = self.GameHailManagement.modifyGameHallStatus(data)
                status_code = response_data[0]
                data = {"gameSupplierType": getData['Id'][i], "isEnterable": 'true'}  # 娛樂城開啟
                self.GameHailManagement.modifyGameHallStatus(data)
                self.assertEqual(status_code, common_config.Status_Code)

    def test_GameHallManagement_relatedApi_status_14(self):
        """驗證 娛樂城管理 - MG投注記錄"""
        start = get_yesterdayS()
        end = get_todaynow()
        data = {"GameSupplierType": "MG", "Account": 'test1234', "StartTime": start,
                "EndTime": end}
        response_data = self.GameHailManagement.calculateValidBet(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
