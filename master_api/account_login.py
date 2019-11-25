'''
@Created by yuhsiang
@Date : 2018/12/10
'''

from data_config import master_config


class User(object):

    def __init__(self, http):
        self.__http = http
        self.__connectionId = {}

    def login(self):
        path = '/Account/ValidateAccount'
        data = {'account': master_config.Master_Account, 'password': master_config.Master_Password}
        response_data = self.__http.sendRequest('POST', path, data)
        self.__http.Cookies = response_data[2]

    def info(self):
        # 取得資訊
        path = '/signalr/negotiate'
        data = {}
        response_data = self.__http.sendRequest('POST', path, data)
        self.__connectionId = response_data[1]['ConnectionId']
        return self.__connectionId

    def logout(self):
        path = '/Account/SignOut'
        data = {}
        self.__http.sendRequest('GET', path, data)
