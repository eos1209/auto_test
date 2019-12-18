'''
@Created by loka
@Date : 2019/11/29
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.CommonMethod import UploadFile
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from data_config import master_config


class MemberImportBaseTest(unittest.TestCase):
    """會員匯入 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberImport = member_and_agent.MemberImport(self.__http)

        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberImport_relatedApi_status_01(self):
        """驗證 會員匯入 - 會員匯入頁面 狀態"""
        response_data = self.memberImport.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_02(self):
        """驗證 會員匯入 - 會員匯入紀錄 狀態"""
        response_data = self.memberImport.getRecord({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_03(self):
        """驗證 會員匯入 - 確認是否有會員匯入 狀態"""
        response_data = self.memberImport.checkHasMemberImporting({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_04(self):
        """驗證 會員匯入 - 下載範本 狀態"""
        response_data = self.memberImport.downloadExample({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_05(self):
        """驗證 會員匯入 - 上傳Excel 狀態"""
        self.upload = UploadFile('document/memberImport.xlsx',  # 檔案路徑
                                 'filebase',  # 上傳欄位
                                 'memberImport.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.memberImport.getExcelSum(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 實作關閉檔案物件方法

    def test_MemberImport_relatedApi_status_06(self):
        """驗證 會員匯入 - 開始匯入 狀態"""
        self.upload = UploadFile('document/memberImport.xlsx',  # 檔案路徑
                                 'importFile',  # 上傳欄位
                                 'memberImport.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = {'password': (None, master_config.Master_Password), 'isFilterBank': (None, 'true'),  # 有其他參數上傳用這種mode
                self.upload.upload_name: (
                self.upload.filename, self.upload.open_file, self.upload.file_type, {'Expires': '0'})}
        response_data = self.memberImport.submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
