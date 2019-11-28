'''
@Created by yuhsiang
@Date : 2019/11/28
'''

import unittest
from time import sleep
import random

from selenium import webdriver

from master_api.account_login import User
from master_api.memeber_and_agent import MemberSearch
from master_api.account_management import MemberTransaction
from master_api.account_management import ThirdPartyPayment
from master_api.account_management import VerifyDeposit
from master_api.account_management import VerifyWithdraw
from master_api.system_management import SiteMail
from master_api.reports import BetRecords
from master_api.reports import GameSupplierTransaction
from master_api.reports import MemberLogin
from base.httpRequest import HttpRequest
from data_config import common_config


class SearchMemberAndGoToRandomPage(unittest.TestCase):
    """会员相關功能查询"""

    def getMemberCount(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://master.fnjtd.com/Account/Login")
        sleep(1)
        self.driver.set_window_size(1900, 1020)
        self.driver.find_element_by_xpath("//input[@ng-model = 'self.account']").send_keys("yuhsiang2")
        self.driver.find_element_by_xpath("//input[@ng-model = 'self.password']").send_keys("123456")
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        self.driver.get("http://master.fnjtd.com/Member")
        sleep(5)
        self.driver.find_element_by_xpath("//button[@id='btn-query']").click()
        sleep(5)
        GetMemberCount = self.driver.find_element_by_xpath("//div[@id='result']/div/div[3]/div/div[1]/b").text
        self.GetCountPage = int(int(GetMemberCount.replace(',', '')) / 10) + 1
        self.driver.close()
        return self.GetCountPage

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = MemberSearch(self.__http)
        self.memberTransaction = MemberTransaction(self.__http)
        self.verifyDeposit = VerifyDeposit(self.__http)
        self.thirdPartyPayment = ThirdPartyPayment(self.__http)
        self.verifyWithdraw = VerifyWithdraw(self.__http)
        self.SiteMail = SiteMail(self.__http)
        self.gameSupplierTransaction = GameSupplierTransaction(self.__http)
        self.betRecords = BetRecords(self.__http)
        self.memberLogin = MemberLogin(self.__http)

    def test_search_member_and_go_to_random_page(self):
        """会员查询並隨機跳轉詳細頁擁有的功能"""
        TotalPage = self.getMemberCount()
        # print(TotalPage)
        self.user.login()

        for i in range(0, 150000 - 1):
            random_page = random.randint(0, TotalPage)
            # print(random_page + 1)

            random_member = random.randint(0, 9)
            # print(random_member)

            data = {"pageIndex": random_page,
                    "connectionId": self.user.info()}
            response_data = self.memberSearch.search(data)
            GetMemberName = response_data[1]['PageData'][random_member]['Account']
            print("隨機查詢會員帳號:" + GetMemberName)

            # 進入查詢會員的詳細資料
            data = {"Account": GetMemberName}
            response_data = self.memberSearch.get_detail(data)
            self.memberId = response_data[1]['Member']['Id']
            self.assertEqual(common_config.Status_Code, response_data[0])
            flag = random.randint(1, 10)
            # print(flag)

            if flag == 1:
                # Step 检视帐户交易记录
                data = {"Account": GetMemberName}
                response_data = self.memberTransaction.search(data)
                self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 2:
                # Step 检视公司入款订单
                data = {"count": 100,
                        "query":
                            {"AccountString": GetMemberName,
                             "search": "true"}
                        }
                response_data = self.verifyDeposit.get_load_data(data)
                self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 3:
                # Step 检视线上支付订单
                data = {"count": 25,
                        "query":
                            {"AccountString": GetMemberName,
                             "isDTPP": "true",
                             "search": "true"}
                        }
                response_data = self.thirdPartyPayment.load_new(data)
                self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 4:
                # Step 检视取款申请订单
                data = {"count": 100,
                        "query":
                            {"AccountString": GetMemberName,
                             "search": "true"}
                        }
                response_data = self.verifyWithdraw.load(data)
                self.action = "VerifyDepositPage"
                self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 5:
                # Step 登入记录查询
                flag_1 = random.randint(1, 2)
                if flag_1 == 1:
                    data = {"search": {"Account": GetMemberName},
                            "pageIndex": "",
                            "pageSize": 10}
                    response_data = self.memberLogin.searchV2(data)
                    self.assertEqual(common_config.Status_Code, response_data[0])
                else:
                    data = {"search": {"IP": "118.163.212.115",
                                       "IpIsLike": "false"},
                            "pageIndex": "",
                            "pageSize": 10}
                    response_data = self.memberLogin.searchV2(data)
                    self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 6:
                # Step 检视此会员站内信记录
                data = {"Size": 30,
                        "SearchParam":
                            {"InboxSender": GetMemberName,
                             "InboxIsRead": "true",
                             "InboxIsUnRead": "true"},
                        "SendDateOrderBy": 0,
                        "LastId": " "}
                response_data = self.SiteMail.getInboxList(data)
                self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 7:
                # Step 检视今日投注记录
                data = {"Account": GetMemberName,
                        "WagersTimeBegin": common_config.WagersTimeBegin,
                        "connectionId": self.user.info()}
                response_data = self.betRecords.search(data)
                self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 8:
                # Step 检视娱乐城转帐记录
                data = {"Account": GetMemberName,
                        "transactionDateBegin": common_config.transactionDateBegin,
                        "transactionDateEnd": common_config.transactionDateEnd}
                response_data = self.gameSupplierTransaction.search(data)
                self.assertEqual(common_config.Status_Code, response_data[0])
            elif flag == 9:
                # Step 即时稽核
                data = {"Account": GetMemberName}
                response_data = self.memberSearch.get_detail(data)
                self.assertEqual(common_config.Status_Code, response_data[0])
            else:
                # Step 检视历史记录
                data = {"id": self.memberId,
                        "take": 100,
                        "skip": 0,
                        "query": {}
                        }
                response_data = self.memberSearch.load_history(data)
                self.assertEqual(common_config.Status_Code, response_data[0])

        # def tearDown(self):
        #     self.user.logout()


if __name__ == '__main__':
    unittest.main()
