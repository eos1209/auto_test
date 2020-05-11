'''
@Created by loka
@Date : 2020/03/12
'''


# Home
class Home(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getAllMemberLevels(self, data):
        path = '/Home/GetAllMemberLevels'  # 取得所有會員等級
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllDiscountSettings(self, data):
        path = '/Home/GetAllDiscountSettings'  # 取得所有返水等級
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllBanks(self):
        data = {}
        path = '/Home/GetAllBanks'  # 取得所有銀行
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data
