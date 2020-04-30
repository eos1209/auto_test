'''
@Created by loka
@Date : 2019/11/28
'''

import unittest
from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
import random
from data_config import master_config
from data_config.system_config import systemSetting


class AgentCreateTest(unittest.TestCase):
    """新增代理商 - 相關 API 調用狀態"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.AgentCreate = member_and_agent.AgentCreate(self.__http)
        self.AgentSearch = member_and_agent.AgentSearch(self.__http)
        self.AgentDetail = member_and_agent.AgentDetail(self.__http)
        self.MemberSearch = member_and_agent.MemberSearch(self.__http)
        self.MemberCreate = member_and_agent.MemberCreate(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def getCommissionSettingId(self):
        response_data = self.AgentDetail.getAllCommissionSettings({})
        for i in range(len(response_data[1])):
            if self.config.commissionSetting_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def getDiscountSettingId(self):
        response_data = self.AgentDetail.getAllDiscountSettings({})
        for i in range(len(response_data[1])):
            if self.config.DiscountSetting_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def getMemberLevelId(self):
        response_data = self.AgentDetail.getAllMemberLevels({})
        for i in range(len(response_data[1])):
            if self.config.MemberLevelSetting_config() == response_data[1][i]['Text']:
                Id = response_data[1][i]['Value']
                return Id

    def test_AgentCreate_baseApi_status_01(self):
        """驗證 新增代理商 - 頁面狀態"""
        response_data = self.AgentCreate.create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_02(self):
        """驗證 新增代理商 - 檢查並更新所有代理權限"""
        response_data = self.AgentCreate.checkAllUpdateAgentAuthority({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_03(self):
        """驗證 新增代理商 - 是否取得預設密碼"""
        response_data = self.MemberCreate.getDefaultPasswords({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_04(self):
        """驗證 新增代理商 - 是否取得所有代理等級"""
        response_data = self.AgentCreate.get_all_level_with_create({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_05(self):
        """驗證 新增代理商 - 是否取得所有傭金等級"""
        response_data = self.AgentSearch.get_all_commission_settings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_06(self):
        """驗證 新增代理商 - 是否取得所有返水設定"""
        response_data = self.MemberSearch.getAllDiscountSettings({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_07(self):
        """驗證 新增代理商 - 是否取得所有會員等級"""
        response_data = self.AgentSearch.getAllLevel({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_08(self):
        """新增代理商 - 是否取得所有銀行"""
        response_data = self.AgentCreate.get_all_banks({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_09(self):
        """新增代理商 - 驗證代理帳號是否重複-連線"""
        data = {"Account": self.config.agentLv4()}
        response_data = self.AgentCreate.check_agent_account(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_10(self):
        """新增代理商 - 驗證代理帳號是否重複-ErrorMessage"""
        data = {"Account": self.config.agentLv4()}
        response_data = self.AgentCreate.check_agent_account(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '帐号' + '"' + self.config.agentLv4() + '"' + '已存在')  # 帳號"DS_a_player1"已存在

    def test_AgentCreate_baseApi_status_11(self):
        """新增代理商 - 驗證代理是否存在-連線"""
        data = {"level": 3, "account": self.config.agentLv4()}
        response_data = self.AgentCreate.check_parent(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_12(self):
        """新增代理商 - 驗證代理是否存在-ErrorMessage"""
        level = random.randint(1, 3)  # 1:大股東 2:股東 3:總代理 ，亂數測試代理帳號存在
        data = {"level": level, "account": master_config.no_exist_agent}
        response_data = self.AgentCreate.check_parent(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '找不到此上线帐号')

    def test_AgentCreate_baseApi_status_13(self):
        """新增代理商 - 驗證代理是否新增-代理"""
        account = 'QA_Test' + common_config.now  # 代理帳號
        parent = self.config.agentLv3()  # 代理總帳號:DS_1106_1458
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId": self.getMemberLevelId(),  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "光大银行", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": 'QAautomation',  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": "2019/11/04",  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "112233445566",  # 銀行帳號
            "Province": "abc",  # 省分
            "City": "efg",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": "光大银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_AgentCreate_baseApi_status_14(self):
        """新增代理商 - 驗證代理是否新增-總代理 OR 股東"""
        Name = ''
        parent = ''
        account = 'QATest' + common_config.now + '2'  # 代理帳號
        level = random.randint(2, 3)
        if level == 2:
            parent = self.config.agentLv2()
            Name = '股东'
        elif level == 3:
            parent = self.config.agentLv3()
            Name = '总代理'
        data = {
            "agentLevel": {"Level": level, "Name": Name},
            "commissionSettingId": self.getCommissionSettingId(),
            "defaultDiscountSettingId": -1,  # -1代表隱藏
            "defaultMemberLevelSettingId": -1,  # -1代表隱藏
            "GroupBank": {"Id": 14, "Name": "北京银行", "Sort": 14, "AccountFormat": 2},
            "parent": parent,
            "Account": account,
            "BankAccount": "546546546546",
            "Province": "a",
            "City": "b",
            "AgentLevelId": level,
            "ParentAccount": parent,
            "Percent": 0, "BankName": "北京银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    # def test_AgentCreate_baseApi_status_15(self):
    #     """新增代理商 - 驗證代理是否新增-大股東"""
    #     account = 'QATest' + Config.now + '1'  # 代理帳號
    #     data = {
    #         "agentLevel": {"Level": 1, "Name": "大股东"},
    #         "commissionSettingId": "61",
    #         "defaultDiscountSettingId": -1,
    #         "defaultMemberLevelSettingId": -1,
    #         "GroupBank": {"Id": 19, "Name": "广州银行", "Sort": 19, "AccountFormat": 2},
    #         "Account": account,
    #         "BankAccount": "112233445566",
    #         "Province": "a",
    #         "City": "b",
    #         "AgentLevelId": 1,
    #         "Percent": 0, "BankName": "广州银行"}
    #     response_data = self.AgentCreate.createSubmit(data)
    #     status_code = response_data[0]
    #     self.assertEqual(status_code, Config.Status_Code)

    def test_AgentCreate_baseApi_status_16(self):
        """新增代理商 - 驗證QQ欄位是否可以輸入英文"""
        account = 'QATest' + common_config.now + '3'  # 代理帳號
        parent = self.config.agentLv3()  # 代理總帳號:DS_1106_1458
        data = {
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId":self.getMemberLevelId(),  # 預設會員等級
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "QQ": "a123456",  # QQ
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, 'QQ帐号只能为英文或数字')

    def test_AgentCreate_baseApi_status_17(self):
        """新增代理商 - 沒有銀行名稱是否能夠新增"""
        account = 'QATest' + common_config.now + '5'  # 代理帳號
        parent = self.config.agentLv3()  # 代理總帳號:DS_1106_1458
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId": self.getMemberLevelId(),  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": "QATest",  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": common_config.FirstDay,  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "112233445566",  # 銀行帳號
            "Province": "abc",  # 省分
            "City": "efg",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": ""
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '请輸入銀行名稱')

    def test_AgentCreate_baseApi_status_18(self):
        """新增代理商 - 沒有縣市名稱是否能夠新增"""
        account = 'QATest' + common_config.now + '5'  # 代理帳號
        parent = self.config.agentLv3()  # 代理總帳號:DS_1106_1458
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId": self.getMemberLevelId(),  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "光大银行", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": "QAautomation",  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": "2019/11/04",  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "112233445566",  # 銀行帳號
            "Province": "abc",  # 省分
            "City": "",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": "光大银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '请輸入县市')

    def test_AgentCreate_baseApi_status_19(self):
        """新增代理商 - 沒有省分名稱是否能夠新增"""
        account = 'QATest' + common_config.now + '5'  # 代理帳號
        parent = self.config.agentLv3()  # 代理總帳號:DS_1106_1458
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId": self.getMemberLevelId(),  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "光大银行", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": "QAautomation",  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": "2019/11/04",  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "112233445566",  # 銀行帳號
            "Province": "",  # 省分
            "City": "cde",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": "光大银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '请輸入省份')

    def test_AgentCreate_baseApi_status_20(self):
        """新增代理商 - 沒有銀行帳戶是否能夠新增"""
        account = 'QATest' + common_config.now + '5'  # 代理帳號
        parent = self.config.agentLv3()  # 代理總帳號:DS_1106_1458
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId": self.getMemberLevelId(),  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "光大银行", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": "QAautomation",  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": "2019/11/04",  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "",  # 銀行帳號
            "Province": "abc",  # 省分
            "City": "cde",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": "光大银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '请輸入銀行帐号')

    def test_AgentCreate_baseApi_status_21(self):
        """新增代理商 - 代理沒有會員等級設定是否能夠新增"""
        account = 'QATest' + common_config.now + '5'  # 代理帳號
        parent = self.config.agentLv3()  # 代理總帳號:DS_1106_1458
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId": "-1",  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "光大银行", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": "QA_Test",  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": "2019/11/04",  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "112233445566",  # 銀行帳號
            "Province": "",  # 省分
            "City": "cde",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": "光大银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '最後一层的代理商必须选择预设会员等级')

    def test_AgentCreate_baseApi_status_22(self):
        """新增代理商 - 代理沒有返水設定是否能夠新增"""
        account = 'QATest' + common_config.now + '5'  # 代理帳號
        parent = self.config.agentLv3()
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": "-1",  # 預設返水設定
            "defaultMemberLevelSettingId": self.getMemberLevelId(),  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "光大银行", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": "QA_Test",  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": "2019/11/04",  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "112233445566",  # 銀行帳號
            "Province": "",  # 省分
            "City": "cde",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": "光大银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '最後一层的代理商必须选择预设返水设定')

    def test_AgentCreate_baseApi_status_23(self):
        """代理商新增 - 真實姓名混入非中英文 狀態"""
        account = 'QATest' + common_config.now  # 代理帳號
        parent = self.config.agentLv3()
        data = {
            "agentLevel": {"Level": 4, "Name": "代理"},  # 代理等級
            "commissionSettingId": self.getCommissionSettingId(),  # 佣金設定
            "defaultDiscountSettingId": self.getDiscountSettingId(),  # 預設返水設定
            "defaultMemberLevelSettingId": self.getMemberLevelId(),  # 預設會員等級
            "GroupBank": {"Id": 5, "Name": "光大银行", "Sort": 5, "AccountFormat": 2},  # 銀行資訊
            "parent": parent,  # 上層
            "Account": account,  # 代理商帳號
            "Name": 'QA_Test' + common_config.now,  # 真實姓名
            "Mobile": "987654312",  # 手機
            "Sex": "false",  # 性別 true = 男,false = 女
            "Email": "aa@qq.com",  # Email
            "Birthday": "2019/11/04",  # 生日
            "IdNumber": "a123456",  # 微信
            "QQ": "123456",  # QQ
            "Memo": "@auto_test",  # 備註
            "BankAccount": "112233445566",  # 銀行帳號
            "Province": "abc",  # 省分
            "City": "efg",  # 縣市
            "AgentLevelId": 4,  # 代理等級
            "ParentAccount": parent,  # 上層帳號
            "Percent": 0, "BankName": "光大银行"
        }
        response_data = self.AgentCreate.create_submit(data)
        errorMessage = response_data[1]['ErrorMessage']
        self.assertEqual(errorMessage, '姓名只允许中英文，與全、半形英文句號')


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
