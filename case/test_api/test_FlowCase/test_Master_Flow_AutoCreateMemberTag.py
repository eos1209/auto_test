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
from data_config import master_config
from base.CommonMethod import PortalExecution
from base.CommonMethod import SetDelayTime


class autoCreateMemberTag(unittest.TestCase):
    """自動新增系统侦测-恶意注册標籤-會員註冊在60秒內註冊完成+建立銀行帳號 狀態"""

    # 驗證步驟
    # step 1:會員註冊
    # step 2:馬上登入然後去線上取款設定銀行帳戶
    # step 3:驗證是否有系统侦测-恶意注册的標籤自動新增在該會員詳細資料

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberCreate = member_and_agent.MemberCreate(self.__http)
        self.user.login()
        self.memberVerify = member_and_agent.MemberVerifyPage(self.__http)  # 會員註冊審核
        self.searchMember = member_and_agent.MemberSearch(self.__http)  # 會員搜尋
        self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細資料

    def tearDown(self):
        self.user.logout()

    def test_autoCreateMemberTag_01(self):
        """驗證 由Portal註冊->經過會員註冊審核->再登入"""
        # Step1: Portal端註冊
        account = 'QA_tags' + common_config.now
        self.portal = PortalExecution()
        self.portal.Register(account)
        listData = {'take': 100, 'search': {}}
        getData = self.memberVerify.getList(listData)
        Id = getData[1]['Data'][0]['Id']
        verifyAccount = getData[1]['Data'][0]['SubmitAccount']
        # Step2:會員註冊審核
        data = {'Id': Id, 'verifyAccount': verifyAccount}  # 審核通過該會員
        # Step3:會員登入建立銀行帳戶
        self.memberVerify.approve(data)
        self.portal.SetBankAccount(account, 'a123456')
        SetDelayTime()
        data = {"MemberTagIds": "541", "connectionId": self.user.info()}
        response_data = self.searchMember.search(data)
        validateData = response_data[1]['PageData'][0]['Account']
        self.assertEqual(account, validateData)

    def test_autoCreateMemberTag_02(self):
        """驗證 Master新增會員->修改會員密碼->再登入"""
        SetDelayTime()
        account = "QATags" + common_config.now
        agent = master_config.exist_agent
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
        self.portal.ChangePassword(account, '123456')
        self.portal.SetBankAccount(account, 'a123456')
        self.portal.close()
        data = {"MemberTagIds": "541", "connectionId": self.user.info()}
        response_data = self.searchMember.search(data)
        validateData = response_data[1]['PageData'][0]['Account']
        self.assertEqual(account, validateData)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
