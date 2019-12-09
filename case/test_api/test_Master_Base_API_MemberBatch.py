'''
@Created by loka
@Date : 2019/11/28
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import memeber_and_agent
from master_api.account_login import User
from data_config import master_config
import time


class MemberBatchBaseTest(unittest.TestCase):
    """會員批次 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberBatch = memeber_and_agent.MemberBatch(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberBatch_relatedApi_status_01(self):
        """驗證 會員批次 - 匯入大量帳號 狀態"""
        upload_file = common_config.file_Path + 'test_data/memberSearchBatch.xlsx'  # 檔案
        mime_Type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳的類型
        open_file = open(upload_file, 'rb')  # 打開檔案
        data = {'filename': ('memberSearchBatch.xlsx', open_file, mime_Type, {'Expires': '0'})}
        response_data = self.memberBatch.importAndGetLargeAccount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        open_file.close()  # 關閉

    def test_MemberBatch_relatedApi_status_02(self):
        """驗證 會員批次 - 會員批次頁面 狀態"""
        response_data = self.memberBatch.batch_page()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_03(self):
        """驗證 會員批次 - 清除樣板 狀態  """  # 不確定
        response_data = self.memberBatch.clearTemp()
        # print(response_data)
        self.assertEqual(response_data, None)

    def test_MemberBatch_relatedApi_status_04(self):
        """驗證 會員批次 - 取得會員狀態 狀態"""
        response_data = self.memberBatch.getMemberStates()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_05(self):
        """驗證 會員批次 - 批次會員資料 狀態"""
        data = {'search': {'Account': master_config.Account}, 'take': 3000, 'skip': 0,
                'isSuper': 'false'}
        response_data = self.memberBatch.getBatchData(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_06(self):
        """驗證 會員批次 - 強制取回餘額寶 狀態"""
        data = {
            'search': {'Account': master_config.Account},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'}
        }
        response_data = self.memberBatch.batchWithdrawYuebao(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_07(self):
        """驗證 會員批次 - 批次修改會員狀態 狀態"""
        data = {
            'search': {'Account': master_config.batchAccount},
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
            'search': {'Account': master_config.batchAccount},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'levelId': 21
        }
        response_data = self.memberBatch.batchUpdateMemberLevel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_09(self):
        """驗證 會員批次 - 批次時時歸水歸零 狀態"""
        data = {
            'search': {'Account': master_config.batchAccount},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'password': master_config.Master_Password
        }
        response_data = self.memberBatch.anyTimeDiscountBatchReset(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberBatch_relatedApi_status_10(self):
        """驗證 會員批次 - 批次人工存入 狀態"""
        self.memberDeposit = memeber_and_agent.MemberDeposit(self.__http)
        depositToken = self.memberDeposit.deposit_token()
        data = {
            'search': {'Account': master_config.batchAccount},
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
        self.memberTags = memeber_and_agent.MemberTags(self.__http)
        data = {
            'search': {'Account': master_config.batchAccount},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'newTags': ['QA_batchAutomation'],
            'addTagIds': [],
            'deleteTagIds': []
        }
        response_data = self.memberBatch.batchAddOrDeleteMemberTags(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        # 刪除標籤
        getData = self.memberTags.getTags()
        dataLength = len(getData[1]['ReturnObject']) - 1  # 取得最後一筆資料
        memberTagId = dataLength
        data = {
            'search': {'MemberTagIds': getData[1]['ReturnObject'][memberTagId]['Id']},
            'isSuper': 'false',
            'batchParam': {'isAll': 'true'},
            'newTags': [],
            'addTagIds': [],
            'deleteTagIds': [getData[1]['ReturnObject'][memberTagId]['Id']]
        }
        self.memberBatch.batchAddOrDeleteMemberTags(data)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
