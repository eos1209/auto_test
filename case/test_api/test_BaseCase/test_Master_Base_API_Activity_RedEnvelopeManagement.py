'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from master_api.account_login import User
from master_api.system_management import ActivityManagement
from base.HTMLTestReportCN import HTMLTestRunner
from base.CommonMethod import UploadFile
from base.httpRequest import HttpRequest
from data_config import common_config
from data_config.system_config import systemSetting
from datetime import datetime, timedelta
from data_config import master_config
from base.CommonMethod import SetDelayTime
from base.CommonMethod import Portal_test


class RedEnvelopeManagementBaseTest(unittest.TestCase):
    """ 红包派送 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 參數設定
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.redEnvelopeManagement = ActivityManagement.RedEnvelopeManagement(self.__http)
        self.user.login()
        self.portal = Portal_test()

    def tearDown(self):
        self.user.logout()

    def red_RedEnvelope_create(self):  # 建立紅包活動
        self.upload = UploadFile('document/red.xlsx',  # 檔案路徑
                                 'fileBase',  # 上傳欄位
                                 'red.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        startTime = (datetime.now() + timedelta(hours = -11.99)).strftime("%Y/%m/%d %H:%M:%S")  # 開始時間-美東時間
        endTime = (datetime.now() + timedelta(hours = +11)).strftime("%Y/%m/%d %H:%M:%S")  # 結束時間 - 後天
        data = {'Name': (None, 'QA_Revoke_redEnvelope'),
                'Password': (None, master_config.Master_Password),
                'StartTime': (None, startTime),  # 有其他參數上傳用這種mode
                'EndTime': (None, endTime), 'Description': (None, 'QA_automation'),
                self.upload.upload_name: (
                    self.upload.filename, self.upload.open_file, self.upload.file_type, {'Expires': '0'})}
        self.redEnvelopeManagement.addRedEnvelope(data)

    def getId(self):
        data = {"take": 100,
                "skip": 0,
                "search": {},
                'connectionId': self.user.info()
                }
        response_data = self.redEnvelopeManagement.getList(data)
        return response_data[1]['ReturnObject'][0]['Id']

    def end_redEnvelope(self):  # 先沖銷紅包
        data = {"take": 100,
                "skip": 0,
                "search": {},
                'connectionId': self.user.info()}
        response_data = self.redEnvelopeManagement.getList(data)
        for i in range(len(response_data[1])):
            if response_data[1]['ReturnObject'][i]['Name'] == 'QA_automation_redEnvelope' and \
                    response_data[1]['ReturnObject'][i]['Status'] == 2:
                data = {"Id": response_data[1]['ReturnObject'][i]['Id']}
                self.redEnvelopeManagement.suspendActivity(data)

    def test_RedEnvelopeManagement_Get_List_Data(self):
        """驗證 红包派送 - 取得列表資料"""
        data = {"take": 100,
                "skip": 0,
                "search": {},
                'connectionId': self.user.info()}
        response_data = self.redEnvelopeManagement.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_02(self):
        """驗證 红包派送 - 取得狀態資料 """
        response_data = self.redEnvelopeManagement.getAllStatus({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_03(self):
        """驗證 红包派送 - 詳細資料"""
        Id = self.getId()
        data = {"id": Id}
        response_data = self.redEnvelopeManagement.get_detail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_04(self):
        """ 紅包派送 - 紅包匯入 狀態 2019/12/03"""
        # 1205
        self.upload = UploadFile('document/red.xlsx',  # 檔案路徑
                                 'fileBase',  # 上傳欄位
                                 'red.xlsx'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        startTime = (datetime.now() + timedelta(hours = -11.99)).strftime("%Y/%m/%d %H:%M:%S")  # 開始時間-美東時間
        endTime = (datetime.now() + timedelta(hours = +11)).strftime("%Y/%m/%d %H:%M:%S")  # 結束時間 - 後天
        data = {'Name': (None, 'QA_automation_redEnvelope'),
                'Password': (None, master_config.Master_Password),
                'StartTime': (None, startTime),  # 有其他參數上傳用這種mode
                'EndTime': (None, endTime), 'Description': (None, 'QA_automation'),
                self.upload.upload_name: (
                    self.upload.filename, self.upload.open_file, self.upload.file_type, {'Expires': '0'})}
        response_data = self.redEnvelopeManagement.addRedEnvelope(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉

    def test_RedEnvelopeManagement_relatedApi_status_05(self):
        """紅包派送 - 更新備註 狀態 2020/02/21"""
        Id = self.getId()
        data = {"Id": Id, "NewValue": "@QA_automation_Import-redEnvelope"}
        response_data = self.redEnvelopeManagement.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_06(self):
        """紅包派送 - 立即中止紅包 狀態 2020/02/21"""
        Id = self.getId()
        data = {"Id": Id}
        SetDelayTime()
        response_data = self.redEnvelopeManagement.suspendActivity(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_RedEnvelopeManagement_relatedApi_status_07(self):
        """紅包派送 - 沖銷紅包 狀態 """
        # step 1:先沖銷自動化測試產生的紅包
        self.end_redEnvelope()
        # step 2:匯入紅包->手機領取->驗證紅包
        self.red_RedEnvelope_create()  # 匯入紅包
        SetDelayTime()
        Id = self.getId()  # 取得ID
        response_result = self.portal.RedEnvelope_Received(self.config.test_Member_config(),
                                                           self.config.test_Password_config(), Id)  # 領取紅包
        SetDelayTime()
        if response_result:
            data = {"Id": Id, "RevokePortalMemo": "@QA_automation-RevokeRedEnvelope",
                    "Password": master_config.Master_Password}
            self.redEnvelopeManagement.revoke(data)
            data = {"id": Id}
            response_data = self.redEnvelopeManagement.get_detail(data)
            revoke_member_count = 1  # 預計會員沖銷人數1人
            self.assertEqual(revoke_member_count, response_data[1]['ReturnObject']['MemberCount'], '會員領錯紅包，請先將紅包都結束')
        elif response_result == '會員沒有領到紅包':
            self.assertNotEqual(response_result, '會員沒有領到紅包', '會員沒有領到紅包')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
