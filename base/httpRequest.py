'''
@Created by yuhsiang
@Date : 2018/12/10
'''
import requests
from requests.cookies import RequestsCookieJar
from data_config import master_config
from data_config.system_config import systemSetting


def send_get_Portal_request(path, payload, Headers, cookies):
    config = systemSetting()
    base_url = config.Portal_config() + path
    r = requests.get(base_url, params = payload, headers = Headers, cookies = cookies)
    status_code = r.status_code  # 獲取返回狀態碼
    response_text = r.text
    return str(status_code), response_text, r.cookies  # 返回響應碼，内容


def send_post_Portal_request(path, payload, Headers, cookies):
    config = systemSetting()
    base_url = config.Portal_config() + path
    r = requests.post(base_url, json = payload, headers = Headers, cookies = cookies)
    status_code = r.status_code  # 獲取返回狀態碼
    response_text = r.json()
    return str(status_code), response_text, r.cookies  # 返回響應碼，内容


def send_error_post_Portal_request(path, payload, Headers, cookies):
    config = systemSetting()
    base_url = config.Portal_config() + path
    r = requests.post(base_url, json = payload, headers = Headers, cookies = cookies, allow_redirects = False)
    status_code = r.status_code  # 獲取返回狀態碼
    response_text = r.text
    return str(status_code), response_text, r.cookies  # 返回響應碼，内容


def cookie_process(cookie_jar):  # 處理登入後的cookie
    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    return cookie


def add_cookie(login_cookie, get_cookie):  # 上一頁假的RequestVerificationToken必須加在新的cookie一起回傳
    set_RequestVerificationToken_value = get_cookie['__RequestVerificationToken']
    set_request = requests.cookies.RequestsCookieJar()
    set_request.set('__RequestVerificationToken', set_RequestVerificationToken_value)
    login_cookie.update(set_request)
    return login_cookie


class HttpRequest(object):
    # Cookies = {}

    def __init__(self):

        self.Cookies = {}
        self.config = systemSetting()  # 參數設定

    def send_get_request(self, base_url, payload, Headers):
        r = requests.get(base_url, params = payload, headers = Headers, cookies = self.Cookies)
        status_code = r.status_code  # 獲取返回狀態碼
        response_text = r.text
        return str(status_code), response_text, r.cookies  # 返回響應碼，内容

    def send_post_request(self, base_url, payload, Headers):
        r = requests.post(base_url, json = payload, headers = Headers, cookies = self.Cookies)
        status_code = r.status_code  # 獲取返回狀態碼
        # if status_code == 200:
        #     if r.json() is not None:
        #         response_json = r.json()  # 響應内容，json類型轉化成python數據類型
        #     else:
        #         response_json = {}
        # else:
        #     response_json = r.content
        if r.content:
            response_json = r.json()  # 響應内容，json類型轉化成python數據類型
            response_time = r.elapsed.total_seconds()
        else:
            response_json = r.content
            response_time = r.elapsed.total_seconds()
        print(r.elapsed.total_seconds())
        r.close()
        return str(status_code), response_json, r.cookies, response_time  # 返回響應碼，内容

    def send_post_request_for_file(self, base_url, file, Headers):
        r = requests.post(base_url, files = file, headers = Headers, cookies = self.Cookies)
        status_code = r.status_code  # 獲取返回狀態碼
        if r.content:
            response_json = r.json()  # 響應内容，json類型轉化成python數據類型
        else:
            response_json = r.content
            print(status_code, response_json)
        r.close()
        return str(status_code), response_json, r.cookies  # 返回響應碼，内容

    """
    <summary>
    Master 皆用此方法調用
    """

    def sendRequest(self, method, path, data):
        base_url = self.config.Master_config() + path
        if method == "GET":
            response_data = self.send_get_request(base_url, data, master_config.Get_Mater_Headers)
        elif method == "POST":
            response_data = self.send_post_request(base_url, data, master_config.Post_Master_Headers)
        return response_data

    def sendRequestForUploadFile(self, path, data):
        base_url = self.config.Master_config() + path
        response_data = self.send_post_request_for_file(base_url, data, master_config.Post_headers_upLoadFile)
        return response_data
