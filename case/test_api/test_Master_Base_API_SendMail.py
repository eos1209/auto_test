'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import system_management
from master_api.account_login import User


class SiteMailBaseTest(unittest.TestCase):
    """ 站內信 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.siteMail = system_management.SiteMail(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_Statistics_relatedApi_status_01(self):
        """驗證 站內信 - 取得列表頁面"""
        response_data = self.siteMail.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_02(self):
        """驗證 站內信 - 取得發送信件頁面"""
        response_data = self.siteMail.send({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_03(self):
        """驗證 站內信(發送對象--單個會員)"""
        data = {"SendMailType": 1,
                "MailRecievers": "Vicky",
                "BatchParam": " ",
                "SearchParam": " ",
                "SuperSearchRequest": " ",
                "ResendMailID": " ",
                "Subject": "測試站內信(測試數量)",
                "MailBody": "<p>測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信測試批次站內信</p>\n",
                "ExcelFilePath": " "}
        response_data = self.siteMail.sendMail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_04(self):
        """驗證 站內信(發送對象--多個會員)"""
        data = {"SendMailType": 1,
                "MailRecievers": "hsiang, hsiang01, hsiang02, hsiang03,",
                "BatchParam": " ",
                "SearchParam": " ",
                "SuperSearchRequest": " ",
                "ResendMailID": " ",
                "Subject": "測試站內信(發送對象--多個會員)",
                "MailBody": "<p>"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "</p>\n",
                "ExcelFilePath": " "}
        response_data = self.siteMail.sendMail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_05(self):
        """驗證 站內信(發送對象--全站)"""
        data = {"SendMailType": 4,
                "MailRecievers": " ",
                "BatchParam": " ",
                "SearchParam": " ",
                "SuperSearchRequest": " ",
                "ResendMailID": " ",
                "Subject": "測試站內信(發送對象--全站)",
                "MailBody": "<p>"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "</p>\n",
                "ExcelFilePath": " "}
        response_data = self.siteMail.sendMail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_Statistics_relatedApi_status_06(self):
        """驗證 站內信(發送對象--批次-會員等級)"""
        data = {"SendMailType": 2,
                "MailRecievers": " ",
                "BatchParam": {
                    "isAll": "true"
                },
                "SearchParam": {
                    "MemberLevelSettingIds": ["14"]
                },
                "SuperSearchRequest": " ",
                "IsSuper": "false",
                "ResendMailID": " ",
                "Subject": "測試批次站內信(小量)",
                "MailBody": "<p>"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信測試批次站內信"
                            "測試批次站內信測試批次站內信"
                            "</p>\n",
                "ExcelFilePath": " "}
        response_data = self.siteMail.sendMail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_Statistics_relatedApi_status_07(self):
    #     """驗證 站內信(發送對象--匯入檔案)"""
    #     # data = 'D:/GM Automation/gpk.api.test/dataConfig/import.xlsx'
    #     # response_data = self.siteMail.uploadCustomExcel(dat)
    #     files = {"file": open("D:/GM Automation/gpk.api.test/dataConfig/import.xlsx", "rb")}
    #     # r = requests.post("http://master.ky1188.net/SiteMail/UploadCustomExcel", files=files)
    #     # response_json = r.content
    #     # print(response_json)
    #     response_data = self.siteMail.uploadCustomExcel(files)
    #     status_code = response_data[0]
    #     print(status_code)

    # data = {"SendMailType": 5,
    #         "MailRecievers": " ",
    #         "BatchParam": " ",
    #         "SearchParam": " ",
    #         "SuperSearchRequest": " ",
    #         "ResendMailID": " ",
    #         "Subject": "發送對象--汇入档案",
    #         "MailBody": "<p>親愛的%S0</p>\n\n<p>%S1</p>\n\n<p>即刻起 %S2 都有%S3 的 %S4</p>\n\n<p>%S5 一起 %S6 喔!</p>\n\n<p>%S7 活動 %S8</p>\n\n<p>滿%S9</p>\n\n<p>祝各位%S10</p>\n",
    #         "ExcelFilePath": "/GeneratedFiles/BatchSiteMail_20181226100456.xlsx"}
    # response_data = self.siteMail.sendMail(data)
    # status_code = response_data[0]
    # self.assertEqual(status_code, config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
