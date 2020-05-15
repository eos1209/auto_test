'''
@Created by loka
@Date : 2020/01/31
'''

import unittest
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from master_api import account_management
from data_config.system_config import systemSetting
from base.CommonMethod import Portal_test


class MoneyPassword(unittest.TestCase):
    """ 重設取款密碼流程"""

    def setUp(self):
        self.config = systemSetting()  # 參數設定

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.memberCreate = member_and_agent.MemberCreate(cls.__http)
        cls.user.login()
        cls.memberDetail = member_and_agent.MemberDetail(cls.__http)  # 會員詳細資料
        cls.verifyWithdraw = account_management.VerifyWithdraw(cls.__http)  # 取款審核
        cls.memberTransaction = account_management.MemberTransaction(cls.__http)  # 交易紀錄

    def tearDown(self):
        self.user.logout()

    def member_id(self):
        MoneyPassword.Master_login()
        data = {"connectionId": self.user.info(), "account": self.config.test_Member_config()}
        response_data = self.memberDetail.getDetail(data)
        return response_data[1]['Member']['Id']

    def test_MoneyPassword_01(self):
        """驗證 重設取款密碼流程 - 變更取款密碼"""
        # 流程
        # 1.重設取款密碼
        # 2.登入變更取款密碼
        # 3.再次登入線上取款驗證密碼是否正確
        # 4.到取款審核看板拒絕取款要求並且退回
        # 5.驗證交易紀錄查詢的單號是否跟取款審核要求的ID是否一致
        data = {"id": self.member_id()}
        response_data = self.memberDetail.resetMoneyPassword(data)
        getMoneyPassword = response_data[1]['MoneyPassword']
        self.portal = Portal_test()
        self.portal.resetMoneyPassword(self.config.test_Member_config(), self.config.test_Password_config(),
                                       getMoneyPassword)
        self.portal.verifyDraw(self.config.test_Member_config(), self.config.test_Password_config(), '123456')
        MoneyPassword.Master_login()
        data = {"count": 100, "query": {"search": 'null'}}
        response_data = self.verifyWithdraw.load(data)
        getId = response_data[1]['Data'][0]['Id']
        data = {"id": getId}
        self.verifyWithdraw.deny(data)
        data = {"Account": self.config.test_Member_config(), "Types": ["OnlineWithdraw"]}
        response_data = self.memberTransaction.search(data)
        getData = response_data[1]['PageData'][0]['Memo']
        getValidateData = getData.split("'")
        validateData = getValidateData[1].split('/')
        # print(validateData)
        self.assertEqual(str(validateData[2]), str(getId))

    def test_MoneyPassword_02(self):
        """驗證 取款密碼提款流程 - 線上取款"""
        # 流程
        # 1.重設取款密碼
        # 2.再次登入線上取款驗證密碼是否正確
        # 3.到取款審核看板拒絕取款要求並且退回
        # 4.驗證交易紀錄查詢的單號是否跟取款審核要求的ID是否一致
        data = {"id": self.member_id()}
        response_data = self.memberDetail.resetMoneyPassword(data)
        getMoneyPassword = response_data[1]['MoneyPassword']
        self.portal = Portal_test()
        self.portal.verifyDraw(self.config.test_Member_config(), self.config.test_Password_config(), getMoneyPassword)
        MoneyPassword.Master_login()
        data = {"count": 100, "query": {"search": 'null'}}
        response_data = self.verifyWithdraw.load(data)
        getId = response_data[1]['Data'][0]['Id']
        data = {"id": getId}
        self.verifyWithdraw.deny(data)
        data = {"Account": self.config.test_Member_config(), "Types": ["OnlineWithdraw"]}
        response_data = self.memberTransaction.search(data)
        getData = response_data[1]['PageData'][0]['Memo']
        getValidateData = getData.split("'")
        validateData = getValidateData[1].split('/')
        print(validateData)
        self.assertEqual(str(validateData[2]), str(getId))


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
