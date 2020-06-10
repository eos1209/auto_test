'''
@Created by loka
@Date : 2020/06/09
'''
import requests
import abc


class HttpRequest_interface(metaclass = abc.ABCMeta):  # 建立http介面
    @abc.abstractmethod
    def get(self, *args):
        pass

    @abc.abstractmethod
    def post(self, *args):
        pass


class Agent_Http(HttpRequest_interface):  # Agent的http方法繼承(inherit) http介面
    def get(self, *args):
        r = requests.get(args[0], params = args[1], headers = args[2], cookies = args[3])
        status_code = r.status_code  # 獲取返回狀態碼
        response_text = r.text
        return str(status_code), response_text, r.cookies  # 返回響應碼，内容

    def post(self, *args):
        r = requests.post(args[0], json = args[1], headers = args[2], cookies = args[3])
        status_code = r.status_code  # 獲取返回狀態碼
        if r.content:
            response_json = r.json()  # 響應内容，json類型轉化成python數據類型
        else:
            response_json = r.content
        return str(status_code), response_json, r.cookies  # 返回響應碼，内容

    def post_login(self, *args):
        r = requests.post(args[0], json = args[1], headers = args[2], cookies = args[3], allow_redirects = False)
        status_code = r.status_code  # 獲取返回狀態碼
        response_json = r.content
        return str(status_code), response_json, r.cookies  # 返回響應碼，内容
