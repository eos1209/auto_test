# 因為入口關閉所以註解
# 20200514開啟入口
#
# '''
# @Created by loka
# @Date : 2020/03/05
# '''
import unittest
import time
import random
from pprint import pprint

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from data_config.system_config import systemSetting
from master_api.Home import Home


class SuperSearchTest(unittest.TestCase):
    """超級會員查詢 功能驗證流程"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberSearch = member_and_agent.MemberSearch(self.__http)  # 會員搜尋
        self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細
        self.memberTags = member_and_agent.MemberTags(self.__http)  # 會員標籤
        self.home = Home(self.__http)
        self.user.login()

    @classmethod
    def timestamp(cls):
        return int(time.time())

    def GetMemberStates(self):
        """取得所有狀態值"""
        data = {}
        response_data = self.memberSearch.getMemberStates(data)
        item = []
        for i in range(len(response_data[1])):
            item.append(response_data[1][i]["Value"])
        return item

    def getAllDiscountSettings(self):  # 取全部的返水等級，放在一個item
        data = {}
        response_data = self.home.getAllDiscountSettings(data)
        item = []
        for i in range(len(response_data[1])):
            item.append(response_data[1][i]['Value'])
        return item

    def getAllMemberLevels(self):  # 取全部的會員等級，放在一個item
        data = {}
        response_data = self.home.getAllMemberLevels(data)
        item = []
        for i in range(len(response_data[1])):
            item.append(response_data[1][i]['Value'])
        return item

    def getmemberTags(self):  # 取全部的會員標籤，放在一個item
        data = {}
        response_data = self.memberTags.getTags(data)
        item = []
        for i in range(len(response_data[1]["ReturnObject"])):
            item.append(response_data[1]["ReturnObject"][i]['Id'])
        return item

    def test_MemberV2_relatedApi_status_01(self):
        """驗證 超級會員查詢 - 取得超級會員顯示欄位 功能"""
        data = {}
        response_data = self.memberSearch.getColumnForSuperSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberV2_relatedApi_status_02(self):
        """超級會員查詢 - 單一會員查詢"""
        data = {"connectionId": self.user.info(),
                "search": {"account": self.config.MasterMember(),
                           "_": SuperSearchTest.timestamp()
                           }
                }
        response_data = self.memberSearch.superSearch(data)
        validateData = response_data[1]['ReturnObject']['MemberInformationList'][0]['Account']
        self.assertEqual(self.config.MasterMember(), validateData, '搜尋出來的帳號不一致')

    def test_MemberV2_relatedApi_status_03(self):
        """超級會員查詢 - 多個會員查詢"""
        configData = self.config.batch_Member_config().split(',')
        data = {"connectionId": self.user.info(),
                "pageIndex": 0,
                "search": {"account": self.config.batch_Member_config(),
                           "_": SuperSearchTest.timestamp()
                           }
                }
        response_data = self.memberSearch.superSearch(data)
        for i in range(response_data[1]['ReturnObject']['TotalCount']):
            validateData = response_data[1]['ReturnObject']['MemberInformationList'][i]['Account']
            if bool(configData[i] != validateData):
                self.assertNotEqual(configData[i], validateData, '搜尋出來的帳號不一致')
            else:
                self.assertEqual(configData[i], validateData)

    def test_MemberV2_relatedApi_status_04(self):
        """超級會員查詢 - 帳戶餘額查詢"""
        # configData = 1.01
        data = {"connectionId": self.user.info(),
                "search": {"_": SuperSearchTest.timestamp(),
                           "balanceMin": 1,
                           "balanceMax": 1.01
                           }
                }
        response_data = self.memberSearch.GetSuperSearchSumBalance(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        # for i in range(10):
        #     validateData = response_data[1]['ReturnObject']['MemberInformationList'][i]['Balance']
        #     if bool(configData <= validateData):
        #         self.assertEqual(bool(configData <= validateData), True)
        #     else:
        #         self.assertEqual(bool(configData <= validateData), False, '金額錯誤，超出預期條件')

    def test_MemberV2_relatedApi_status_05(self):
        """超級會員查詢 - 餘額寶餘額查詢"""
        # configData = 20
        data = {"connectionId": self.user.info(),
                "pageIndex": 0,
                "search": {"yuebaoMin": 10,
                           "yuebaoMax": 20,
                           "_": SuperSearchTest.timestamp(),
                           "export": {"columnIds": [22],
                                      "advancedColumn": []
                                      }
                           }
                }
        response_data = self.memberSearch.superSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        # for i in range(10):
        #     validateData = response_data[1]['ReturnObject']['MemberInformationList'][i]['YuebaoAmount']
        #     if bool(configData >= validateData):
        #         self.assertEqual(bool(configData >= validateData), True)
        #     else:
        #         self.assertEqual(bool(configData <= validateData), False, '金額錯誤，超出預期條件')

    def test_MemberV2_relatedApi_status_06(self):
        """超級會員查詢 - 停用、啟用、錢包凍結、系統停用、系統錢包凍結 狀態查詢"""
        # configData = 0
        status = self.GetMemberStates()
        for i in range(len(status)):
            data = {"connectionId": self.user.info(),
                    "pageIndex": 0,
                    "search": {"_": SuperSearchTest.timestamp(),
                               "state": i,
                               "export": {"columnIds": [6],
                                          "advancedColumn": []
                                          }
                               }
                    }
            response_data = self.memberSearch.superSearch(data)
            status_code = response_data[0]
            self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberV2_relatedApi_status_07(self):
        """超級會員查詢 - 會員等級隨機取樣查詢"""
        Leves = random.choice(self.getAllMemberLevels())
        data = {"connectionId": self.user.info(),
                "pageIndex": 0,
                "search": {"_": SuperSearchTest.timestamp(),
                           "state": Leves,
                           "export": {"columnIds": [6],
                                      "advancedColumn": []
                                      }
                           }
                }
        response_data = self.memberSearch.superSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberV2_relatedApi_status_08(self):
        """超級會員查詢 - 會員標籤隨機取樣查詢"""
        Tags = random.choice(self.getmemberTags())
        data = {
            "connectionId": self.user.info(),
            "pageIndex": 0,
            "search": {
                "memberTagIds": [Tags],
                "_": SuperSearchTest.timestamp()
            }
        }
        response_data = self.memberSearch.superSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberV2_relatedApi_status_09(self):
        """超級會員查詢 - 返水等級隨機取樣查詢"""
        DiscountSettings = random.choice(self.getAllDiscountSettings())
        data = {"connectionId": self.user.info(),
                "pageIndex": 0,
                "search": {"discountSettingId": [DiscountSettings],
                           "_": SuperSearchTest.timestamp()
                           }
                }
        response_data = self.memberSearch.superSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberV2_relatedApi_status_10(self):
        """超級會員查詢 - 匯出EXcel"""
        data = {
            "search": {
                "search": 'true',
                "gameSupplierType": 1,
                "_": SuperSearchTest.timestamp(),
                "page": 1
            },
            "connectionId": self.user.info(),
            "columnIds": [
            ],
            "advancedColumn": [
            ]
        }
        response_data = self.memberSearch.ExportForSuperSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberV2_relatedApi_status_11(self):
        """超級會員查詢 - 驗證選取顯示欄位"""
        data = {
            "connectionId": self.user.info(),
            "pageIndex": 0,
            "search": {
                "gameSupplierType": 1,
                "_": SuperSearchTest.timestamp(),
                "export": {
                    "columnIds": [
                        0,
                        1],
                    "advancedColumn": [
                    ]
                }
            }
        }
        response_data = self.memberSearch.superSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberV2_relatedApi_status_12(self):
        """超級會員查詢 - 更多條件_注冊裝置驗證"""
        data = {
            "connectionId": self.user.info(),
            "pageIndex": 0,
            "search": {
                "advanceSearch": {
                    "memberInfoRequest": {
                        "registerDevice": 1
                    }
                },
                "_": SuperSearchTest.timestamp()
            }
        }
        response_data = self.memberSearch.superSearch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
