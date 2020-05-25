'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from data_config.system_config import systemSetting
from master_api import system_management
from master_api.account_login import User
from base.CommonMethod import UploadFile
from base.CommonMethod import system_config_Setting
from base.CommonMethod import Portal_test


class SiteMailBaseTest(unittest.TestCase):
    """ 站內信 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 參數設定
        # self.__http = HttpRequest()
        # self.user = User(self.__http)
        # self.siteMail = system_management.SiteMail(self.__http)
        # self.user.login()

    def tearDown(self):
        self.user.logout()

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.siteMail = system_management.SiteMail(cls.__http)
        cls.user.login()

    def test_SiteMail_relatedApi_status_01(self):
        """驗證 站內信 - 取得列表頁面"""
        SiteMailBaseTest.Master_login()  # 登入
        response_data = self.siteMail.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_02(self):
        """驗證 站內信 - 取得發送信件頁面"""
        SiteMailBaseTest.Master_login()  # 登入
        response_data = self.siteMail.send({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_03(self):
        """驗證 站內信(發送對象--單個會員)"""
        SiteMailBaseTest.Master_login()  # 登入
        data = {"SendMailType": 1,
                "MailRecievers": self.config.test_Member_config(),
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

    def test_SiteMail_relatedApi_status_04(self):
        """驗證 站內信(發送對象--多個會員)"""
        SiteMailBaseTest.Master_login()  # 登入
        data = {"SendMailType": 1,
                "MailRecievers": self.config.batch_Member_config(),
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

    def test_SiteMail_relatedApi_status_05(self):
        """驗證 站內信(發送對象--全站)"""
        SiteMailBaseTest.Master_login()  # 登入
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

    def test_SiteMail_relatedApi_status_06(self):
        """驗證 站內信(發送對象--批次-會員等級)"""
        self.system = system_config_Setting()
        Id = self.system.getMemberLevelId()
        SiteMailBaseTest.Master_login()  # 登入
        data = {"SendMailType": 2,
                "MailRecievers": " ",
                "BatchParam": {
                    "isAll": "true"
                },
                "SearchParam": {
                    "MemberLevelSettingIds": [Id]
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

    def test_SiteMail_relatedApi_status_07(self):
        """驗證 站內信(發送對象--匯入檔案)"""
        SiteMailBaseTest.Master_login()  # 登入
        self.upload = UploadFile('document/Email_Import.xlsx', 'excelFile', 'Email_Import.xlsx')
        data = self.upload.Upload_file()
        response_data = self.siteMail.uploadCustomExcel(data)
        self.upload.Close_file()  # 關閉
        ExcelPath = response_data[1]['ExcelPath']
        data = {"SendMailType": 5,
                "MailRecievers": " ",
                "BatchParam": " ",
                "SearchParam": " ",
                "SuperSearchRequest": " ",
                "ResendMailID": " ",
                "Subject": "測試站內信(發送對象--匯入檔案)",
                "MailBody": "<p>"
                            "%S0-%S1-%S2-%S3-%S4-%S5-%S6-%S7-%S8-%S9-%S10"
                            "</p>\n",
                "ExcelFilePath": ExcelPath}
        response_data = self.siteMail.sendMail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_08(self):
        """驗證 上傳檔案是否成功"""
        SiteMailBaseTest.Master_login()  # 登入
        self.upload = UploadFile('document/Email_Import.xlsx', 'excelFile', 'Email_Import.xlsx')
        data = self.upload.Upload_file()
        response_data = self.siteMail.uploadCustomExcel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉

    def test_SiteMail_relatedApi_status_09(self):
        """驗證 站內信(發送對象--回覆信件)"""
        # Step 1 取得寄件匣中的第一筆信件ID做回覆信件的依據
        data = {"Size": 30, "SearchParam": {"SentboxDate": "1"}, "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getSentboxList(data)
        getId = response_data[1]['SentboxMailList'][0]['Id']
        data = {"SendMailType": 3,
                "MailRecievers": " ",
                "BatchParam": " ",
                "SearchParam": " ",
                "SuperSearchRequest": " ",
                "ResendMailID": getId,
                "Subject": "測試站內信(發送對象--回覆信件)",
                "MailBody": "<p>"
                            "測試回覆站內信測試回覆站內信測試回覆站內信"
                            "測試回覆站內信測試回覆站內信測試回覆站內信"
                            "測試回覆站內信測試回覆站內信測試回覆站內信"
                            "測試回覆站內信測試回覆站內信測試回覆站內信"
                            "測試回覆站內信測試回覆站內信測試回覆站內信"
                            "測試回覆站內信測試回覆站內信測試回覆站內信"
                            "測試回覆站內信測試回覆站內信測試回覆站內信"
                            "</p>\n",
                "ExcelFilePath": " "}
        response_data = self.siteMail.sendMail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_10(self):
        """驗證 站內信 - 取得全站會員數量"""
        SiteMailBaseTest.Master_login()  # 登入
        response_data = self.siteMail.getAllSiteMemberCount({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_11(self):
        """驗證 站內信 - 刪除寄件匣"""
        # step 1 取得寄件匣Id
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Size": 30, "SearchParam": {"SentboxDate": "1"}, "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getSentboxList(data)
        getId = response_data[1]['SentboxMailList'][0]['Id']
        data = {"sentboxMailIds": [getId]}
        response_data = self.siteMail.deleteSentboxMails(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_12(self):
        """驗證 站內信 - 刪除收件匣"""
        # step 1 取得收件匣Id
        self.portal = Portal_test()
        self.portal.siteMail(self.config.test_Member_config(), self.config.test_Password_config())
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Size": 30, "SearchParam": {"InboxIsRead": 'true', "InboxIsUnRead": 'true', "InboxDate": "1"},
                "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getInboxList(data)
        getId = response_data[1]['InboxMailList'][0]['Id']
        data = {"inboxMailIds": [getId]}
        response_data = self.siteMail.deleteInboxMails(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_13(self):
        """驗證 站內信 - 取得信件詳細資料"""
        # step 1 取得收件匣Id
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Size": 30, "SearchParam": {"InboxIsRead": 'true', "InboxIsUnRead": 'true', "InboxDate": "1"},
                "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getInboxList(data)
        getId = response_data[1]['InboxMailList'][0]['Id']
        data = {"mailId": getId}
        response_data = self.siteMail.getMailDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_14(self):
        """驗證 站內信 - 收件匣未讀信件數"""
        SiteMailBaseTest.Master_login()  # 登入
        response_data = self.siteMail.getUnreadCount({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_15(self):
        """驗證 站內信 - 設定收件匣未讀為已讀信件"""
        # step 1 取得收件匣Id
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Size": 30, "SearchParam": {"InboxIsRead": 'true', "InboxIsUnRead": 'true', "InboxDate": "1"},
                "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getInboxList(data)
        getId = response_data[1]['InboxMailList'][0]['Id']
        data = {"inboxMailIds": [getId], "isRead": 'true'}  # 已讀
        response_data = self.siteMail.setInboxMailsAsReadOrUnread(data)
        status_code = response_data[0]
        data = {"inboxMailIds": [getId], "isRead": 'false'}  # 未讀
        self.siteMail.setInboxMailsAsReadOrUnread(data)
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_16(self):
        """驗證 站內信 - 取得收件匣列表"""
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Size": 30, "SearchParam": {"InboxIsRead": 'true', "InboxIsUnRead": 'true', "InboxDate": "1"},
                "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getInboxList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_17(self):
        """驗證 站內信 - 取得寄件匣列表"""
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Size": 30, "SearchParam": {"SentboxDate": "1"}, "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getSentboxList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_18(self):
        """驗證 站內信 - 以日為期間搜尋列表"""
        SiteMailBaseTest.Master_login()  # 登入
        response_data = self.siteMail.getSearchMailDateList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_SiteMail_relatedApi_status_19(self):
    #     """驗證 站內信 - 下載信件內容明細"""
    #     # 前置作業 : 先送一封匯入檔案的信件給會員
    #     self.upload = UploadFile('document/Email_Import.xlsx', 'excelFile', 'Email_Import.xlsx')
    #     data = self.upload.Upload_file()
    #     response_data = self.siteMail.uploadCustomExcel(data)
    #     self.upload.Close_file()
    #     ExcelPath = response_data[1]['ExcelPath']
    #     data = {"SendMailType": 5,
    #             "MailRecievers": " ",
    #             "BatchParam": " ",
    #             "SearchParam": " ",
    #             "SuperSearchRequest": " ",
    #             "ResendMailID": " ",
    #             "Subject": "測試站內信(發送對象--匯入檔案)",
    #             "MailBody": "<p>"
    #                         "%S0-%S1-%S2-%S3-%S4-%S5-%S6-%S7-%S8-%S9-%S10"
    #                         "</p>\n",
    #             "ExcelFilePath": ExcelPath}
    #     self.siteMail.sendMail(data)
    #     # step 1: 取得寄件匣信件Id
    #     data = {"Size": 30, "SearchParam": {"SentboxDate": "1"}, "SendDateOrderBy": 0, "LastId": 'null'}
    #     response_data = self.siteMail.getSentboxList(data)
    #     getId = response_data[1]['SentboxMailList'][0]['Id']
    #     data = {"siteMailId": getId}
    #     response_data = self.siteMail.downloadSiteMailExcelContent(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_20(self):
        """驗證 站內信 - 促銷匣列表"""
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Size": 30, "SearchParam": {"PromotionboxPublishDate": "1", "PromotionboxUnpublishDate": "1"},
                "PublishDateOrderBy": 0, "UnpublishDateOrderBy": 'null', "PageIndex": 'null'}
        response_data = self.siteMail.announcement_GetList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_21(self):
        """驗證 站內信 - 寄促銷信"""
        SiteMailBaseTest.Master_login()  # 登入
        data = {"Subject": "@QA_automation", "MailBody": "<p>12333333333</p>\n", "PublishDate": common_config.FirstDay,
                "UnpublishDate": common_config.EndDay}
        response_data = self.siteMail.announcement_SendMail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_22(self):
        """驗證 站內信 - 刪除促銷信"""
        SiteMailBaseTest.Master_login()  # 登入
        # step 1: 取得促銷匣信件Id
        data = {"Size": 30, "SearchParam": {"PromotionboxPublishDate": "1", "PromotionboxUnpublishDate": "1"},
                "PublishDateOrderBy": 0, "UnpublishDateOrderBy": 'null', "PageIndex": 'null'}
        response_data = self.siteMail.announcement_GetList(data)
        getId = response_data[1]['PromotionboxMailList'][0]['Id']
        data = {"Ids": [getId]}
        response_data = self.siteMail.announcement_Delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SiteMail_relatedApi_status_23(self):
        """驗證 站內信 - 取得收件人名單"""
        SiteMailBaseTest.Master_login()  # 登入
        # step 1 取得寄件匣Id
        data = {"Size": 30, "SearchParam": {"SentboxDate": "1"}, "SendDateOrderBy": 0, "LastId": 'null'}
        response_data = self.siteMail.getSentboxList(data)
        getId = response_data[1]['SentboxMailList'][0]['Id']
        data = {"mailId": getId, "size": 30, "lastId": ''}
        response_data = self.siteMail.getMailReceiverList(data)
        status_code = response_data[0]
        # print(response_data[1])
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
