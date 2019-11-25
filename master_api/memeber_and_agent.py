'''
@Created by yuhsiang
@Date : 2019/5/20
'''
from master_api.account_login import User


# 会员查询
class MemberSearch(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def query_page(self):
        path = '/Member/Query'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def search(self, data):
        path = '/Member/Search'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_detail(self, data):
        path = '/Member/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def account_balance(self, data):
        path = '/Member/SumBalance'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_deposit_withdraw_info(self, data):
        path = '/Member/GetDepositWithdrawInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_audit_detail(self, data):
        path = '/Member/GetAuditDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def load_history(self, data):
        path = '/Member/LoadHistory'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def update_bank_account(self, data):
        # API Name =>会员新增&查询-更新銀行帳户
        # body--/{memberAccount}/{updateBankAccountParams}
        path = '/Member/UpdateBankAccount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 人工存款
class MemberDeposit(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def deposit_page(self):
        # 人工存入頁面
        path = '/Member/Deposit'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_deposit_audit_types(self):
        # 取得人工存入稽核方式
        path = '/Member/GetDepositAuditTypes'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_manual_member_types(self):
        # 取得人工存入可選類型
        path = '/Member/GetManualMemberTypes'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_deposit_limit(self):
        # 取得人工存入限額
        path = '/Member/GetDepositLimit'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deposit_token(self):
        # 取得存款的 Token
        path = '/Member/DepositToken'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deposit_submit(self, data):
        # 送出
        path = '/Member/DepositSubmit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 人工提款
class MemberWithdraw(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def withdraw_page(self):
        # 人工提出頁面
        path = '/Member/Withdraw'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def withdraw_init(self, data):
        # 人工提出初始化
        path = '/Member/WithdrawInit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def withdraw_submit(self, data):
        # 人工提出送出
        path = '/Member/WithdrawSubmit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 代理商查询
class AgentSearchPage(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def query(self):
        # 取得代理商查詢頁面
        path = '/Agent/Query'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_all_level(self, data):
        # 取得所有代理層級
        path = '/Agent/GetAllLevel'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_member_levels(self, data):
        # 取得所有會員層級
        path = '/Home/GetAllMemberLevels'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_discount_settings(self, data):
        # 取得所有返水等級
        path = '/Home/GetAllDiscountSettings'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_commission_settings(self, data):
        # 取得所有佣金設定
        path = '/Agent/GetAllCommissionSettings'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 代理商詳細
class AgentDetail(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def detail(self):
        # 代理商查詢 - 取得代理詳細資料頁面
        path = '/Agent/Detail'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail(self, data):
        # 代理詳細資訊
        path = '/Agent/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def disable(self, data):
        # 停用此代理帳號
        path = '/Agent/Disable'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def active(self, data):
        # 啟用此代理帳號
        path = '/Agent/Active'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 新增会员


# 会员汇入


# 新增代理商
class AgentCreate(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def get_default_passwords(self, data):
        # 預設代理商密碼123456
        path = 'Member/GetDefaultPasswords'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create(self):
        # 取得新增代理商頁面
        path = '/Agent/Create'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_all_level_with_create(self, data):
        # 新增時取得所有代理層級
        path = '/Agent/GetAllLevelWithCreate'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_banks(self, data):
        # 銀行資訊-新增時取得所有銀行名稱
        path = '/Home/GetAllBanks'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def check_agent_account(self, data):
        # 代理商查詢 - 檢查新增代理帳號是否已存在
        path = '/Agent/CheckAgentAccount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def check_parent(self, data):
        # 檢查上層代理是否可用
        path = '/Agent/CheckParent'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create_submit(self, data):
        # 代理新增完後送出訂單 看是否建立成功
        path = '/Agent/CreateSubmit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

# 代理申请审核


# 会员注册审核


# 试玩审核
