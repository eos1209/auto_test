'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from master_api.account_login import User
from master_api.system_management import ActivityManagement
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from base.CommonMethod import UploadFile
from datetime import datetime, timedelta
from data_config.system_config import systemSetting
from base.CommonMethod import Portal_test


class LuckyWheelManagementBaseTest(unittest.TestCase):
    """ 幸运转盘 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.luckyWheelManagement = ActivityManagement.LuckyWheelManagement(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):  # 取得Id
        data = {"Size": 100,
                "IsPending": True,
                "IsStart": True,
                "IsEnd": True}
        response_data = self.luckyWheelManagement.getEventList(data)
        Id = response_data[1]['Response'][0]['ID']
        return Id

    @staticmethod
    def create_LuckyWheel_mode(mode):  # 讀取系統檔案來決定獎品數量
        BeginTime = (datetime.now() + timedelta(hours = -12)).strftime("%Y/%m/%d %H:%M:%S")
        EndTime = (datetime.now() + timedelta(hours = -11)).strftime("%Y/%m/%d %H:%M:%S")
        if mode == 6:
            data = {"Name": "QA_test", "Type": 0, "StartDate": BeginTime,
                    "EndDate": EndTime,
                    "RewardCount": mode, "EventDescription": "QA_automation",
                    "RewardInfoList": [{"Type": "1", "Name": "A", "TypeDescription": "再来一次", "Probability": 10},
                                       {"Type": "2", "Name": "B", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "3", "Name": "C", "TypeDescription": "奖品", "Stock": 10,
                                        "Probability": 10},
                                       {"Type": "2", "Name": "D", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 20},
                                       {"Type": "2", "Name": "E", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 30},
                                       {"Type": "1", "Name": "F", "TypeDescription": "再来一次", "Probability": 20}]}
            return data
        elif mode == 8:
            data = {"Name": "QA_test", "Type": 0, "StartDate": BeginTime,
                    "EndDate": EndTime,
                    "RewardCount": mode, "EventDescription": "QA_automation",
                    "RewardInfoList": [{"Type": "1", "Name": "A", "TypeDescription": "再来一次", "Probability": 10},
                                       {"Type": "2", "Name": "B", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "3", "Name": "C", "TypeDescription": "奖品", "Stock": 10,
                                        "Probability": 10},
                                       {"Type": "2", "Name": "D", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "2", "Name": "E", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 30},
                                       {"Type": "1", "Name": "F", "TypeDescription": "再来一次", "Probability": 20},
                                       {"Type": "2", "Name": "G", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 5},
                                       {"Type": "2", "Name": "H", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 5},
                                       ]}
            return data
        elif mode == 10:
            data = {"Name": "QA_test", "Type": 0, "StartDate": BeginTime,
                    "EndDate": EndTime,
                    "RewardCount": mode, "EventDescription": "QA_automation",
                    "RewardInfoList": [{"Type": "1", "Name": "A", "TypeDescription": "再来一次", "Probability": 10},
                                       {"Type": "2", "Name": "B", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "3", "Name": "C", "TypeDescription": "奖品", "Stock": 10,
                                        "Probability": 10},
                                       {"Type": "2", "Name": "D", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "2", "Name": "E", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "1", "Name": "F", "TypeDescription": "再来一次", "Probability": 10},
                                       {"Type": "2", "Name": "G", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "2", "Name": "H", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "2", "Name": "I", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "2", "Name": "J", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       ]}
            return data
        elif mode == 12:
            data = {"Name": "QA_test", "Type": 0, "StartDate": BeginTime,
                    "EndDate": EndTime,
                    "RewardCount": mode, "EventDescription": "QA_automation",
                    "RewardInfoList": [{"Type": "1", "Name": "A", "TypeDescription": "再来一次", "Probability": 10},
                                       {"Type": "2", "Name": "B", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "3", "Name": "C", "TypeDescription": "奖品", "Stock": 10,
                                        "Probability": 10},
                                       {"Type": "2", "Name": "D", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "2", "Name": "E", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 10},
                                       {"Type": "1", "Name": "F", "TypeDescription": "再来一次", "Probability": 10},
                                       {"Type": "2", "Name": "G", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 20},
                                       {"Type": "2", "Name": "H", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 5},
                                       {"Type": "2", "Name": "I", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 5},
                                       {"Type": "2", "Name": "J", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 5},
                                       {"Type": "2", "Name": "K", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 3},
                                       {"Type": "2", "Name": "L", "TypeDescription": "奖金", "Price": 1, "Audit": 1,
                                        "Stock": 10, "Probability": 2},
                                       ]}
            return data

    def test_LuckyWheelManagement_relatedApi_status_01(self):
        """驗證 幸运转盘 - 取得列表資料 頁面 狀態"""
        response_data = self.luckyWheelManagement.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_02(self):
        """驗證 幸运转盘 - 取得列表資料 狀態"""
        data = {"Size": 100,
                "IsPending": True,
                "IsStart": True,
                "IsEnd": True}
        response_data = self.luckyWheelManagement.getEventList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_03(self):
        """驗證 幸运转盘 - 取得入口圖片 狀態"""
        data = {"EventName": "LuckyWheelManagement"}
        response_data = self.luckyWheelManagement.getImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_04(self):
        """驗證 幸运转盘 - 預覽網址 狀態"""
        response_data = self.luckyWheelManagement.getPortalUrl({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_05(self):
        """驗證 幸运转盘 - 新增幸運輪盤 頁面 狀態"""
        response_data = self.luckyWheelManagement.createAndModify({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_06(self):
        """驗證 幸运转盘 - 取得獎品種類 狀態"""
        response_data = self.luckyWheelManagement.getRewardTypeList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_07(self):
        """驗證 幸运转盘 - 取得幸運輪盤活動時間 狀態"""
        response_data = self.luckyWheelManagement.getEventList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_08(self):
        """驗證 幸运转盘 - 上傳圖片 狀態"""
        self.upload = UploadFile('image/jpg/test_jpg.jpg',  # 檔案路徑
                                 'imageFile',  # 上傳欄位
                                 'test_jpg.jpg'  # 上傳檔名
                                 )  # 先實例上傳檔案物件
        data = self.upload.Upload_file()  # 實作上傳檔案物件方法
        response_data = self.luckyWheelManagement.uploadRewardImage(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        self.upload.Close_file()  # 關閉檔案

    def test_LuckyWheelManagement_relatedApi_status_09(self):
        """驗證 幸运转盘 - 新增活動 狀態"""
        data = self.create_LuckyWheel_mode(self.config.LuckyWheel())
        response_data = self.luckyWheelManagement.createNewEvent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_10(self):
        """驗證 幸运转盘 - 幸運輪盤詳細頁面 狀態"""
        response_data = self.luckyWheelManagement.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_11(self):
        """驗證 幸运转盘 - 幸運輪盤詳細資料 狀態"""
        Id = self.getId()
        data = {"EventID": Id}
        response_data = self.luckyWheelManagement.getEventDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_12(self):
        """驗證 幸运转盘 - 序號管理頁面 狀態"""
        response_data = self.luckyWheelManagement.serialNumber({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_13(self):
        """驗證 幸运转盘 - 序號管理名單 狀態"""
        Id = self.getId()
        data = {"eventID": Id, "skip": 0, "take": 100, "searchNumber": 'null'}
        response_data = self.luckyWheelManagement.getSerialNumberList(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_14(self):
        """驗證 幸运转盘 - 產生序號 狀態"""
        Id = self.getId()
        BeginTime = (datetime.now() + timedelta(hours = -12)).strftime("%Y/%m/%d %H:%M:%S")
        EndTime = (datetime.now() + timedelta(hours = -11)).strftime("%Y/%m/%d %H:%M:%S")
        data = {"EventID": Id, "RaffleCount": 10, "UsageCount": 20, "StartDate": BeginTime,
                "EndDate": EndTime, "BatchCount": 10}
        response_data = self.luckyWheelManagement.createSerialNumber(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_15(self):
        """驗證 幸运转盘 - Portal 抽獎 狀態"""
        Id = self.getId()
        data = {"eventID": Id, "skip": 0, "take": 100}
        response_data = self.luckyWheelManagement.getSerialNumberList(data)  # 1.查詢新增的序號
        serialNumber = response_data[1]['Response'][0]['SerialNumber']  # 2.取得序號
        self.portal = Portal_test()
        self.portal.luckyWheel(self.config.test_Member_config(), self.config.test_Password_config(), Id, serialNumber)
        newData = {"eventID": Id, "skip": 0, "take": 100}
        response_data = self.luckyWheelManagement.getSerialNumberList(newData)  # 4.查詢已使用抽獎序號
        validateData = response_data[1]['Response'][0]['UseRecordCount']
        self.assertEqual(validateData, 1)

    def test_LuckyWheelManagement_relatedApi_status_16(self):
        """驗證 幸运转盘 - 匯出序號管理名單 狀態"""
        Id = self.getId()
        data = {"eventId": Id, "searchNumber": 'null'}
        response_data = self.luckyWheelManagement.exportExcel(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_17(self):
        """驗證 幸运转盘 - 中獎名單頁面 狀態"""
        response_data = self.luckyWheelManagement.rewardRecord({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_18(self):
        """驗證 幸运转盘 - 中獎名單 狀態"""
        Id = self.getId()
        data = {"EventID": Id, "Size": 100}
        response_data = self.luckyWheelManagement.getRewardRecord(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_19(self):
        """驗證 幸运转盘 - 派發獎勵 狀態"""
        Id = self.getId()
        data = {"EventID": Id, "Size": 100}
        response_data = self.luckyWheelManagement.getRewardRecord(data)
        eventId = response_data[1]['Response'][0]['EventID']
        recordsIDs = response_data[1]['Response'][0]['ID']
        data = {"eventID": eventId, "recordIDs": recordsIDs}
        response_data = self.luckyWheelManagement.sendRewards(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_20(self):
        """驗證 幸运转盘 - 中獎名單統計 狀態"""
        Id = self.getId()
        data = {"EventID": Id}
        response_data = self.luckyWheelManagement.getRewardStatistics(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_LuckyWheelManagement_relatedApi_status_21(self):
        """驗證 幸运转盘 - 立即下架 狀態"""
        Id = self.getId()
        data = {"EventID": Id}
        response_data = self.luckyWheelManagement.eventOff(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
