'''
@Created by loka
@Date : 2020/01/08
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from base.CommonMethod import PortalExecution
from base.CommonMethod import SetDelayTime
from data_config.system_config import systemSetting


class autoCreateMemberTag(unittest.TestCase):
    """自動新增系统侦测-恶意注册標籤-會員註冊在60秒內註冊完成+建立銀行帳號 狀態"""

    # 驗證步驟
    # step 1:會員註冊
    # step 2:馬上登入然後去線上取款設定銀行帳戶
    # step 3:驗證是否有系统侦测-恶意注册的標籤自動新增在該會員詳細資料
    # step 4:從會員歷史紀錄中驗證是否有這筆紀錄+取得該會員的標籤

    def setUp(self):
        self.config = systemSetting()  # 系統參數

    def tearDown(self):
        self.user.logout()

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.memberCreate = member_and_agent.MemberCreate(cls.__http)
        cls.user.login()
        cls.memberVerify = member_and_agent.MemberVerifyPage(cls.__http)  # 會員註冊審核
        cls.searchMember = member_and_agent.MemberSearch(cls.__http)  # 會員搜尋
        cls.memberDetail = member_and_agent.MemberDetail(cls.__http)  # 會員詳細資料
        cls.memberTags = member_and_agent.MemberTags(cls.__http)  # 會員標籤

    def test_autoCreateMemberTag_01(self):
        """驗證 由Portal註冊->經過會員註冊審核->再登入"""
        # Step1: Portal端註冊
        validateTags = ''
        account = 'QA_tags' + common_config.now
        self.portal = PortalExecution()
        self.portal.Register(account)
        autoCreateMemberTag.Master_login()  # 登入
        listData = {'take': 100, 'search': {}}
        getData = self.memberVerify.getList(listData)
        Id = getData[1]['Data'][0]['Id']
        verifyAccount = getData[1]['Data'][0]['SubmitAccount']
        # Step2:會員註冊審核
        data = {'Id': Id, 'verifyAccount': verifyAccount}  # 審核通過該會員
        # Step3:會員登入建立銀行帳戶
        self.memberVerify.approve(data)
        self.portal_setBank = PortalExecution()
        self.portal_setBank.SetBankAccount(account, 'a123456')
        SetDelayTime()
        # step 4:從會員歷史紀錄中驗證是否有這筆紀錄+取得該會員的標籤
        autoCreateMemberTag.Master_login()  # 登入
        data = {"account": account}
        getId = self.memberDetail.historyInit(data)
        Id = getId[1]['MemberId']
        data = {"id": Id, "take": 100, "skip": 0, "query": {}}
        response_data = self.memberDetail.loadHistory(data)
        memberHistory = response_data[1][0]['Content']
        data = {'account': account}
        response_data = self.memberTags.getMemberTags(data)  # 取得該會員的標籤
        memberTags = response_data[1]['ReturnObject']
        for i in range(len(memberTags)):
            if memberTags[i]['Name'] == '系统侦测-恶意注册':
                validateTags = 'True'
                break
            validateTags = 'False'
        validateData = '新增标签【系统侦测-恶意注册】'
        self.assertEqual(str(bool(memberHistory == validateData)), validateTags, '該會員的標籤有問題請查看')

    def test_autoCreateMemberTag_02(self):
        """驗證 Master新增會員->修改會員密碼->再登入"""
        validateTags = ''
        account = "QATags" + common_config.now
        agent = self.config.agentLv4()
        autoCreateMemberTag.Master_login()  # 登入
        data = {'Account': account,
                'Agent': agent,
                'memo': '@autoMemberTags-fromPortal'}
        self.memberCreate.createSubmit(data)
        data = {'Account': account,
                'connectionId': self.user.info()}
        response_data = self.searchMember.search(data)
        memberId = response_data[1]['PageData'][0]['Id']
        data = {'id': memberId}
        self.memberDetail.resetMoneyPassword(data)
        self.portal = PortalExecution()
        # Step3:會員登入建立銀行帳戶
        self.portal.ChangePassword(account, '123456')
        self.portal.SetBankAccount(account, 'a123456')
        # step 4:從會員歷史紀錄中驗證是否有這筆紀錄+取得該會員的標籤
        autoCreateMemberTag.Master_login()  # 登入
        data = {"account": account}
        getId = self.memberDetail.historyInit(data)
        Id = getId[1]['MemberId']
        data = {"id": Id, "take": 100, "skip": 0, "query": {}}
        response_data = self.memberDetail.loadHistory(data)
        memberHistory = response_data[1][0]['Content']
        data = {'account': account}
        response_data = self.memberTags.getMemberTags(data)
        memberTags = response_data[1]['ReturnObject']
        for i in range(len(memberTags)):
            if memberTags[i]['Name'] == '系统侦测-恶意注册':
                validateTags = 'True'
                break
            validateTags = 'False'
        validateData = '新增标签【系统侦测-恶意注册】'
        self.assertEqual(str(bool(memberHistory == validateData)), validateTags, '該會員的標籤有問題請查看')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
