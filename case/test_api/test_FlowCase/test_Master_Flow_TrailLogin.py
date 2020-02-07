'''
@Created by loka
@Date : 2020/01/17
'''

import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from base.CommonMethod import PortalExecution


class TrailLogin(unittest.TestCase):
    """試玩帳號登入 - 確認可以登入成功"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.trail = member_and_agent.Trial(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_trailLogin(self):
        """試玩帳號登入"""
        Id = self.getId()  # 取得ID
        data = {"id": Id}
        self.trail.allow(data)
        account = self.get_trailAccount()  # 取得帳號
        password = self.get_trailPassword()  # 取得密碼
        self.portal = PortalExecution()
        validateData = self.portal.Trail_Login(account, password)  # 試玩登入並且取得登入成功後的試玩帳號
        self.assertEqual(validateData, account)

    def getId(self):
        data = {"count": 100, "skip": 0}
        response_data = self.trail.load(data)
        Id = response_data[1][0]['Id']
        return Id

    def get_trailAccount(self):
        data = {"count": 100, "skip": 0}
        response_data = self.trail.load(data)
        Account = response_data[1][0]['Account']
        return Account

    def get_trailPassword(self):
        data = {"count": 100, "skip": 0}
        response_data = self.trail.load(data)
        Password = response_data[1][0]['Password']
        return Password


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
