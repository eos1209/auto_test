'''
@Created by yuhsiang
@Date : 2018/12/10
'''
import unittest
from base.TimeClass import get_first_day, get_next_first_day, get_todaynow_Y
from master_api.Home import Home
from master_api.account_login import User
from master_api.system_management import ActivityManagement
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config


class CheckInEventBaseTest(unittest.TestCase):
    """ 签到奖励 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.home = Home(self.__http)
        self.checkInEvent = ActivityManagement.CheckInEvent(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getAllMemberLevels(self):  # 取全部的會員等級，放在一個item
        data = {}
        response_data = self.home.getAllMemberLevels(data)
        item = []
        for i in range(len(response_data[1])):
            item.append(response_data[1][i]['Value'])
        return item

    def getAllMemberLevelsAll(self):  # 取全部的會員等級，重新組合列表
        data = {}
        items = []
        response_data = self.home.getAllMemberLevels(data)
        for i in range(len(response_data[1])):
            a = {
                "Id": response_data[1][i]['Value'],
                "Name": response_data[1][i]['Text']
            }
            items.append(a)
        return items

    def getLevels(self):  # 取QA_test等級
        data = {}
        response_data = self.home.getAllMemberLevels(data)
        for i in range(len(response_data[1])):
            if response_data[1][i]['Text'] == "QA_Test":
                ID = response_data[1][i]['Value']
        return ID

    def getloadNewId(self):
        """取得最新一筆 - ID"""
        data = {"take": 100,
                "skip": 0,
                "query": {"AllState": True,
                          "StatusList": [0, 1, 2]}
                }
        response_data = self.checkInEvent.loadNew(data)
        for i in range(len(response_data[1]['ReturnObject'])):
            if response_data[1]['ReturnObject'][i]['Name'] == get_todaynow_Y():
                ID = response_data[1]['ReturnObject'][i]['Id']
                Name = response_data[1]['ReturnObject'][i]['Name']
                break
            else:
                ID = response_data[1]['ReturnObject'][i]['Id']
                Name = response_data[1]['ReturnObject'][i]['Name']
        return ID, Name

    def test_CheckInEvent_relatedApi_status_01(self):
        """驗證 签到奖励 - 取得列表資料"""
        data = {"take": 100,
                "skip": 0,
                "query": {"AllState": True,
                          "StatusList": [0, 1, 2]}
                }
        response_data = self.checkInEvent.loadNew(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CheckInEvent_relatedApi_status_02(self):
        """驗證 签到奖励 - 取得獲取活動時間表"""
        data = {}
        response_data = self.checkInEvent.GetEventTimeList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CheckInEvent_relatedApi_status_03(self):
        """驗證 签到奖励 - 新增簽到獎勵 下個月的第一天 到最後一天"""
        data = {
            "BeginTime": get_next_first_day()[0],
            "EventSettings": [
                {
                    "Days": 1,
                    "BonusAmount": 1,
                    "Img": {
                        "$ngfBlobUrl": "blob:http://master.fnjtd.com/d1447882-6516-46e0-be16-6fa3520d2e1e"
                    },
                    "ImageUrl": "/Cdn2Redirect/Web.Portal/CheckInOfferImages/069ca58947de47588c39c988f49cf238.png",
                    "imgStatus": 2,
                    "uploadImgErrorMessage": "",
                    "errorFile": 'null'
                }],
            "CheckType": 1,
            "IsSupplement": 'true',
            "SupplementSetting": {
                "SettlementType": 1,
                "DepositTotalCount": 1
            },
            "Name": get_todaynow_Y(),
            "EndTime": get_next_first_day()[1],
            "DailyCheckMoney": 1,
            "AutoSupplementZeroing": 'true',
            "MemberLevelSettings": self.getLevels()
        }
        response_data = self.checkInEvent.Create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CheckInEvent_relatedApi_status_04(self):
        """驗證 签到奖励 - 取得所有可用的會員級別設置"""
        data = {"beginTime": get_first_day()[0],
                "endTime": get_first_day()[1],
                "id": 'null'
                }
        response_data = self.checkInEvent.AllAvailableMemberLevelSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CheckInEvent_relatedApi_status_05(self):
        """驗證 签到奖励 - 取得簽到獎勵詳細資料"""
        data = {"id": self.getloadNewId()[0]}
        response_data = self.checkInEvent.GetDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CheckInEvent_relatedApi_status_06(self):
        """ 驗證 簽到獎勵 - 修改未開始活動每日簽到金"""
        data = {
            "Id": self.getloadNewId()[0],
            "Name": self.getloadNewId()[1],
            "RecordCount": 0,
            "AccordCount": 0,
            "BeginTime": get_next_first_day()[0],
            "EndTime": get_next_first_day()[1],
            "DailyCheckMoney": 3,
            "DailyAuditTimes": 'null',
            "IsSupplement": 'true',
            "AutoLoopBonusDays": 'false',
            "AutoSupplementZeroing": 'true',
            "CheckType": 1,
            "DepositSetting": {
                "DepositCountStart": 'null',
                "DepositCountEnd": 'null',
                "DepositTotalAmountStart": 'null',
                "DepositTotalAmountEnd": 'null',
                "DepositTimeStart": 'null',
                "DepositTimeEnd": 'null'
            },
            "CommissionSettings": [
            ],
            "SupplementSetting": {
                "RawDataList": [
                ],
                "SupplementCount": 'null',
                "DepositTotalCount": 1,
                "DepositTotalAmount": 'null',
                "SettlementType": 1,
                "Commission": 'null'
            },
            "MemberLevels": self.getAllMemberLevelsAll(),
            "EventSettings": [
                {
                    "Days": 1,
                    "BonusAmount": 1,
                    "ImageUrl": "/Cdn2Redirect/Web.Portal/CheckInOfferImages/069ca58947de47588c39c988f49cf238.png",
                    "BonusAuditTimes": 'null',
                    "imgStatus": 2
                }],
            "Creator": "sky",
            "CreateTime": "/Date(1589225295810)/",
            "MemberLevelSettings": self.getAllMemberLevels()
        }
        response_data = self.checkInEvent.Update(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_CheckInEvent_relatedApi_status_(self):
        """驗證 签到奖励 - 活動下架"""
        data = {"offerId": self.getloadNewId()[0]}
        print(data)
        response_data = self.checkInEvent.EventOff(data)
        print(response_data[1])
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
