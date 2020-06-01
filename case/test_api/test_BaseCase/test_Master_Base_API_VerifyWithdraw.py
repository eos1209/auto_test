'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from data_config import common_config
from master_api import account_management
from master_api.account_login import User
from master_api import member_and_agent
from base.CommonMethod import SetDelayTime
from data_config.system_config import systemSetting
from base.CommonMethod import Portal_test
import time

class VerifyWithdrawBaseTest(unittest.TestCase):
    """ 取款申请审核 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 參數設定
        # self.__http = HttpRequest()
        # self.user = User(self.__http)
        # self.verifyWithdraw = account_management.VerifyWithdraw(self.__http)
        # self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細資料
        # self.user.login()

    @classmethod
    def Master_login(cls):
        cls.__http = HttpRequest()
        cls.user = User(cls.__http)
        cls.verifyWithdraw = account_management.VerifyWithdraw(cls.__http)
        cls.memberDetail = member_and_agent.MemberDetail(cls.__http)  # 會員詳細資料
        cls.user.login()

    def tearDown(self):
        self.user.logout()

    def getId(self):
        SetDelayTime()
        data = {"count": 100, "query": {"search": 'null'}}
        response_data = self.verifyWithdraw.load(data)
        getId = response_data[1]['Data'][0]['Id']
        return getId

    def member_id(self):
        data = {"connectionId": self.user.info(), "account": self.config.test_Member_config()}
        response_data = self.memberDetail.getDetail(data)
        return response_data[1]['Member']['Id']

    def test_VerifyWithdraw_relatedApi_status_01(self):
        """驗證 取款申请审核 - 取得頁面"""
        VerifyWithdrawBaseTest.Master_login()  # Master登入
        response_data = self.verifyWithdraw.index({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_02(self):
        """驗證 取款申请审核 - 取得詳細資料"""
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verifyWithdraw.load(data)
        get_verify_withdraw_id = response_data[1]['Data'][0]['Id']

        data = {"id": get_verify_withdraw_id,
                "connectionId": self.user.info()}
        response_data = self.verifyWithdraw.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_03(self):
        """驗證 取款申请审核 - 匯出"""
        data = {"search": None}
        response_data = self.verifyWithdraw.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_04(self):
        """驗證 取款申请审核 - 取得訂單狀態"""
        response_data = self.verifyWithdraw.getApplyStates({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_05(self):
        """驗證 取款申请审核 - 取得詳細頁面"""
        response_data = self.verifyWithdraw.detail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_06(self):
        """驗證 取款申请审核 - 取得列表資料"""
        data = {"count": 100,
                "query":
                    {"search": None}
                }
        response_data = self.verifyWithdraw.load(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_07(self):
        """驗證 取款申请审核 - 人工出款"""
        data = {"id": self.member_id()}
        response_data = self.memberDetail.resetMoneyPassword(data)
        getMoneyPassword = response_data[1]['MoneyPassword']
        self.portal = Portal_test()
        self.portal.verifyDraw(self.config.test_Member_config(), self.config.test_Password_config(), getMoneyPassword)
        VerifyWithdrawBaseTest.Master_login()
        Id = self.getId()
        data = {"id": Id}
        response_data = self.verifyWithdraw.allow(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_08(self):
        """驗證 取款申请审核 - 退回"""
        data = {"id": self.member_id()}
        response_data = self.memberDetail.resetMoneyPassword(data)
        getMoneyPassword = response_data[1]['MoneyPassword']
        self.portal = Portal_test()
        self.portal.verifyDraw(self.config.test_Member_config(), self.config.test_Password_config(),
                               getMoneyPassword)  # PS:該登入會員必須先設定好銀行帳戶+支付寶帳戶
        VerifyWithdrawBaseTest.Master_login()
        Id = self.getId()
        data = {"id": Id}
        response_data = self.verifyWithdraw.deny(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_09(self):
        """驗證 取款申请审核 - 拒絕"""
        data = {"id": self.member_id()}
        response_data = self.memberDetail.resetMoneyPassword(data)
        getMoneyPassword = response_data[1]['MoneyPassword']
        self.portal = Portal_test()
        self.portal.verifyDraw(self.config.test_Member_config(), self.config.test_Password_config(),
                               getMoneyPassword)
        VerifyWithdrawBaseTest.Master_login()
        Id = self.getId()
        data = {"id": Id}
        response_data = self.verifyWithdraw.reject(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_10(self):
        """取款申请审核-取得搜尋取款申请條件框頁面 狀態"""
        response_data = self.verifyWithdraw.detailDialog({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_11(self):
        """取款申请审核-取得取款審核申請詳細資料 狀態"""
        Id = self.getId()
        data = {"id": Id, "connectionId": self.user.info()}
        response_data = self.verifyWithdraw.getDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_12(self):
        """取款申请审核-取得可使用代付列表 狀態"""
        response_data = self.verifyWithdraw.getUseList({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_13(self):
        """取款申请审核-檢視代付歷程 狀態"""
        Id = self.getId()
        data = {"withdrawApplicationId": Id}
        response_data = self.verifyWithdraw.getHistories(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_14(self):
        """取款申请审核-更新交易紀錄的前台備注 狀態"""
        Id = self.getId()
        data = {"id": Id, "portalMemo": "@QA_automation"}
        response_data = self.verifyWithdraw.updatePortalMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_15(self):
        """取款申请审核-更新交易紀錄備注 狀態"""
        Id = self.getId()
        data = {"id": Id, "Memo": "@QA_automation"}
        response_data = self.verifyWithdraw.updateMemo(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_16(self):
        """取款申请审核-取得稽核明細頁面"""
        response_data = self.verifyWithdraw.auditDetail({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_17(self):
        """取款申请审核-取得稽核明細詳細資料 狀態"""
        Id = self.getId()
        data = {"id": Id}
        response_data = self.verifyWithdraw.getAuditDetail(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_18(self):
        """取款申请审核-結束檢視 狀態"""
        Id = self.getId()
        data = {"id": Id}
        response_data = self.verifyWithdraw.exitReadWithdraw(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_VerifyWithdraw_relatedApi_status_19(self):
        """取款申请审核-取得檢視者 狀態"""
        Id = self.getId()
        data = {"id": Id}
        response_data = self.verifyWithdraw.getViewers(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)
    #
    # def test_VerifyWithdraw_relatedApi_status_20(self):
    #     VerifyWithdrawBaseTest.Master_login()  # Master登入
    #     for i in range(300):
    #         data = {"count": 100,
    #                 "query": {"search": "true", "_": int(time.time()), "States": [1], "IsCheckStates": 'true'}}
    #         response_data = self.verifyWithdraw.load(data)
    #         for j in range(100):
    #             getId = response_data[1]['Data'][j]['Id']
    #             data = {"id": getId}
    #             self.verifyWithdraw.deny(data)




if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
