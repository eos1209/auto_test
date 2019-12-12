'''
@Created by loka
@Date : 2019/11/29
'''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import memeber_and_agent
from master_api.account_login import User
from data_config import master_config


class MemberImportBaseTest(unittest.TestCase):
    """會員匯入 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberImport = memeber_and_agent.MemberImport(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberImport_relatedApi_status_01(self):
        """驗證 會員匯入 - 會員匯入頁面 狀態"""
        response_data = self.memberImport.index()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_02(self):
        """驗證 會員匯入 - 會員匯入紀錄 狀態"""
        response_data = self.memberImport.getRecord()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_03(self):
        """驗證 會員匯入 - 確認是否有會員匯入 狀態"""
        response_data = self.memberImport.checkHasMemberImporting()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_04(self):
        """驗證 會員匯入 - 下載範本 狀態"""
        response_data = self.memberImport.downloadExample()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberImport_relatedApi_status_05(self):
        """驗證 會員匯入 - 上傳Excel 狀態"""
        upload_file = common_config.file_Path + 'test_data/memberImport.xlsx'  # 檔案
        mime_Type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'filebase': ('memberImport.xlsx', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.memberImport.getExcelSum(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉

    def test_MemberImport_relatedApi_status_06(self):
        """驗證 會員匯入 - 開始匯入 狀態"""
        upload_file = common_config.file_Path + 'test_data/memberImport.xlsx'  # 檔案
        mime_Type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'password': (None, master_config.Master_Password), 'isFilterBank': (None, 'true'),  # 有其他參數上傳用這種mode
                'importFile': ('memberImport.xlsx', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.memberImport.submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
