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


class EmailLoginValidation(unittest.TestCase):
    """電子郵件登入驗證-超過三次失敗無法再發送郵件"""

    # step 1:登入Portal直接失敗三次
    # step 2:查看會員詳細資料鎖頭是否有索起來
    # step 3:是否可以解開

    # 前置作業:
    #   測試會員:QALink01140234
    #   密碼:a123456
    #   會員等級:API測試，Id:58
    #   掛載商戶: QAJTEST
    #   寄信的Email地址: tak_liao@xinliwang.com.tw

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細資料
        self.user.login()

    def tearDown(self):
        self.user.logout()

    # def test_EmailLoginValidation(self):
    #     """驗證 超過三次失敗無法再發送郵件"""


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
