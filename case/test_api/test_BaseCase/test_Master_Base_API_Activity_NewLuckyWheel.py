'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from master_api.account_login import User
from master_api.system_management import ActivityManagement
from master_api.system_management import PortalManagement
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from data_config.system_config import systemSetting
from base.CommonMethod import UploadFile
from base.CommonMethod import GameHallType
from base.CommonMethod import Portal_test
from time import sleep
from datetime import datetime, timedelta
from base.CommonMethod import system_config_Setting


class NewLuckyWheelBaseTest(unittest.TestCase):
    """ 时来运转 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.newLuckyWheel = ActivityManagement.NewLuckyWheel(self.__http)
        self.PortalManagement = PortalManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def create_NewLuckyWheel_mode(self, mode):  # 讀取系統檔案來決定獎品數量
        self.system = system_config_Setting()
        self.gameHall = GameHallType()
        BeginTime = (datetime.now() + timedelta(hours = -12)).strftime("%Y/%m/%d %H:%M:%S")
        EndTime = (datetime.now() + timedelta(hours = -11)).strftime("%Y/%m/%d %H:%M:%S")
        if mode == 6:
            data = {
                "RewardInfoList": [
                    {"status": 2, "RewardType": "1", "RewardTitle": "A", "RewardName": "1st", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "再来一次", "Probability": 10},
                    {"status": 2, "RewardType": "2", "RewardTitle": "B", "RewardName": "2nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖金", "Price": 1, "Audit": 1, "Stock": 11,
                     "Probability": 50},
                    {"status": 2, "RewardType": "3", "RewardTitle": "C", "RewardName": "3nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖品", "Stock": 1, "Probability": 10},
                    {"status": 2, "RewardType": "2", "RewardTitle": "D", "RewardName": "4th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "谢谢参与"},
                    {"status": 2, "RewardType": "2", "RewardTitle": "E", "RewardName": "5th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "F", "RewardName": "6th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1}],
                "RewardCount": mode,
                "BeginTime": BeginTime,
                "DailyOpenTimes": [],
                "LotterySettings": [{"DepositAmount": 1,
                                     "GameCategories": self.gameHall.GameCategories(),
                                     "categoriesText": "(全选)",
                                     "CommissionAmount": 1,
                                     "LotteryCount": 1, "isInsert": 'true'}
                                    ],
                "Name": 'QA_test',
                "EndTime": EndTime,
                "EntranceVisible": 'true',
                "LotteryBaseCount": 5,
                "DepositType": 1,
                "MemberLevelIds": [self.system.getMemberLevelId()],
                "Description": "<p>@QA_automation</p>\n"
            }
            return data
        elif mode == 8:
            data = {
                "RewardInfoList": [
                    {"status": 2, "RewardType": "1", "RewardTitle": "A", "RewardName": "1st", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "再来一次", "Probability": 10},
                    {"status": 2, "RewardType": "2", "RewardTitle": "B", "RewardName": "2nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖金", "Price": 1, "Audit": 1, "Stock": 11,
                     "Probability": 30},
                    {"status": 2, "RewardType": "3", "RewardTitle": "C", "RewardName": "3nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖品", "Stock": 1, "Probability": 10},
                    {"status": 2, "RewardType": "2", "RewardTitle": "D", "RewardName": "4th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "E", "RewardName": "5th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "F", "RewardName": "6th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "G", "RewardName": "7th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "H", "RewardName": "8th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1}
                ],

                "RewardCount": mode,
                "BeginTime": BeginTime,
                "DailyOpenTimes": [],
                "LotterySettings": [{"DepositAmount": 1,
                                     "GameCategories": self.gameHall.GameCategories(),
                                     "categoriesText": "(全选)",
                                     "CommissionAmount": 1,
                                     "LotteryCount": 1, "isInsert": 'true'}
                                    ],
                "Name": "QA_test",
                "EndTime": EndTime,
                "EntranceVisible": 'true',
                "LotteryBaseCount": 5,
                "DepositType": 1,
                "MemberLevelIds": [self.system.getMemberLevelId()],
                "Description": "<p>@QA_automation</p>\n"
            }
            return data
        elif mode == 10:
            data = {
                "RewardInfoList": [
                    {"status": 2, "RewardType": "1", "RewardTitle": "A", "RewardName": "1st", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "再来一次", "Probability": 10},
                    {"status": 2, "RewardType": "2", "RewardTitle": "B", "RewardName": "2nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖金", "Price": 1, "Audit": 1, "Stock": 11,
                     "Probability": 10},
                    {"status": 2, "RewardType": "3", "RewardTitle": "C", "RewardName": "3nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖品", "Stock": 1, "Probability": 10},
                    {"status": 2, "RewardType": "2", "RewardTitle": "D", "RewardName": "4th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "E", "RewardName": "5th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "F", "RewardName": "6th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "G", "RewardName": "7th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "H", "RewardName": "8th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "I", "RewardName": "9th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "J", "RewardName": "10th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1}
                ],
                "RewardCount": mode,
                "BeginTime": BeginTime,
                "DailyOpenTimes": [],
                "LotterySettings": [{"DepositAmount": 1,
                                     "GameCategories": self.gameHall.GameCategories(),
                                     "categoriesText": "(全选)",
                                     "CommissionAmount": 1,
                                     "LotteryCount": 1, "isInsert": 'true'}
                                    ],
                "Name": "QA_test",
                "EndTime": EndTime,
                "EntranceVisible": 'true',
                "LotteryBaseCount": 5,
                "DepositType": 1,
                "MemberLevelIds": [self.system.getMemberLevelId()],
                "Description": "<p>@QA_automation</p>\n"
            }
            return data
        elif mode == 12:
            data = {
                "RewardInfoList": [
                    {"status": 2, "RewardType": "1", "RewardTitle": "A", "RewardName": "1st", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "再来一次", "Probability": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "B", "RewardName": "2nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖金", "Price": 1, "Audit": 1, "Stock": 11,
                     "Probability": 19},
                    {"status": 2, "RewardType": "3", "RewardTitle": "C", "RewardName": "3nd", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "TypeDescription": "奖品", "Stock": 1, "Probability": 10},
                    {"status": 2, "RewardType": "2", "RewardTitle": "D", "RewardName": "4th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "E", "RewardName": "5th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "F", "RewardName": "6th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 10, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "G", "RewardName": "7th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 20, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "H", "RewardName": "8th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 5, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "I", "RewardName": "9th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 5, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "J", "RewardName": "10th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 5, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "K", "RewardName": "11th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 3, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1},
                    {"status": 2, "RewardType": "2", "RewardTitle": "L", "RewardName": "12th", "ImageUrl": '',
                     "uploadImgErrorMessage": "", "Probability": 2, "TypeDescription": "奖金", "Stock": 1, "Price": 1,
                     "Audit": 1}
                ],

                "RewardCount": mode,
                "BeginTime": BeginTime,
                "DailyOpenTimes": [],
                "LotterySettings": [{"DepositAmount": 1,
                                     "GameCategories": self.gameHall.GameCategories(),
                                     "categoriesText": "(全选)",
                                     "CommissionAmount": 1,
                                     "LotteryCount": 1, "isInsert": 'true'}
                                    ],
                "Name": "QA_test",
                "EndTime": EndTime,
                "EntranceVisible": 'true',
                "LotteryBaseCount": 5,
                "DepositType": 1,
                "IsShowRewardRecord": 'true',
                "MemberLevelIds": [self.system.getMemberLevelId()],
                "Description": "<p>@QA_automation</p>\n"
            }
            return data

    def getLuckyWheelId(self):
        data = {"skip": 0, "take": 100, "search": {"AllState": False, "Status": [0, 1]}}
        response_data = self.newLuckyWheel.getList(data)
        print(response_data)
        for i in range(len(response_data[1]['ReturnObject'])):
            if response_data[1]['ReturnObject'][i]['Name'] == 'QA_test':
                Id = response_data[1]['ReturnObject'][i]['Id']
                return Id

    def test_NewLuckyWheelBaseTest_relatedApi_status_01(self):
        """驗證 时来运转 - 取得列表資料"""
        data = {"skip": 0,
                "take": 100,
                "search": {"AllState": True,
                           "Status": [0, 1, 2]}}
        response_data = self.newLuckyWheel.getList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_02(self):
        """驗證 时来运转 - 取得入口圖片"""
        data = {"EventName": "NewLuckyWheel"}
        response_data = self.newLuckyWheel.getImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_03(self):
        """驗證 时来运转 - 更新入口圖片"""
        data = {"EventName": "NewLuckyWheel",
                "WebImageUrl": "/CdnRedirect/Web.Portal/_Common/Content/Views/Shared/images/Service/NewLuckyWheel.gif",
                "WebIsShow": 'true',
                "MobileImageUrl": "/CdnRedirect/Web.Mobile/_Common/Content/Views/Shared/images/Service/NewLuckyWheel.gif",
                "MobileIsShow": 'true'}
        response_data = self.newLuckyWheel.updateEntranceImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_04(self):
        """驗證 时来运转 - 更新入口圖片"""
        self.upload = UploadFile('image/jpg/test_jpg.jpg', 'ImageFile', 'test_jpg.jpg')
        data = self.upload.Upload_file()
        response_data = self.newLuckyWheel.uploadImages(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()

    def test_NewLuckyWheelBaseTest_relatedApi_status_05(self):
        """驗證 时来运转 - 預覽Portal"""
        response_data = self.newLuckyWheel.getPortalUrl({})
        status_code = response_data[0]
        self.assertEqual(bool(status_code == common_config.Status_Code),
                         bool(self.config.Portal_config() + '/' == response_data[1]['PortalUrl']))

    def test_NewLuckyWheelBaseTest_relatedApi_status_06(self):
        """驗證 时来运转 - 取得全時來運轉時間列表"""
        response_data = self.newLuckyWheel.getAllLuckyWheelTimeList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_07(self):
        """驗證 时来运转 - 取得獎勵列表"""
        response_data = self.newLuckyWheel.getRewardTypeList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_08(self):
        """驗證 时来运转 - 新增時來運轉"""
        data = self.create_NewLuckyWheel_mode(self.config.NewLuckyWheel())
        response_data = self.newLuckyWheel.create(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_09(self):
        """驗證 时来运转 - 取得時來運轉詳細資料 狀態"""
        # step1:取得詳細資料Id
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id}
        response_data = self.newLuckyWheel.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_NewLuckyWheelBaseTest_relatedApi_status_10(self):
    #     """驗證 时来运转 - 修改時來運轉 狀態"""
    #     Id = self.getLuckyWheelId()
    #     data = {"luckyWheelId": Id}
    #     response_data = self.newLuckyWheel.getDetail(data)
    #     BeginTime = (datetime.now() + timedelta(hours = -12)).strftime("%Y/%m/%d %H:%M:%S")
    #     EndTime = (datetime.now() + timedelta(hours = -11)).strftime("%Y/%m/%d %H:%M:%S")
    #     luckyWheelInfo = response_data[1]['ReturnObject']
    #     # luckyWheelInfo['BeginTime'] = BeginTime
    #     # luckyWheelInfo['EndTime'] = EndTime
    #     luckyWheelInfo['MemberLevelIds'] = [luckyWheelInfo['MemberLevels'][0]['Id']]
    #     # print(luckyWheelInfo)
    #     data = {"luckyWheelInfo": luckyWheelInfo, 'luckyWheelId': Id}
    #     response_data = self.newLuckyWheel.modifyLuckyWheelInfo(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_11(self):
        """驗證 时来运转 - Portal時來運轉 狀態"""
        sleep(60)
        Id = self.getLuckyWheelId()
        self.portal = Portal_test()
        validateData = self.portal.newLuckyWheel(self.config.test_Member_config(), self.config.test_Password_config(),
                                                 Id)
        self.assertEqual(validateData, True)

    def test_NewLuckyWheelBaseTest_relatedApi_status_12(self):
        """驗證 时来运转 - 剩餘抽獎次數名單 狀態"""
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id, "take": 25, "skip": 0}
        response_data = self.newLuckyWheel.joinMemberDetailList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_13(self):
        """驗證 时来运转 - 匯出剩餘抽獎次數名單 狀態"""
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id}
        response_data = self.newLuckyWheel.exportMemberLuckyDrawCount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_14(self):
        """驗證 时来运转 - 添加次數 狀態"""
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id, "accounts": self.config.test_Member_config(), "count": 10}
        response_data = self.newLuckyWheel.manualSupply(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_15(self):
        """驗證 时来运转 - 抽獎名單-取得時來運轉名字 狀態"""
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id}
        response_data = self.newLuckyWheel.getNewLuckyWheelName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_16(self):
        """驗證 时来运转 - 抽獎名單-取得中獎名單 狀態"""
        Id = self.getLuckyWheelId()
        data = {"search": {"RewardStatus": [0, 1], "RewardTypes": ["0", "1", "2", "3"]}, "luckyWheelId": Id, "skip": 0,
                "take": 100}
        response_data = self.newLuckyWheel.getRewardRecords(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_17(self):
        """驗證 时来运转 - 抽獎名單-派發獎品獎金 狀態"""
        Id = self.getLuckyWheelId()
        data = {"search": {"RewardStatus": [0, 1], "RewardTypes": ["2", "3"]}, "luckyWheelId": Id, "skip": 0,
                "take": 100}
        response_data = self.newLuckyWheel.getRewardRecords(data)
        sentRewardId = response_data[1]['ReturnObject'][0]['Id']
        data = {"luckyWheelId": Id, "recordIds": sentRewardId}
        response_data = self.newLuckyWheel.sendRewards(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_18(self):
        """驗證 时来运转 - 抽獎名單-總抽獎次數 狀態"""
        Id = self.getLuckyWheelId()
        data = {"search": {"RewardStatus": [0, 1], "RewardTypes": ["0", "1", "2", "3"]}, "luckyWheelId": Id}
        response_data = self.newLuckyWheel.getCalculationCount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_19(self):
        """驗證 时来运转 - 抽獎名單-中獎統計圖 狀態"""
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id}
        response_data = self.newLuckyWheel.getRewardStatistics(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_20(self):
        """驗證 时来运转 - 中獎人名單開關 狀態"""
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id, "isShow": 'true'}
        response_data = self.newLuckyWheel.modifyShowRewardRecord(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_NewLuckyWheelBaseTest_relatedApi_status_21(self):
        """驗證 时来运转 - 立即下架 狀態"""
        Id = self.getLuckyWheelId()
        data = {"luckyWheelId": Id}
        response_data = self.newLuckyWheel.luckyWheelOff(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
