'''
@Created by loka
@Date : 2019/11/28
'''
import unittest
import time
from data_config import common_config
from data_config import master_config
from base.CommonMethod import SetDelayTime
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api import system_management
from master_api.account_login import User
from data_config.system_config import systemSetting


class MemberDetailBaseTest(unittest.TestCase):
    """會員詳細資料 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberDetail = member_and_agent.MemberDetail(self.__http)
        self.searchMember = member_and_agent.MemberSearch(self.__http)
        self.deposit = member_and_agent.MemberDeposit(self.__http)
        self.withDraw = member_and_agent.MemberWithdraw(self.__http)
        self.AgentDetail = member_and_agent.AgentDetail(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    # 取得會員的 MemberId
    def GetMemberId(self):
        data = {'Account': self.config.MasterMember(),
                'connectionId': self.user.info()}
        response_data = self.searchMember.search(data)
        memberId = response_data[1]['PageData'][0]['Id']
        SetDelayTime()
        # time.sleep(3)
        return memberId

    def getDiscountSetting2(self):
        response_data = self.AgentDetail.getAllDiscountSettings({})
        for i in range(len(response_data[1])):
            if self.config.DiscountSetting_2_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def getMemberLevelId(self):
        response_data = self.AgentDetail.getAllMemberLevels({})
        for i in range(len(response_data[1])):
            if self.config.MemberLevelSetting_2_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    # 取得會員詳細資料
    def GetMemberDetail(self):
        data = {'connectionId': self.user.info(), 'account': self.config.MasterMember()}
        response_data = self.memberDetail.getDetail(data)
        memberDetail = response_data[1]
        return memberDetail

    def depositSubmitAudit(self):
        depositToken = self.deposit.deposit_token({})
        data = {
            'AccountsString': self.config.MasterMember(),
            'Type': 4,
            'AuditType': 'Deposit',
            'DepositToken': depositToken[1],
            'Audit': 0.1,
            'Amount': 0.1,
            'PortalMemo': '@autotest-Preliminary work-Audit',
            'Memo': '@autotest-Preliminary work-Audit',
            'Password': master_config.Master_Password,
            'AmountString': '0.1',
            "TimeStamp": time.time()
        }
        self.deposit.deposit_submit(data)

    def WithdrawSubmit(self):
        getmemberId = self.GetMemberId()
        data = {
            'id': getmemberId,
            'money': 0.1,
            'type': 4,
            'password': master_config.Master_Password,
            'isReal': 'false',
            '"memo': 'QA_Automation'
        }
        self.withDraw.withdraw_submit(data)

    def test_MemberDetail_relatedApi_status_01(self):
        """會員詳細資料 - 會員詳細資料頁面 狀態"""
        response_data = self.memberDetail.detail_page({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_02(self):
        """會員詳細資料 - 取得會員詳細資料 狀態"""
        data = {'connectionId': self.user.info(), 'account': self.config.test_Member_config()}
        response_data = self.memberDetail.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_03(self):
        """會員詳細資料 - 取得存提款資訊 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.getDepositWithdrawInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_04(self):
        """會員詳細資料 - 取得會員正在參與的活動 狀態"""
        getMemberId = self.GetMemberId()
        data = {'memberId': getMemberId}
        response_data = self.memberDetail.getMemberEventList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_05(self):
        """會員詳細資料 - 更新會員狀態 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId, 'state': 1}
        response_data = self.memberDetail.updateMemberState(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_06(self):
        """會員詳細資料 - 更新會員等級 狀態"""
        getMemberId = self.GetMemberId()
        data = {'memberId': getMemberId, 'levelId': self.getMemberLevelId()}
        response_data = self.memberDetail.updateMemberLevel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_07(self):
        """會員詳細資料 - 更新返水等級 狀態"""
        getMemberId = self.GetMemberId()
        data = {'memberId': getMemberId, 'settingId': self.getDiscountSetting2()}
        response_data = self.memberDetail.updateDiscountSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_08(self):
        """會員詳細資料 - 修改會員資料頁面 狀態"""
        response_data = self.memberDetail.modifyMemberInfo({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_09(self):
        """會員詳細資料 - 取得會員基本資料 狀態"""
        data = {'account': self.config.test_Member_config()}
        response_data = self.memberDetail.getMemberInfo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_10(self):
        """會員詳細資料 - 更新會員基本資料 狀態"""
        getMemberId = self.GetMemberId()
        data = {
            'Id': getMemberId,
            'Name': 'QATest',
            'Mobile': '+888' + common_config.now,
            'Sex': 'true',
            'Email': 'QA_Test@gmail.com',
            'Birthday': '2019/11/20',
            'IdNumber': 'a123456',
            'QQAccount': 'QAtest' + common_config.now
        }
        response_data = self.memberDetail.updateMemberInfo(data)
        status_code = response_data[0]
        getDetail = self.GetMemberDetail()  # 刷新會員資料
        validateData = getDetail['Member']['QQ']  # 驗證資料
        self.assertEqual(bool(status_code == common_config.Status_Code),
                         bool(validateData == 'QAtest' + common_config.now))

    def test_MemberDetail_relatedApi_status_11(self):
        """會員詳細資料 - 修改銀行資料頁面 狀態"""
        response_data = self.memberDetail.modifyBankAccount({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_12(self):
        """會員詳細資料 - 取得銀行資料 狀態"""
        data = {'account': self.config.MasterMember()}
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
            'memberAccount': self.config.MasterMember(),
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
        getDetail = self.GetMemberDetail()  # 刷新會員資料
        validateData = getDetail['Member']['BankAccount']['Account']  # 驗證資料
        self.assertEqual(bool(status_code == common_config.Status_Code),
                         bool(validateData == common_config.now))

    def test_MemberDetail_relatedApi_status_15(self):
        """會員詳細資料 - 取得銀行修改紀錄 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.getBankHistories(data)
        status_code = response_data[0]
        getDetail = self.GetMemberDetail()  # 刷新會員資料
        validateData = getDetail['Member']['AlipayAccount']['Account']  # 驗證資料
        self.assertEqual(bool(status_code == common_config.Status_Code),
                         bool(validateData == 'QA_Test' + common_config.now))

    def test_MemberDetail_relatedApi_status_16(self):
        """會員詳細資料 - 取得支付寶修改紀錄 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.getAlipayAccountHistories(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_17(self):
        """會員詳細資料 - 更新區域驗證限制 狀態"""
        getMemberId = self.GetMemberId()
        data = {'memberId': getMemberId, 'enable': 'true'}
        response_data = self.memberDetail.updateMemberIsNeedRegionValidate(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        data = {'memberId': getMemberId, 'enable': 'false'}
        self.memberDetail.updateMemberIsNeedRegionValidate(data)

    def test_MemberDetail_relatedApi_status_18(self):
        """會員詳細資料 - 手機簡訊驗證 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId, 'status': 'false'}
        response_data = self.memberDetail.updateMemberSmsLoginValidationEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_19(self):
        """會員詳細資料 - 稽核頁面 狀態"""
        response_data = self.memberDetail.audit({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_20(self):
        """會員詳細資料 -取得稽核詳細資料  狀態"""
        data = {'account': self.config.MasterMember()}
        response_data = self.memberDetail.getAuditDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_21(self):
        """會員詳細資料 -修改稽核頁面  狀態"""
        response_data = self.memberDetail.auditModify({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_22(self):
        """會員詳細資料 -取得會員稽核列表資料 狀態"""
        data = {'account': self.config.MasterMember()}
        response_data = self.memberDetail.getDepositList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        return response_data

    def test_MemberDetail_relatedApi_status_23(self):
        """會員詳細資料 -更新稽核資料 狀態"""
        self.depositSubmitAudit()
        data = {'account': self.config.MasterMember()}
        getMemberId = self.GetMemberId()
        depositData = self.memberDetail.getDepositList(data)
        amountAudit = int(time.time())  # 修改金額為現在時間戳
        depositData[1]['Data'][0]['AuditAmount'] = amountAudit
        updateData = depositData
        data = {"id": getMemberId, "updateParams": updateData[1]['Data']}
        response_data = self.memberDetail.updateDepositAudit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.WithdrawSubmit()  # 提出

    def test_MemberDetail_relatedApi_status_24(self):
        """會員詳細資料 -清除稽核 狀態"""
        data = {'account': self.config.MasterMember()}
        response_data = self.memberDetail.clearAudit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_25(self):
        """會員詳細資料 -重設密碼 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.resetPassword(data)
        # print(response_data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_26(self):
        """會員詳細資料 -娛樂城錢包全取回 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.allWalletBackMember(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_27(self):
        """會員詳細資料 -娛樂城錢包全更新 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.allWalletUpdateMember(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_28(self):
        """會員詳細資料 -重設取款密碼 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.resetMoneyPassword(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_29(self):
        """會員詳細資料 -更新備註 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId, 'memo': 'QA_automation'}
        response_data = self.memberDetail.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_30(self):
        """會員詳細資料 -更換代理商頁面 狀態"""
        response_data = self.memberDetail.changeAgent({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_31(self):
        """會員詳細資料 -取得代理 狀態"""
        data = {'account': self.config.MasterMember()}
        response_data = self.memberDetail.getAgents(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_32(self):
        """會員詳細資料 -更換代理 狀態"""
        data = {
            'memberAccount': self.config.MasterMember(),
            'newAgentAccount': self.config.agentLv4()
        }
        response_data = self.memberDetail.changeAgentSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_33(self):
        """會員詳細資料 -會員歷史紀錄頁面 狀態"""
        response_data = self.memberDetail.history({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_34(self):
        """會員詳細資料 -會員歷史紀錄 狀態"""
        data = {'account': self.config.MasterMember()}
        response_data = self.memberDetail.historyInit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_35(self):
        """會員詳細資料 -讀取會員歷史紀錄 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId, 'take': 100, 'skip': 0, 'query': {}}
        response_data = self.memberDetail.loadHistory(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_36(self):
        """會員詳細資料 -讀取會員修改歷史紀錄 狀態"""
        getMemberId = self.GetMemberId()
        data = {'id': getMemberId}
        response_data = self.memberDetail.getMemberInfoHistories(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relateApi_status_37(self):
        """會員詳細資料 - 更新會員基本資料 - 真實姓名混入非中英文 狀態"""
        getMemberId = self.GetMemberId()
        data = {
            'Id': getMemberId,
            'Name': 'QATest' + common_config.now,
            'Mobile': '+888' + common_config.now,
            'Sex': 'true',
            'Email': 'QA_Test@gmail.com',
            'Birthday': '2019/11/20',
            'IdNumber': 'a123456',
            'QQAccount': 'dddd'
        }
        response_data = self.memberDetail.updateMemberInfo(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '真实姓名只接受中英文字与全、半型英文句号')

    def test_MemberDetail_relatedApi_status_38(self):
        """會員詳細資料 - 解除暫停登入狀態"""
        getMemberId = self.GetMemberId()
        data = {"memberId": getMemberId}
        response_data = self.memberDetail.UnsuspendLogin(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberDetail_relatedApi_status_39(self):
        """驗證 會員詳細資料 - 解除暫停登入狀態 - 開 狀態"""
        data = {"memberId": self.GetMemberId(),
                "status": 'true'
                }
        try:
            response_data = self.memberDetail.UpdateMaliciouslyLoginEnable(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)
        except:
            print("發生錯誤：" + status_code[1])

    def test_MemberDetail_relatedApi_status_40(self):
        """驗證 會員詳細資料 - 解除暫停登入狀態 - 關 狀態"""
        data = {"memberId": self.GetMemberId(),
                "status": 'false'
                }
        response_data = self.memberDetail.UpdateMaliciouslyLoginEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
