'''
@Created by loka
@Date : 2019/11/28
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from data_config import master_config
import time
from base.CommonMethod import UploadFile
from data_config.system_config import systemSetting


class MemberBatchBaseTest(unittest.TestCase):
    """會員批次 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.agentDetail = member_and_agent.AgentDetail(self.__http)
        self.memberBatch = member_and_agent.MemberBatch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getDiscountSettingId(self):
        response_data = self.agentDetail.getAllDiscountSettings({})
        for i in range(len(response_data[1])):
            if self.config.DiscountSetting_2_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def test_MemberBatch_relatedApi_status_01(self):
        """驗證 會員批次 - 匯入大量帳號 狀態"""
        self.upload = UploadFile('document/memberSearchBatch.xlsx', 'filename', 'memberSearchBatch.xlsx')
        data = self.upload.Upload_file()
        response_data = self.memberBatch.importAndGetLargeAccount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉

    def test_MemberBatch_relatedApi_status_02(self):
        """驗證 會員批次 - 會員批次頁面 狀態"""
        response_data = self.memberBatch.batch_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_03(self):
        """驗證 會員批次 - 清除樣板 狀態  """  # 不確定
        response_data = self.memberBatch.clearTemp({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_04(self):
        """驗證 會員批次 - 取得會員狀態 狀態"""
        response_data = self.memberBatch.getMemberStates({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_05(self):
        """驗證 會員批次 - 批次會員資料 狀態"""
        data = {'search': {'Account': self.config.test_Member_config()}, 'take': 3000, 'skip': 0,
                'isSuper': 'false'}
        response_data = self.memberBatch.getBatchData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_06(self):
        """驗證 會員批次 - 強制取回餘額寶 狀態"""
        data = {
            'search': {'Account': self.config.test_Member_config()},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'}
        }
        response_data = self.memberBatch.batchWithdrawYuebao(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_07(self):
        """驗證 會員批次 - 批次修改會員狀態 狀態"""
        data = {
            'search': {'Account': self.config.batch_Member_config()},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            "newState": "1"
        }
        response_data = self.memberBatch.batchUpdateMemberState(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_08(self):
        """驗證 會員批次 - 批次修改會員等級 狀態"""
        data = {
            'search': {'Account': self.config.batch_Member_config()},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'levelId': self.getDiscountSettingId()
        }
        response_data = self.memberBatch.batchUpdateMemberLevel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_09(self):
        """驗證 會員批次 - 批次時時歸水歸零 狀態"""
        data = {
            'search': {'Account': self.config.batch_Member_config()},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'password': master_config.Master_Password
        }
        response_data = self.memberBatch.anyTimeDiscountBatchReset(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_10(self):
        """驗證 會員批次 - 批次人工存入 狀態"""
        # Step1 先從人工存入取得 Token
        self.memberDeposit = member_and_agent.MemberDeposit(self.__http)
        depositToken = self.memberDeposit.deposit_token({})

        # Step2 使用批次人工存入
        data = {
            'search': {'Account': self.config.batch_Member_config()},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'depositParams': {
                'AuditType': 'None',
                'Type': 4,
                'DepositToken': depositToken[1],
                'Amount': 0.1,
                'Memo': '@0.1',
                'PortalMemo': '@0.1',
                'Password': master_config.Master_Password,
                'AmountString': '0.1',
                'TimeStamp': time.time()
            }
        }
        response_data = self.memberBatch.depositSubmitForMemberBatchDeposit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_11(self):
        """驗證 會員批次 - 批次修改會員標籤 狀態"""
        # Step1 批次修改會員標籤
        data = {
            'search': {'Account': self.config.batch_Member_config()},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'newTags': [self.config.batchTag_config()],
            'addTagIds': [],
            'deleteTagIds': []
        }
        response_data = self.memberBatch.batchAddOrDeleteMemberTags(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

        # Step2 驗證更改完畢後刪除標籤
        # 呼叫取得會員標籤 API 後取最後一筆資料
        self.memberTags = member_and_agent.MemberTags(self.__http)
        getMemberTagsData = self.memberTags.getTags({})
        for i in range(len(getMemberTagsData[1]['ReturnObject'])):
            if getMemberTagsData[1]['ReturnObject'][i]['Name'] == self.config.batchTag_config():
                self.getTagsId = getMemberTagsData[1]['ReturnObject'][i]['Id']

        data = {
            'search': {'MemberTagIds': self.getTagsId},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'newTags': [],
            'addTagIds': [],
            'deleteTagIds': [self.getTagsId]
        }
        self.memberBatch.batchAddOrDeleteMemberTags(data)

    def test_MemberBatch_relatedApi_status_12(self):
        """驗證 會員批次 - 批次更新簡訊驗證 狀態"""
        # Step1 批次修改簡訊驗證
        data = {"search": {'Account': self.config.batch_Member_config()}, "isSuper": 'false',
                "batchParam": {"isAll": 'true'},
                "isEnable": 'false'}
        response_data = self.memberBatch.batchUpdateMemberSmsValidation(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_13(self):
        """驗證 會員批次 - 批次更新電子郵件驗證 狀態"""
        # Step1 批次修改電子郵件驗證
        data = {"search": {'Account': self.config.batch_Member_config()}, "isSuper": 'false',
                "batchParam": {"isAll": 'true'},
                "isEnable": 'false'}
        response_data = self.memberBatch.batchUpdateMemberEmailValidation(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_14(self):
        """驗證 會員批次 - 批次停用二次驗證 狀態"""
        data = {"search": {'Account': self.config.batch_Member_config()}, "isSuper": 'false',
                "batchParam": {"isAll": 'true'},
                "isEnable": 'false'}
        response_data = self.memberBatch.batchDisableMemberGoogleAuthenticator(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_15(self):
        """驗證 會員批次 - 批次停用裝置驗證 狀態"""
        data = {"search": {'Account': self.config.batch_Member_config()}, "isSuper": 'false',
                "batchParam": {"isAll": 'true'},
                "isEnable": 'false'}
        response_data = self.memberBatch.batchDisableMemberGpkAuthenticator(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
