'''
@Created by loka
@Date : 2019/11/28
'''
import unittest
from data_config import common_config
from data_config import master_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import memeber_and_agent
from master_api.account_login import User


class MemberDetailBaseTest(unittest.TestCase):
    """會員詳細資料 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberDetail = memeber_and_agent.MemberDetail(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_MemberDetail_relatedApi_status_01(self):
        """會員詳細資料 - 會員詳細資料頁面 狀態"""
        response_data = self.memberDetail.detail_page()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_02(self):
        """會員詳細資料 - 取得會員詳細資料 狀態"""
        data = {'connectionId': self.user.info(), 'account': master_config.Account}
        response_data = self.memberDetail.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_03(self):
        """會員詳細資料 - 取得存提款資訊 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.getDepositWithdrawInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_04(self):
        """會員詳細資料 - 取得會員正在參與的活動 狀態"""
        data = {'memberId': master_config.Account_Id}
        response_data = self.memberDetail.getMemberEventList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_05(self):
        """會員詳細資料 - 更新會員狀態 狀態"""
        data = {'id': master_config.Account_Id, 'state': 1}
        response_data = self.memberDetail.updateMemberState(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_06(self):
        """會員詳細資料 - 更新會員等級 狀態"""
        data = {'memberId': master_config.Account_Id, 'levelId': 12}
        response_data = self.memberDetail.updateMemberLevel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_07(self):
        """會員詳細資料 - 更新返水等級 狀態"""
        data = {'memberId': master_config.Account_Id, 'settingId': 6}
        response_data = self.memberDetail.updateDiscountSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_08(self):
        """會員詳細資料 - 修改會員資料頁面 狀態"""
        response_data = self.memberDetail.modifyMemberInfo()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_09(self):
        """會員詳細資料 - 取得會員基本資料 狀態"""
        data = {'account': master_config.Account}
        response_data = self.memberDetail.getMemberInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_10(self):
        """會員詳細資料 - 更新會員基本資料 狀態"""
        data = {
            'Id': master_config.Account_Id,
            'Name': 'QA_Test' + common_config.now,
            'Mobile': '+888' + common_config.now,
            'Sex': 'true',
            'Email': 'QA_Test@gmail.com',
            'Birthday': '2019/11/20',
            'IdNumber': 'a123456',
            'QQAccount': 'dddd'
        }
        response_data = self.memberDetail.updateMemberInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_11(self):
        """會員詳細資料 - 修改銀行資料頁面 狀態"""
        response_data = self.memberDetail.modifyBankAccount()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_12(self):
        """會員詳細資料 - 取得銀行資料 狀態"""
        data = {'account': master_config.Account}
        response_data = self.memberDetail.getBankAccount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_13(self):
        """會員詳細資料 - 檢查銀行帳戶 狀態"""
        data = {'account': common_config.now}
        response_data = self.memberDetail.checkBankAccount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_14(self):
        """會員詳細資料 - 更新銀行資料 狀態"""
        data = {
            'memberAccount': master_config.Account,
            'GroupBankId': 1,
            'Province': 'fffff',
            'City': 'fffff',
            'Account': common_config.now,
            'Memo': common_config.now,
            'AlipayAccount': 'QA_Test' + common_config.now,
            'AlipayNickName': common_config.now,
            'AlipayMemo': 'QA_automation' + common_config.now,
            'ForceUpdate': 'false'
        }
        response_data = self.memberDetail.updateBankAccount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_15(self):
        """會員詳細資料 - 取得銀行修改紀錄 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.getBankHistories(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_16(self):
        """會員詳細資料 - 取得支付寶修改紀錄 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.getAlipayAccountHistories(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_17(self):
        """會員詳細資料 - 更新區域驗證限制 狀態"""
        data = {'id': master_config.Account_Id, 'allow': 'false'}
        response_data = self.memberDetail.updateMemberLoginEveryWhere(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_18(self):
        """會員詳細資料 - 手機簡訊驗證 狀態"""
        data = {'id': master_config.Account_Id, 'status': 'false'}
        response_data = self.memberDetail.updateMemberSmsLoginValidationEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_19(self):
        """會員詳細資料 - 稽核頁面 狀態"""
        response_data = self.memberDetail.audit()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_20(self):
        """會員詳細資料 -取得稽核詳細資料  狀態"""
        data = {'account': master_config.Account}
        response_data = self.memberDetail.getAuditDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_21(self):
        """會員詳細資料 -修改稽核頁面  狀態"""
        response_data = self.memberDetail.auditModify()
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_22(self):
        """會員詳細資料 -取得會員稽核資料 狀態"""
        data = {'account': master_config.Account}
        response_data = self.memberDetail.getDepositList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_MemberDetail_relatedApi_status_23(self):
    #     """會員詳細資料 -更新稽核資料 狀態"""

    def test_MemberDetail_relatedApi_status_24(self):
        """會員詳細資料 -清除稽核 狀態"""
        data = {'account': master_config.Account}
        response_data = self.memberDetail.clearAudit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_25(self):
        """會員詳細資料 -重設密碼 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.resetPassword(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_26(self):
        """會員詳細資料 -娛樂城錢包全取回 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.allWalletBackMember(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_27(self):
        """會員詳細資料 -娛樂城錢包全取回 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.allWalletBackMember(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_28(self):
        """會員詳細資料 -娛樂城錢包全取回 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.allWalletUpdateMember(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_29(self):
        """會員詳細資料 -重設取款密碼 狀態"""
        data = {'id': master_config.Account_Id}
        response_data = self.memberDetail.resetMoneyPassword(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_30(self):
        """會員詳細資料 -更新備註 狀態"""
        data = {'id': master_config.Account_Id,'memo':common_config.now}
        response_data = self.memberDetail.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)