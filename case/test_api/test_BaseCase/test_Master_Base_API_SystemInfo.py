'''
@Created by loka
@Date : 2020/01/02
'''
import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import system_management
from master_api.account_login import User


class SystemInfoBaseTest(unittest.TestCase):
    """ 站台系統值設置 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.SystemInfo = system_management.SystemInfo(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_SystemInfo_relatedApi_status_01(self):
        """驗證 站台系統值設置 - 取得列表頁面"""
        response_data = self.SystemInfo.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_02(self):
        """驗證 站台系統值設置 - 取得會員狀態"""
        response_data = self.SystemInfo.getMemberStates({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_03(self):
        """驗證 站台系統值設置 - 取得站台系統值設置"""
        response_data = self.SystemInfo.getAll({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_04(self):
        """驗證 站台系統值設置 - 代理管端系统客服"""
        data = {"NewValue": "http://www.google.com.tw"}
        response_data = self.SystemInfo.updateAgentCustomerService(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_05(self):
        """驗證 站台系統值設置 - 更新會員登入驗證碼類型"""
        data = {"NewValue": "1"}
        response_data = self.SystemInfo.updateCaptchaTypeLogin(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_06(self):
        """驗證 站台系統值設置 - 更新密碼錯誤次數"""
        data = {"NewValue": 5}
        response_data = self.SystemInfo.updatePortalLoginFailTimesLimit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_07(self):
        """驗證 站台系统值设置-更新區域驗證"""
        data = {"newValue": 'false'}
        response_data = self.SystemInfo.updateLoginRegionValidationEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_08(self):
        """驗證 站台系统值设置-更新跨區驗證鎖頭"""
        data = {"newValue": 'false'}
        response_data = self.SystemInfo.updateLockOtherRegion(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_09(self):
        """驗證 站台系统值设置-更新簡訊驗證"""
        data = {"newValue": 'false'}
        response_data = self.SystemInfo.updateLoginSmsValidationEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_10(self):
        """驗證 站台系统值设置-更新二次驗證"""
        data = {"newValue": 'false'}
        response_data = self.SystemInfo.updateLoginGoogleAuthenticatorEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_11(self):
        """驗證 站台系统值设置-更新會員登入圖片驗證"""
        data = {"newValue": 'false'}
        response_data = self.SystemInfo.updatePortalNeedNeCaptcha(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_12(self):
        """驗證 站台系统值设置-更新會員註冊驗證碼類型"""
        data = {"NewValue": "1"}
        response_data = self.SystemInfo.updateCaptchaTypeRegister(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_13(self):
        """驗證 站台系统值设置-更新問答驗證"""
        data = {"NewValue": 'false'}
        response_data = self.SystemInfo.updateRobotQuestionRegister(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_14(self):
        """驗證 站台系统值设置-更新會員註冊圖片驗證"""
        data = {"NewValue": 'false'}
        response_data = self.SystemInfo.updatePortalNeedNeCaptchaForRegister(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_15(self):
        """驗證 站台系统值设置-更新未投注會員管理"""
        data = {"NewValue": 'false'}
        response_data = self.SystemInfo.updateMemberNoBetEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_16(self):
        """驗證 站台系统值设置-更新未投注會員管理狀態"""
        data = {"noBetDays": 120, "noBetStatusId": 4}
        response_data = self.SystemInfo.updateMemberNoBetDayAndStatus(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_SystemInfo_relatedApi_status_17(self):
        """驗證 站台系统值设置-更新郵件驗證"""
        data = {"newValue": 'false'}
        response_data = self.SystemInfo.updateLoginEmailValidationEnable(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        data = {"newValue": 'True'}
        self.SystemInfo.updateLoginEmailValidationEnable(data)

    def test_SystemInfo_relatedApi_status_18(self):
        """驗證 站台系统值设置-更新裝置驗證"""
        data = {"newValue": 'True'}
        response_data = self.SystemInfo.updateGpkAuthenticator(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
        data = {"newValue": 'False'}
        self.SystemInfo.updateGpkAuthenticator(data)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
