'''
@Created by loka
@Date : 2019/12/30
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import system_management
from master_api.account_login import User
from base.CommonMethod import UploadFile


class BlockListManagementBaseTest(unittest.TestCase):
    """封鎖名單管理 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.blockListManagement = system_management.BlockListManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_BlockListManagement_relatedApi_status_01(self):
        """驗證 封鎖名單管理-取得銀行帳戶列表 狀態"""
        data = {"take": 100, "skip": 0, "search": {"tab": "2"}}
        response_data = self.blockListManagement.bankAccountGetList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_02(self):
        """驗證 封鎖名單管理-取得銀行列表 狀態"""
        response_data = self.blockListManagement.bankAccountGetGroupBank({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_03(self):
        """驗證 封鎖名單管理-匯出銀行封鎖名單Excel 狀態"""
        response_data = self.blockListManagement.bankAccountExportExcel({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_04(self):
        """驗證 封鎖名單管理-新增銀行帳戶封鎖名單 狀態"""
        data = {"bankName": "农业银行", "bankAccount": "123456", "memo": "@QA_automation"}
        response_data = self.blockListManagement.bankAccountAddBankAccountBlockInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_05(self):
        """驗證 封鎖名單管理-刪除銀行帳戶封鎖名單 狀態"""
        data = {"take": 100, "skip": 0, "search": {"tab": "2"}}
        response_data = self.blockListManagement.bankAccountGetList(data)
        getId = response_data[1]['ReturnObject'][0]['Id']
        data = [getId]
        response_data = self.blockListManagement.bankAccountDeleteBankBlocks(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_06(self):
        """驗證 封鎖名單管理-下載銀行帳戶匯入範本 狀態"""
        response_data = self.blockListManagement.bankAccountDownloadSampleExcel({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_07(self):
        """驗證 封鎖名單管理-檢查銀行帳戶匯入範本上傳 狀態"""
        self.upload = UploadFile('document/bankAccountBlockManagement.xlsx',  # 檔案路徑
                                 'importFile',  # 上傳欄位
                                 'bankAccountBlockManagement.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.blockListManagement.bankAccountCheckImportExcel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉

    def test_BlockListManagement_relatedApi_status_08(self):
        """驗證 封鎖名單管理- 銀行帳戶匯入範本上傳 狀態"""
        self.upload = UploadFile('document/bankAccountBlockManagement.xlsx',  # 檔案路徑
                                 'importFile',  # 上傳欄位
                                 'bankAccountBlockManagement.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.blockListManagement.bankAccountImportExcel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉
        # step 2:刪除匯入資料
        data = {"take": 100, "skip": 0, "search": {"tab": "2"}}
        response_data = self.blockListManagement.bankAccountGetList(data)
        getId = response_data[1]['ReturnObject'][0]['Id']
        data = [getId]
        self.blockListManagement.bankAccountDeleteBankBlocks(data)

    def test_BlockListManagement_relatedApi_status_09(self):
        """驗證 封鎖名單管理-取得IP列表 狀態"""
        data = {"take": 100, "skip": 0, "search": {"tab": "1"}}
        response_data = self.blockListManagement.ipGetList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_10(self):
        """驗證 封鎖名單管理-匯出銀IP鎖名單Excel 狀態"""
        response_data = self.blockListManagement.ipExportExcel({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_11(self):
        """驗證 封鎖名單管理-新增IP封鎖名單 狀態"""
        data = {"ipv4": "127.0.0.1", "memo": "@QA_automation"}
        response_data = self.blockListManagement.ipAddIPBlockInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_12(self):
        """驗證 封鎖名單管理-刪除銀行帳戶封鎖名單 狀態"""
        data = {"take": 100, "skip": 0, "search": {"tab": "1"}}
        response_data = self.blockListManagement.ipGetList(data)
        getId = response_data[1]['ReturnObject'][0]['Id']
        data = [getId]
        response_data = self.blockListManagement.ipDeleteIPBlocks(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_13(self):
        """驗證 封鎖名單管理-檢查IP匯入範本上傳 狀態"""
        self.upload = UploadFile('document/ipBlockManagement.xlsx',  # 檔案路徑
                                 'importFile',  # 上傳欄位
                                 'ipBlockManagement.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.blockListManagement.ipCheckImportExcel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉

    def test_BlockListManagement_relatedApi_status_14(self):
        """驗證 封鎖名單管理- IP匯入範本上傳 狀態"""
        self.upload = UploadFile('document/ipBlockManagement.xlsx',  # 檔案路徑
                                 'importFile',  # 上傳欄位
                                 'ipBlockManagement.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.blockListManagement.ipImportExcel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉
        # step 2:刪除匯入資料
        data = {"take": 100, "skip": 0, "search": {"tab": "1"}}
        response_data = self.blockListManagement.ipGetList(data)
        getId = response_data[1]['ReturnObject'][0]['Id']
        data = [getId]
        self.blockListManagement.ipDeleteIPBlocks(data)

    def test_BlockListManagement_relatedApi_status_15(self):
        """驗證 封鎖名單管理- 取得國別阻擋名單 狀態"""
        response_data = self.blockListManagement.getCountrySetting({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_16(self):
        """驗證 封鎖名單管理- 取得白名單IP名單 狀態"""
        response_data = self.blockListManagement.getWhiteListSetting({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_17(self):
        """驗證 封鎖名單管理- 更新國別阻擋名單 狀態"""
        data = {"blockedCountryList": []}
        response_data = self.blockListManagement.updateCountryBlockSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_18(self):
        """驗證 封鎖名單管理- 檢查新增白名單IP 狀態"""
        data = {"ip": "127.0.0.1"}
        response_data = self.blockListManagement.checkWhiteIpWhenAdd(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_BlockListManagement_relatedApi_status_19(self):
        """驗證 封鎖名單管理- 更新白名單IP 狀態"""
        data = {
            "whiteListSettings": ["211.23.116.131", "118.163.212.115", "211.23.224.148", "59.125.28.220", "111.11.15.2",
                                  "113.141.163.16", "211.22.163.139"],
            "whiteListMemos": ["菲律宾代理ABIN办公室", "菲律宾代理ASA办公室", "", "业务使用", "", "陝西02", "MIS+Infra辦公室"]}
        response_data = self.blockListManagement.updateWhiteListSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
