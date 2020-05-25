'''
@Created by loka
@Date : 2019/12/20
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from data_config import master_config
from master_api import system_management
from master_api.account_login import User


class AnyTimeDiscountBaseTest(unittest.TestCase):
    """ 返水設定 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.AnyTimeDiscount = system_management.AnyTimeDiscountSetting(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        response_data = self.AnyTimeDiscount.getList({})
        length = len(response_data[1]['Settings']) - 1
        getId = response_data[1]['Settings'][length]['Id']
        return getId

    def test_AnyTimeDiscount_relatedApi_status_01(self):
        """驗證 返水設定 - 取得看板頁面"""
        response_data = self.AnyTimeDiscount.list({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_02(self):
        """驗證 返水設定 - 取得看板資料"""
        response_data = self.AnyTimeDiscount.getList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_03(self):
        """驗證 返水設定 - 時時返水是否歸零"""
        response_data = self.AnyTimeDiscount.getIsATDResetRunning({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_04(self):
        """驗證 返水設定 - 取得批次返水新增頁面"""
        response_data = self.AnyTimeDiscount.createForBatch({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_05(self):
        """驗證 返水設定 - 新增批次返水資料"""
        data = {"Name": "@QA_automation", "Details": []}
        response_data = self.AnyTimeDiscount.verifyParams(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_06(self):
        """驗證 返水設定 - 時時返水修改頁面"""
        response_data = self.AnyTimeDiscount.modifyForATD({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_07(self):
        """驗證 返水設定 - 時時返水啟用視窗"""
        response_data = self.AnyTimeDiscount.activeDialog({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_08(self):
        """驗證 返水設定 - 新增返水等級"""
        data = {"createParams": {"Name": "@QA_Automation", "Details": []},
                "setting": {"DiscountSettingId": 'null', "EnableAppointment": common_config.EndDay,
                            "DisableAppointment": 'null', "Limit": 10, "Audit": 1, "ReceiveSwitch": 'true',
                            "MaxAmountlimit": 1, "Time": 14, "Type": 2}, "detail": []}
        response_data = self.AnyTimeDiscount.createSubmit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_09(self):
        """驗證 返水設定 - 返水詳細頁面"""
        response_data = self.AnyTimeDiscount.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_10(self):
        """驗證 返水設定 - 返水設定詳細"""
        # step 1 取得Id
        Id = self.getId()
        data = {'id': Id}
        response_data = self.AnyTimeDiscount.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_11(self):
        """驗證 返水設定 - 時時返水設定詳細"""
        # step 1 取得Id
        Id = self.getId()
        data = {'discountSettingId': Id}
        response_data = self.AnyTimeDiscount.getATDSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_12(self):
        """驗證 返水設定 - 更新返水名稱"""
        # step 1 取得Id
        Id = self.getId()
        data = {'Id': Id, "name": '@QA_automation'}
        response_data = self.AnyTimeDiscount.updateName(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_13(self):
        """驗證 返水設定 - 更新一般返水狀態"""
        # step 1 取得Id
        Id = self.getId()
        data = {"id": Id, "isDiscount": 'false'}
        response_data = self.AnyTimeDiscount.updateHasDiscount(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_14(self):
        """驗證 返水設定 - 返水修改頁面"""
        response_data = self.AnyTimeDiscount.modifyForBatch({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_15(self):
        """驗證 返水設定 - 時返歸零視窗"""
        response_data = self.AnyTimeDiscount.resetDialog({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_16(self):
        """驗證 返水設定 - 時時返水歸零"""
        # step 1 取得Id
        Id = self.getId()
        data = {"password": master_config.Master_Password, "discountSettingId": Id}
        response_data = self.AnyTimeDiscount.alterATDResetByDiscountSetting(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_17(self):
        """驗證 返水設定 - 時時返水歸零紀錄"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id, "skip": 0, "take": 10}
        response_data = self.AnyTimeDiscount.getATDResetByDiscountSettingRecord(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_18(self):
        """驗證 返水設定 - 時時返水-娛樂城返水比"""
        # step 1 取得Id
        Id = self.getId()
        data = {"id": Id, "details": []}
        response_data = self.AnyTimeDiscount.updateDetails(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_19(self):
        """驗證 返水設定 - 時時返水-時時返水領取開關"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id, "receiveSwitch": 'false'}
        response_data = self.AnyTimeDiscount.alterATDReceiveSwitch(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_20(self):
        """驗證 返水設定 - 時時返水-時時返水領取開關歷程紀錄"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id, "skip": 0, "take": 10}
        response_data = self.AnyTimeDiscount.getATDWithdrawSwitchLog(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_21(self):
        """驗證 返水設定 - 時時返水啟用/停用期間"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id,
                "EnableAppointment": common_config.EndDay,
                'DisableAppointment': 'null'
                }
        response_data = self.AnyTimeDiscount.alterATDAppointment(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_22(self):
        """驗證 返水設定 - 更新最低領取限額"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id, "limit": 1}
        response_data = self.AnyTimeDiscount.alterATDLimit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_23(self):
        """驗證 返水設定 - 更新單日最高領取限額"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id, "Maxlimint": 1}
        response_data = self.AnyTimeDiscount.alterATDMaxAmountLimit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_24(self):
        """驗證 返水設定 - 取得時時返水娛樂城詳細資料"""
        response_data = self.AnyTimeDiscount.getATDSupplierDetail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_25(self):
        """驗證 返水設定 - 時時返水設定詳細資料"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id}
        response_data = self.AnyTimeDiscount.getATDSettingDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_26(self):
        """驗證 返水設定 - 更新時時返水-返水比"""
        # step 1 取得Id
        Id = self.getId()
        data = {"discountSettingId": Id,
                "viewModel": []}
        response_data = self.AnyTimeDiscount.alterATDPercentages(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_27(self):
        """驗證 返水設定 - 更新備註"""
        # step 1 取得Id
        Id = self.getId()
        data = {"id": Id, "memo": "@QA_automation"}
        response_data = self.AnyTimeDiscount.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AnyTimeDiscount_relatedApi_status_28(self):
        """驗證 返水設定 - 刪除返水等級"""
        # step 1 取得Id
        Id = self.getId()
        data = {"id": Id}
        response_data = self.AnyTimeDiscount.delete(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
