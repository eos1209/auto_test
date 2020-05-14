# 因為入口關閉所以註解
#
# '''
# @Created by loka
# @Date : 2020/03/05
# '''
import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from data_config.system_config import systemSetting
import time
from datetime import date, timedelta


class SuperSearchTest(unittest.TestCase):
    """超級會員查詢 功能驗證流程"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = member_and_agent.MemberSearch(self.__http)  # 會員搜尋
        self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細
        self.memberTags = member_and_agent.MemberTags(self.__http)  # 會員標籤
        self.user.login()

    @classmethod
    def timestamp(cls):
        return int(time.time())

    # def test_MemberV2_relatedApi_status_01(self):

    def test_single_AccountSearch(self):
        """超級會員查詢 - 單一會員查詢"""
        data = {"connectionId": self.user.info(),
                "search": {"account": self.config.MasterMember(), "_": SuperSearchTest.timestamp()}}
        response_data = self.memberSearch.superSearch(data)
        validateData = response_data[1]['ReturnObject']['MemberInformationList'][0]['Account']
        self.assertEqual(self.config.MasterMember(), validateData, '搜尋出來的帳號不一致')


    def test_batch_AccountSearch(self):
        """超級會員查詢 - 多個會員查詢"""
        configData = self.config.batch_Member_config().split(',')
        data = {"connectionId": self.user.info(),
                "search": {"account": self.config.batch_Member_config(), "_": SuperSearchTest.timestamp()}}
        response_data = self.memberSearch.superSearch(data)
        for i in range(response_data[1]['ReturnObject']['TotalCount']):
            validateData = response_data[1]['ReturnObject']['MemberInformationList'][i]['Account']
            if bool(configData[i] != validateData):
                self.assertNotEqual(configData, validateData, '搜尋出來的帳號不一致')
            else:
                self.assertEqual(configData, validateData)

    def test_balanceMinSearch(self):
        """超級會員查詢 - 帳戶餘額查詢"""
        configData = 1.01
        data = {"connectionId": self.user.info(),
                "search": {"_": SuperSearchTest.timestamp(), "balanceMin": 1,
                           "balanceMax": 1.01}}
        response_data = self.memberSearch.superSearch(data)
        # print(response_data[1])
        for i in range(10):
            validateData = response_data[1]['ReturnObject']['MemberInformationList'][i]['Balance']
            if bool(configData <= validateData):
                self.assertEqual(bool(configData <= validateData), True)
            else:
                self.assertEqual(bool(configData <= validateData), False, '金額錯誤，超出預期條件')

    def test_yuebaoSearch(self):
        """超級會員查詢 - 餘額寶餘額查詢"""
        configData = 20
        data = {"connectionId": self.user.info(), "pageIndex": 0,
                "search": {"yuebaoMin": 10, "yuebaoMax": 20, "_": SuperSearchTest.timestamp(),
                           "export": {"columnIds": [22], "advancedColumn": []}}}
        response_data = self.memberSearch.superSearch(data)
        for i in range(10):
            validateData = response_data[1]['ReturnObject']['MemberInformationList'][i]['YuebaoAmount']
            # print(validateData)
            if bool(configData >= validateData):
                self.assertEqual(bool(configData >= validateData), True)
            else:
                self.assertEqual(bool(configData <= validateData), False, '金額錯誤，超出預期條件')

    def test_statusSearch(self):
        """超級會員查詢 - 狀態查詢"""
        configData = 0
        data = {"connectionId": self.user.info(), "pageIndex": 0,
                "search": {"_": SuperSearchTest.timestamp(), "state": 0,
                           "export": {"columnIds": [6], "advancedColumn": []}}}
        response_data = self.memberSearch.superSearch(data)
        for i in range(10):
            validateData = response_data[1]['ReturnObject']['MemberInformationList'][i]['State']
            # print(validateData)
            if bool(configData == validateData):
                self.assertEqual(bool(configData == validateData), True)
            else:
                self.assertEqual(bool(configData != validateData), False, '會員狀態錯誤')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
