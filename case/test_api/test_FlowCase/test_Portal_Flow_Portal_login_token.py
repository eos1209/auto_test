'''
@Created by loka
@Date : 2020/05/22
'''
import unittest
from requests.cookies import RequestsCookieJar
from base.HTMLTestReportCN import HTMLTestRunner
import requests
import re
from base.httpRequest import cookie_process
from base.CommonMethod import Portal_test
from data_config.system_config import systemSetting
from portal_api.portal_api import Portal_api
import json


def json_format(data):  # json資料轉換
    json_data = json.dumps(data)
    return json_data


def login_07():
    login = requests.get('http://www.jp777.net/')
    getToken = re.search('(_RequestVerificationToken" type="hidden" value=")(.*?)(" />)', login.text)
    Token = getToken.group(2)
    cookie = requests.utils.dict_from_cookiejar(login.cookies)
    Portal_Headers_request = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'c8763': Token,
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest",
    }
    getCode = requests.post('http://www.jp777.net' + '/Home/GetCaptchaForLogin', data = {},
                            headers = Portal_Headers_request, cookies = cookie)
    getImg = getCode.json()
    data = {"account": 'QA_YT0007999982', "password": 'a654321',
            "checkCode": "e5466e48e20e4944a0bdaa6bac351c8d",
            "checkCodeEncrypt": getImg['value'],
            # "fingerprint": "0f7dcb0d1f847f355a7d518c969e4ecd",
            # "signalRId": "13f9acc5-00e6-480f-a58a-e9e628dc429e"
            }
    response_data = requests.post('http://www.jp777.net' + '/login/login',
                                  data = json_format(data),
                                  headers = Portal_Headers_request, cookies = cookie
                                  )
    cookie = requests.utils.dict_from_cookiejar(response_data.cookies)
    return cookie


class test_Portal_token(unittest.TestCase):
    def setUp(self):
        self.config = systemSetting()  # 系統參數

    def tearDown(self):
        pass

    def test_oldCookie(self):
        """驗證-登入成功之後更改成舊token是否被登出"""
        self.portal = Portal_test()
        self.portal_api = Portal_api()
        login = self.portal.login(self.config.test_Member_config(),
                                  self.config.test_Password_config())  # 登入後cookie
        # print(type(login))
        get_cookie = cookie_process(login)
        cookie_update = RequestsCookieJar()
        cookie_update.set('protalnew', get_cookie['portalnew'])  # 加入舊Token
        get_cookie.update(cookie_update)
        get_cookie.pop('portalnew')  # 刪除新的Token
        get_cookie = RequestsCookieJar()
        # print(type(get_cookie))
        data = {"Subject": "dfgdfg", "MailBody": "<p>dfgdfgdfgfd</p>\n"}
        response_data = self.portal_api.portal_siteMail_error(data, get_cookie)
        validate = '302'
        self.assertEqual(validate, response_data[0])

    # def test_cookie_attack(self):
    #     self.portal = Portal_test()
    #     cookie_07 = login_07()
    #     self.portal_api = Portal_api()
    #     login = self.portal.login(self.config.test_Member_config(),
    #                               self.config.test_Password_config())  # 登入後cookie
    #
    #     print(cookie_07['.ASPXAUTHFORPORTAL'])
    #     login = RequestsCookieJar()
    #     login.pop('.ASPXAUTHFORPORTAL')
    #     cookie_update = RequestsCookieJar()
    #     cookie_update.set('.ASPXAUTHFORPORTAL',cookie_07['.ASPXAUTHFORPORTAL'])
    #     login.update(cookie_update)
    #     print(login)
    #     # cookie_update.set('protalnew', ['portalnew'])  # 加入舊Token
    #     # data = {"Subject": "dfgdfg", "MailBody": "<p>dfgdfgdfgfd</p>\n"}
    #     # response_data = self.portal_api.portal_siteMail_error(data, cookie_07)  # 跨網站攻擊
    #     # validate = '302'
    #     # self.assertEqual(validate, response_data[0])


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
