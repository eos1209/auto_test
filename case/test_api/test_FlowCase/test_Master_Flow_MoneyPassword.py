'''
@Created by loka
@Date : 2020/01/31
'''

import unittest
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from data_config import portal_config
from master_api.account_login import User
from base.CommonMethod import PortalExecution
from master_api import account_management


class MoneyPassword(unittest.TestCase):
    """ 重設取款密碼流程"""

    # 測試帳號:QATags02040246
    # 測試帳號Id:3152066
    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberCreate = member_and_agent.MemberCreate(self.__http)
        self.user.login()
        self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細資料
        self.verifyWithdraw = account_management.VerifyWithdraw(self.__http)  # 取款審核
        self.memberTransaction = account_management.MemberTransaction(self.__http)  # 交易紀錄

    def tearDown(self):
        self.user.logout()

    def test_MoneyPassword_01(self):
        """驗證 重設取款密碼流程 - 變更取款密碼"""
        # 流程
        # 1.重設取款密碼
        # 2.登入變更取款密碼
        # 3.再次登入線上取款驗證密碼是否正確
        # 4.到取款審核看板拒絕取款要求並且退回
        # 5.驗證交易紀錄查詢的單號是否跟取款審核要求的ID是否一致
        data = {"id": 3152066}
        response_data = self.memberDetail.resetMoneyPassword(data)
        getMoneyPassword = response_data[1]['MoneyPassword']
        self.portal = PortalExecution()
        self.portal.resetMoneyPassword(portal_config.Portal_account, portal_config.Portal_Password, getMoneyPassword)
        self.portal_verifyWithdraw = PortalExecution()
        self.portal_verifyWithdraw.verifyWithdraw('QATags02040246', 'a123456', '123456')  # PS:該登入會員必須先設定好銀行帳戶+支付寶帳戶
        data = {"count": 100, "query": {"search": 'null'}}
        response_data = self.verifyWithdraw.load(data)
        getId = response_data[1]['Data'][0]['Id']
        data = {"id": getId}
        self.verifyWithdraw.deny(data)
        data = {"Account": portal_config.Portal_account, "Types": ["OnlineWithdraw"]}
        response_data = self.memberTransaction.search(data)
        getData = response_data[1]['PageData'][0]['Memo']
        getValidateData = getData.split("'")
        validateData = getValidateData[1].split('/')
        print(validateData)
        self.assertEqual(str(validateData[2]), str(getId))

    def test_MoneyPassword_02(self):
        """驗證 取款密碼提款流程 - 線上取款"""
        # 流程
        # 1.重設取款密碼
        # 2.再次登入線上取款驗證密碼是否正確
        # 3.到取款審核看板拒絕取款要求並且退回
        # 4.驗證交易紀錄查詢的單號是否跟取款審核要求的ID是否一致
        data = {"id": 3152066}
        response_data = self.memberDetail.resetMoneyPassword(data)
        getMoneyPassword = response_data[1]['MoneyPassword']
        print(getMoneyPassword)
        self.portal = PortalExecution()
        self.portal.verifyWithdraw('QATags02040246', 'a123456', getMoneyPassword)  # PS:該登入會員必須先設定好銀行帳戶+支付寶帳戶
        data = {"count": 100, "query": {"search": 'null'}}
        response_data = self.verifyWithdraw.load(data)
        getId = response_data[1]['Data'][0]['Id']
        data = {"id": getId}
        self.verifyWithdraw.deny(data)
        data = {"Account": portal_config.Portal_account, "Types": ["OnlineWithdraw"]}
        response_data = self.memberTransaction.search(data)
        getData = response_data[1]['PageData'][0]['Memo']
        getValidateData = getData.split("'")
        validateData = getValidateData[1].split('/')
        print(validateData)
        self.assertEqual(str(validateData[2]), str(getId))


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
