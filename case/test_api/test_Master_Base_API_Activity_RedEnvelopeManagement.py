'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from master_api.account_login import User
from master_api.system_management import ActivityManagement
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from datetime import datetime, timedelta
from data_config import master_config


class RedEnvelopeManagementBaseTest(unittest.TestCase):
    """ 红包派送 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.redEnvelopeManagement = ActivityManagement.RedEnvelopeManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_RedEnvelopeManagement_relatedApi_status_01(self):
        """驗證 红包派送 - 取得列表資料"""
        data = {"take": 100, "skip": 0, "search": {}}
        response_data = self.redEnvelopeManagement.get_list(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_02(self):
        """驗證 红包派送 - 詳細資料"""
        data = {"id": 255}
        response_data = self.redEnvelopeManagement.get_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_03(self):
        """ 紅包派送 - 紅包匯入 狀態 2019/12/03"""
        # 1205
        startTime = (datetime.now() + timedelta(hours=-12)).strftime("%Y/%m/%d %H:%M:%S")  # 開始時間-美東時間
        endTime = (datetime.now() + timedelta(hours=+11)).strftime("%Y/%m/%d %H:%M:%S")  # 結束時間 - 後天
        upload_file = common_config.file_Path + 'testData/red.xlsx'  # 檔案
        mime_Type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'Name': (None, 'QA_automation_redEnvelope'), 'Password': (None, master_config.Master_Password),
                'StartTime': (None, startTime),  # 有其他參數上傳用這種mode
                'EndTime': (None, endTime), 'Description': (None, 'QA_automation'),
                'fileBase': ('red.xlsx', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.redEnvelopeManagement.addRedEnvelope(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
