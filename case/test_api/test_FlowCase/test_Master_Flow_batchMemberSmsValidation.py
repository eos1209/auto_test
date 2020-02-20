'''
@Created by loka
@Date : 2020/02/13
'''
import unittest
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import member_and_agent
from master_api.account_login import User
from base.CommonMethod import SetDelayTime
from master_api import system_management
from data_config.system_config import systemSetting


class batchMemberSmsValidationTest(unittest.TestCase):
    """簡訊驗證批次 - 驗證流程 狀態"""

    # 前置作業:站台系統值設定需要打開簡訊驗證開關
    # step 1:先以會員等級QA_Test搜尋作為批次資料
    # step 2:批次執行簡訊驗證
    # step 3:驗證-1:走訪每一位該等級會員是否確實簡訊驗證符合動作
    # step 4:驗證-2:走訪每一位該等級會員的會員歷史紀錄確定要有該開關紀錄
    # step 5:關閉簡訊驗證開關
    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.SystemInfo = system_management.SystemInfo(self.__http)  # 簡訊驗證
        self.memberBatch = member_and_agent.MemberBatch(self.__http)  # 會員批次
        self.memberDetail = member_and_agent.MemberDetail(self.__http)  # 會員詳細
        self.searchMember = member_and_agent.MemberSearch(self.__http)  # 會員搜尋
        self.memberTags = member_and_agent.MemberTags(self.__http)  # 會員標籤
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def GetLastMemberTags(self):
        getMemberTagsData = self.memberTags.getTags({})
        for i in range(len(getMemberTagsData[1]['ReturnObject'])):
            if getMemberTagsData[1]['ReturnObject'][i]['Name'] == self.config.singleTag_config():
                getTagsId = getMemberTagsData[1]['ReturnObject'][i]['Id']
                return getTagsId

    def test_MemberSmsValidation(self):
        # 簡訊驗證開啟
        # step 1:先以會員等級QA_Test搜尋作為批次資料
        # step 2:批次執行簡訊驗證
        data = {"search": {"MemberTagIds": self.GetLastMemberTags()}, "isSuper": 'false',
                "batchParam": {"isAll": 'true'},
                "isEnable": 'true'}
        print(self.memberBatch.batchUpdateMemberSmsValidation(data))
        # step 3:驗證-1:走訪每一位該等級會員是否確實簡訊驗證符合動作
        # step 4:驗證-2:走訪每一位該等級會員的會員歷史紀錄確定要有該開關紀錄
        data = {"MemberTagIds": self.GetLastMemberTags()}
        response_data = self.searchMember.getSearchCount(data)  # 計算總筆數
        memberTotal = response_data[1]['ReturnObject']
        print(memberTotal)
        if memberTotal % 10 == 0:  # 判斷是否為整數
            memberPageCount = memberTotal / 10
        else:
            memberPageCount = (memberTotal / 10) + 1
        for page in range(int(memberPageCount)):
            data = {"MemberTagIds": self.GetLastMemberTags(), "pageIndex": page,
                    "connectionId": self.user.info()}
            response_data = self.searchMember.search(data)
            for count in range(len(response_data[1]['PageData'])):
                Id = response_data[1]['PageData'][count]['Id']
                Name = response_data[1]['PageData'][count]['Account']
                validateMemberDetail = self.MemberDetail(Name)
                validateMemberHistory = self.MemberHistory(Id)
                if bool(validateMemberDetail != validateMemberHistory):
                    self.assertNotEqual('會員詳細:' + str(validateMemberDetail), '會員歷史紀錄' + validateMemberHistory,
                                        '發生錯誤，兩者狀況不一')
                    # print (page)
                else:
                    self.assertEqual(validateMemberDetail, validateMemberHistory)
            SetDelayTime()

    def MemberDetail(self, Name):
        data = {"connectionId": self.user.info(), "account": Name}
        response_data = self.memberDetail.getDetail(data)
        validateData = response_data[1]['Member']['IsSmsValidation']
        return validateData

    def MemberHistory(self, Id):
        data = {"id": Id, "take": 100, "skip": 0, "query": {}}
        response_data = self.memberDetail.loadHistory(data)
        validateData = '异动手机简讯验证开关 -> 【开启】'
        if validateData == response_data[1][0]['Content']:
            return 'True'
        else:
            return 'False'


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
