'''
@Created by loka
@Date : 2020/05/14
'''
from base.httpRequest import send_get_Portal_request
from base.httpRequest import send_post_Portal_request
from base.httpRequest import send_error_post_Portal_request
from base.httpRequest import cookie_process
from base.httpRequest import add_cookie
import re

from data_config.system_config import systemSetting


# Home
def headers(url, cookie):  # 處理標頭部分
    get_token = send_get_Portal_request(url, {}, {}, cookie)
    getToken = re.search('(_RequestVerificationToken" type="hidden" value=")(.*?)(" />)', get_token[1])
    Token = getToken.group(2)
    cookies = add_cookie(cookie, get_token[2])
    Portal_Headers_request = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'c8763': Token,
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest",
    }
    return Portal_Headers_request, cookies


class Portal_api(object):
    def __init__(self):
        self.response_data = {}
        self.config = systemSetting()  # 參數設定

    def get_trail_image(self):  # 取得免費試玩圖片
        get_path = '/'
        header = headers(get_path, {})
        path = '/Home/GetCaptchaForLogin'
        self.response_data = send_post_Portal_request(path, {}, header[0], header[1])
        return self.response_data

    def portal_trial(self, data):
        get_path = '/'
        header = headers(get_path, {})
        path = '/Trial/ApplySubmit'
        self.response_data = send_post_Portal_request(path, data, header[0], header[1])
        return self.response_data

    def get_login_image(self):  # 取得驗證圖片
        get_path = '/'
        header = headers(get_path, {})
        path = '/Home/GetCaptchaForLogin'
        self.response_data = send_post_Portal_request(path, {}, header[0], header[1])
        return self.response_data

    def get_register_image(self):  # 取得註冊驗證圖片
        get_path = '/Register'
        header = headers(get_path, {})
        path = '/Home/GetCaptchaForRegister'
        self.response_data = send_post_Portal_request(path, {}, header[0], header[1])
        return self.response_data

    def portal_login(self, data):  # Portal登入
        get_path = '/'
        header = headers(get_path, {})
        path = '/login/login'
        self.response_data = send_post_Portal_request(path, data, header[0], header[1])
        return self.response_data

    def portal_register(self, data):
        get_path = '/Register'
        header = headers(get_path, {})
        path = '/Register/Submit'
        self.response_data = send_post_Portal_request(path, data, header[0], header[1])
        return self.response_data

    def portal_verifyDraw(self, data, cookie):  # 取款申請審核
        cookie = cookie_process(cookie)
        get_path = '/WithdrawApplication'
        header = headers(get_path, cookie)
        path = '/WithdrawApplication/Apply'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_changePassword(self, data, cookie):  # 更改密碼
        cookie = cookie_process(cookie)
        get_path = '/Account/ChangePassword'
        header = headers(get_path, cookie)
        path = '/Account/ChangePasswordSubmit'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_setBankAccount(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/WithdrawApplication'
        header = headers(get_path, cookie)
        path = '/WithdrawApplication/UpdateBankAccount'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_resetMoneyPassword(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/Account/ChangeMoneyPassword'
        header = headers(get_path, cookie)
        path = '/Account/ChangeMoneyPasswordSubmit'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_siteMail(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/SiteMail'
        header = headers(get_path, cookie)
        path = '/SiteMail/SendMail'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_siteMail_error(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/SiteMail'
        header = headers(get_path, cookie)
        path = '/SiteMail/SendMail'
        self.response_data = send_error_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_CompanyDeposit(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/CompanyDeposit/NewIndex'
        header = headers(get_path, cookie)
        path = '/CompanyDeposit/Apply'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_OnlineDeposit_Create_V2(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/OnlineDeposit/Payment?type=General'
        header = headers(get_path, cookie)
        path = '/OnlineDeposit/Create_V2'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_OnlineDeposit_Send_V2(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/OnlineDeposit/Payment?type=General'
        header = headers(get_path, cookie)
        path = '/OnlineDeposit/Send_V2'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_Get_RedEnvelopeList(self, data, cookie):
        cookie = cookie_process(cookie)
        get_path = '/'
        header = headers(get_path, cookie)
        path = '/RedEnvelope/GetRedEnvelopList'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_RedEnvelope_Recevied(self, data, cookie):  # 前台接收紅包
        cookie = cookie_process(cookie)
        get_path = '/'
        header = headers(get_path, cookie)
        path = '/RedEnvelope/Received'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_GetMemberDiscountDetail(self, data, cookie):  # 前台領取時返詳細
        cookie = cookie_process(cookie)
        get_path = '/'
        header = headers(get_path, cookie)
        path = '/AnyTimeDiscount/GetMemberDiscountDetail'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_ReceiveMemberAnyTimeDiscount(self, data, cookie):  # 前台領取時返
        cookie = cookie_process(cookie)
        get_path = '/'
        header = headers(get_path, cookie)
        path = '/AnyTimeDiscount/ReceiveMemberAnyTimeDiscount'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_LuckyWheel_inputSerialNumber(self, data, cookie):  # 幸運輪盤 - 輸入抽獎序號
        cookie = cookie_process(cookie)
        get_path = '/LuckyWheel'
        header = headers(get_path, cookie)
        path = '/LuckyWheel/InputSerialNumber'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_LuckyWheel_startRaffle(self, data, cookie):  # 幸運輪盤 - 開始旋轉
        cookie = cookie_process(cookie)
        get_path = '/LuckyWheel'
        header = headers(get_path, cookie)
        path = '/LuckyWheel/StartRaffle'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_NewLuckyWheel_startRaffle(self, data, cookie):  # 時來運轉 - 開始旋轉
        cookie = cookie_process(cookie)
        get_path = '/NewLuckyWheel'
        header = headers(get_path, cookie)
        path = '/NewLuckyWheel/StartRaffle'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_missionReward(self,data,cookie,Id):
        cookie = cookie_process(cookie)
        get_path = '/MissionReward'
        header = headers(get_path, cookie)
        path = '/MissionReward/GetMissions/'+str(Id)
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

    def portal_missionReward_CompleteMission(self,data,cookie):
        cookie = cookie_process(cookie)
        get_path = '/MissionReward'
        header = headers(get_path, cookie)
        path = '/MissionReward/CompleteMission'
        self.response_data = send_post_Portal_request(path, data, header[0], cookie)
        return self.response_data

