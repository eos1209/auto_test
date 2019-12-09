'''
@Created by loka
@Date : 2019/12/03
'''

import unittest
from data_config import common_config
from data_config import master_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import account_management
from master_api.account_login import User
from datetime import datetime, timedelta
import time


# switch開發調整
# 原因:執行這一整個baseApi呼叫因為檔案匯入需要時間的關係，後面的取消預約匯入與沖銷優惠沒有辦法有效執行與驗證
# 方法:
# method1:切開寫一個function進行呼叫
# method2:切檔案

class DepositImportBaseTest(unittest.TestCase):
    """優惠匯入 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.DepositImport = account_management.DepositImport(self.__http)
        self.user.login()

    def test_DepositImport_baseApi_status_01(self):
        """優惠匯入 - 優惠匯入頁面 狀態"""
        response_data = self.DepositImport.index()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_DepositImport_baseApi_status_02(self):
        """優惠匯入 - 取得優惠匯入列表 狀態"""
        data = {"take": 100, "skip": 0}
        response_data = self.DepositImport.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_DepositImport_baseApi_status_03(self):
        """優惠匯入 - 上傳Excel 狀態"""
        upload_file = common_config.file_Path + 'testData/depositImport-A.xlsx'  # 檔案
        mime_Type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'filebase': ('depositImport-A.xlsx', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.DepositImport.getExcelSum(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉

    def test_DepositImport_baseApi_status_04(self):
        """優惠匯入 - 優惠匯入-立刻 狀態"""
        ReserveTime = (datetime.now() + timedelta(hours=1)).strftime("%Y/%m/%d %H:%M:%S")  # 設定一個小時後開始進行優惠匯入
        # print(ReserveTime)
        upload_file = common_config.file_Path + 'testData/depositImport-A.xlsx'  # 檔案
        mime_Type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'password': (None, master_config.Master_Password),  # 有其他參數上傳用這種mode
                'Filebase': ('depositImport-A.xlsx', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.DepositImport.submitDepositImport(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉
        time.sleep(10)

    def test_DepositImport_baseApi_status_06(self):
        """優惠匯入 - 檢查沖銷 狀態"""
        data = {'take': 100, 'skip': 0}
        getList = self.DepositImport.getList(data)
        getId = getList[1]['Records'][0]['Id']
        data = {'Id': getId}
        response_data = self.DepositImport.checkRevocation(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_DepositImport_baseApi_status_07(self):
        """優惠匯入 - 優惠沖銷 狀態"""
        data = {'take': 100, 'skip': 0}
        getList = self.DepositImport.getList(data)
        getId = getList[1]['Records'][0]['Id']
        data = {'password': master_config.Master_Password, 'portalMemo': '@QA_automation', 'memo': '@QA_automation',
                'recordId': getId}
        response_data = self.DepositImport.revoke(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_DepositImport_baseApi_status_08(self):
        """優惠匯入 - 取得優惠沖銷詳細 狀態"""
        data = {'take': 100, 'skip': 0}
        getList = self.DepositImport.getList(data)
        getId = getList[1]['Records'][0]['Id']
        data = {'Id': getId}
        response_data = self.DepositImport.getRevokeDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_DepositImport_baseApi_status_05(self):
        """優惠匯入 - 優惠匯入-預約時間 狀態"""
        ReserveTime = (datetime.now() + timedelta(hours=-11)).strftime("%Y/%m/%d %H:%M:%S")  # 設定一個小時後開始進行優惠匯入
        # print(ReserveTime)
        upload_file = common_config.file_Path + 'testData/depositImport-B.xlsx'  # 檔案
        mime_Type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'password': (None, master_config.Master_Password), 'ReserveTime': (None, ReserveTime),  # 有其他參數上傳用這種mode
                'Filebase': ('depositImport-B.xlsx', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.DepositImport.submitDepositImport(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉
        time.sleep(5)

    def test_DepositImport_baseApi_status_09(self):
        """優惠匯入 - 取消預約匯入 狀態"""
        data = {'take': 100, 'skip': 0}
        getList = self.DepositImport.getList(data)
        getId = getList[1]['Records'][0]['Id']
        data = {'RecordId': getId}
        response_data = self.DepositImport.cancelReserveImport(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
