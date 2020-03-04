# '''
# @Created by loka
# @Date : 2020/02/06
# '''
#
# import unittest
# from base.httpRequest import HttpRequest
# from master_api import member_and_agent
# from master_api.account_login import User
# from base.CommonMethod import PortalExecution
# from master_api import account_management
# from data_config import portal_config
# from data_config import common_config
# from data_config import master_config
# from base.CommonMethod import mobileExecution
# from data_config.system_config import systemSetting
#
#
# class test_Portal_Basic_Process(unittest.TestCase):
#     """Portal端 功能腳本 -同步共用方法中的 PortalExecution"""
#
#     def setUp(self):
#         self.config = systemSetting()  # 參數設定
#         self.__http = HttpRequest()
#         self.user = User(self.__http)
#         self.memberCreate = member_and_agent.MemberCreate(self.__http)
#         self.user.login()
#         self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細資料
#         self.verifyWithdraw = account_management.VerifyWithdraw(self.__http)  # 取款審核
#         self.verify_deposit = account_management.VerifyDeposit(self.__http)  # 公司入款
#         self.memberCreate = member_and_agent.MemberCreate(self.__http)
#         self.searchMember = member_and_agent.MemberSearch(self.__http)  # 會員搜尋
#         self.trail = member_and_agent.Trial(self.__http)
#
#     def test_Login(self):
#         """Portal登入"""
#         self.portal = PortalExecution()
#         self.portal.Login(self.config.test_Member_config(), self.config.test_Password_config())
#
#     def test_Register(self):
#         """Portal註冊"""
#         register_Account = "QA_pt" + common_config.now
#         self.portal = PortalExecution()
#         self.portal.Register(register_Account)
#
#     def test_ChangePassword(self):
#         """Portal 修改密碼"""
#         account = "QA" + common_config.now
#         agent = master_config.exist_agent
#         data = {'Account': account,
#                 'Agent': agent,
#                 'memo': '@QA_portal'}
#         self.memberCreate.createSubmit(data)
#         data = {'Account': account,
#                 'connectionId': self.user.info()}
#         response_data = self.searchMember.search(data)
#         memberId = response_data[1]['PageData'][0]['Id']
#         data = {'id': memberId, "connectionId": self.user.info()}
#         get_password = self.memberDetail.resetPassword(data)
#         self.portal = PortalExecution()
#         self.portal.ChangePassword(account, get_password[1]['Password'])
#
#     def test_Trail(self):
#         """Portal 試玩帳號註冊"""
#         self.portal = PortalExecution()
#         self.portal.Trail()
#         data = {"count": 100, "skip": 0}
#         response_data = self.trail.load(data)
#         Id = response_data[1][0]['Id']
#         data = {"id": Id}
#         self.trail.allow(data)
#
#     def test_Trail_Login(self):
#         """Portal 試玩帳號登入"""
#         self.portal = PortalExecution()
#         self.portal.Trail_Login('T2jz4hgab', 'fd8aab')  # 試玩登入
#
#     def test_resetMoneyPassword(self):
#         """Portal 變更取款密碼"""
#         data = {"id": self.config.MemberId_config()}  # 05 : 3152066 06: 1041445
#         response_data = self.memberDetail.resetMoneyPassword(data)
#         getMoneyPassword = response_data[1]['MoneyPassword']
#         self.portal = PortalExecution()
#         self.portal.resetMoneyPassword(self.config.test_Member_config(), self.config.test_Password_config(),
#                                        getMoneyPassword)
#
#     def test_verifyWithdraw(self):
#         """Portal 線上取款"""
#         data = {"id": self.config.MemberId_config()}  # 05 : 3152066 06: 1041445
#         response_data = self.memberDetail.resetMoneyPassword(data)
#         getMoneyPassword = response_data[1]['MoneyPassword']
#         self.portal = PortalExecution()
#         self.portal.verifyWithdraw(self.config.test_Member_config(), self.config.test_Password_config(),
#                                    getMoneyPassword)
#
#     def test_verifyDeposit(self):
#         """Portal 公司入款"""
#         self.portal = PortalExecution()
#         verifyDeposit = self.portal.verifyDeposit(self.config.test_Member_config(),
#                                                   self.config.test_Password_config()).split(' ')  # 切割Portal端的訂單號碼
#         getId = verifyDeposit[1]
#         data = {"count": 100,
#                 "query":
#                     {"search": None}
#                 }
#         response_data = self.verify_deposit.get_load_data(data)
#         self.get_verify_deposit_id = response_data[1]['Data'][0]['Id']
#         if int(getId) == int(self.get_verify_deposit_id):
#             data = {"id": getId}
#             response_data = self.verify_deposit.order_deny(data)
#             status_code = response_data[0]
#             self.assertEqual(status_code, common_config.Status_Code)
#         else:
#             print(self.get_verify_deposit_id)
#             print(getId)
#             self.assertNotEqual(getId, self.get_verify_deposit_id, '前後端公司入款訂單號不相同')
#
#     def test_SetBankAccount(self):
#         """Portal 變更出款銀行密碼"""
#         account = "QApt" + common_config.now
#         agent = master_config.exist_agent
#         data = {'Account': account,
#                 'Agent': agent,
#                 'memo': '@autoMemberTags-fromPortal'}
#         self.memberCreate.createSubmit(data)
#         data = {'Account': account,
#                 'connectionId': self.user.info()}
#         response_data = self.searchMember.search(data)
#         memberId = response_data[1]['PageData'][0]['Id']
#         data = {'id': memberId}
#         self.memberDetail.resetMoneyPassword(data)
#         self.portal = PortalExecution()
#         self.portal.ChangePassword(account, '123456')
#         self.portal.SetBankAccount(account, 'a123456')
#
#     def test_ThirdPartyPayment(self):
#         """Portal 線上存款"""
#         self.portal = PortalExecution()
#         self.portal.ThirdPartyPayment(self.config.test_Member_config(), self.config.test_Password_config())
#
#     def test_Login_Fail(self):
#         self.mobile = mobileExecution()
#         self.mobile.mobile_Login_Fail(self.config.test_Member_config(), '5464646546')
#
#     def test_30(self):
#         for i in range(30):
#             self.test_Login_Fail()
#
#     def test_SiteMail(self):
#         self.portal = PortalExecution()
#         self.portal.SiteMail(self.config.test_Member_config(), self.config.test_Password_config())
