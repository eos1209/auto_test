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
from data_config import master_config


class MemberTagsTest(unittest.TestCase):
    """會員標籤 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.memberTags = member_and_agent.MemberTags(self.__http)
        self.user.login()

    def test_MemberTags_relatedApi_status_01(self):
        """會員標籤 - 取得所有標籤 狀態"""
        response_data = self.memberTags.getTags({})
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTags_relatedApi_status_02(self):
        """會員標籤 - 新增標籤 狀態"""
        data = {
            'newTag': 'QA_automation',
            'memberTagId': '',
            'account': master_config.Account
        }
        response_data = self.memberTags.addMemberTag(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_MemberTags_relatedApi_status_03(self):
        """會員標籤 - 刪除標籤 狀態"""
        # 呼叫取得會員標籤 API 後取最後一筆資料
        TagsId = self.GetLastMemberTags()
        data = {'account': master_config.Account,
                'memberTagId': TagsId}
        response_data = self.memberTags.removeMamberTag(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def GetLastMemberTags(self):
        getMemberTagsData = self.memberTags.getTags({})
        for i in range(len(getMemberTagsData[1]['ReturnObject'])):
            if getMemberTagsData[1]['ReturnObject'][i]['Name'] == master_config.memberTags:
                getTagsId = getMemberTagsData[1]['ReturnObject'][i]['Id']
                return getTagsId


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
