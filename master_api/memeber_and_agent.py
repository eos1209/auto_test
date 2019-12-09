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

    def getAllMemberLevels(self):
        # 取得所有會員等級 - 1127
        path = '/Home/GetAllMemberLevels'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberStates(self):
        # 會員狀態 - 1127
        path = '/Member/GetMemberStates'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllDiscountSettings(self):
        # 返水等級 - 1127
        path = '/Home/GetAllDiscountSettings'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getColumnForExport(self):
        # 匯出會員excel檔案標籤 - 1127
        path = '/Member/GetColumnForExport'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getShelfFunctionSwitch(self):
        # 功能開關 - 1127
        path = '/Home/GetShelfFunctionSwitch'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportMemberSearch(self, data):
        # 匯出檔案 - 1127
        path = '/Member/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 會員標籤
class MemberTags(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def getTags(self):
        # 取得會員標籤
        path = '/MemberTag/GetTags'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def addMemberTag(self, data):
        # 新增會員標籤
        path = '/MemberTag/AddMemberTag'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def removeMamberTag(self, data):
        # 刪除會員標籤
        path = '/MemberTag/RemoveMamberTag'  # 這是正確可執行的
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 會員批次處理
class MemberBatch(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def importAndGetLargeAccount(self, data):
        # 匯入會員批次檔案 -1128
        path = '/Member/ImportAndGetLargeAccount'
        data = data
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def batch_page(self):
        # 會員批次處理頁面
        path = '/Member/Batch'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def clearTemp(self):
        path = '/Member/ClearTemp'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)

    def getMemberStates(self):
        # 取得會員所有狀態
        path = '/Member/GetMemberStates'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBatchData(self, data):
        # 取得批次會員資料
        path = '/Member/GetBatchData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchWithdrawYuebao(self, data):
        # 批次取回餘額寶
        path = '/Member/BatchWithdrawYuebao'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchUpdateMemberState(self, data):
        # 批次修改會員狀態
        path = '/Member/BatchUpdateMemberState'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchUpdateMemberLevel(self, data):
        # 批次修改會員等級
        path = '/Member/BatchUpdateMemberLevel'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def anyTimeDiscountBatchReset(self, data):
        # 批次時時歸水歸零
        path = '/Member/AnyTimeDiscountBatchReset'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def depositSubmitForMemberBatchDeposit(self, data):
        # 批次人工存入
        path = '/Member/DepositSubmitForMemberBatchDeposit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchAddOrDeleteMemberTags(self, data):
        # 批次修改標籤
        path = '/MemberTag/BatchAddOrDeleteMemberTags'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 會員詳細資料
class MemberDetail(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def detail_page(self):
        # 會員詳細資料頁面
        path = '/Member/Detail'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # 取得會員詳細資料
        path = '/Member/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDepositWithdrawInfo(self, data):
        # 取得存提款資訊
        path = '/Member/GetDepositWithdrawInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberEventList(self, data):
        # 取得會員正在參與的活動
        path = '/Member/GetMemberEventList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberState(self, data):
        # 更新會員狀態
        path = '/Member/UpdateMemberState'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberLevel(self, data):
        # 更新會員等級
        path = '/Member/UpdateMemberLevel'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDiscountSetting(self, data):
        # 更新返水等級
        path = '/Member/UpdateDiscountSetting'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyMemberInfo(self):
        # 修改會員資料頁面
        path = '/Member/ModifyMemberInfo'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getMemberInfo(self, data):
        # 取得會員基本資料
        path = '/Member/GetMemberInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberInfo(self, data):
        # 更新會員基本資料
        path = '/Member/UpdateMemberInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyBankAccount(self):
        # 修改銀行資料頁面
        path = '/Member/ModifyBankAccount'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getBankAccount(self, data):
        # 取得銀行資料
        path = '/Member/GetBankAccount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkBankAccount(self, data):
        # 檢查銀行帳戶
        path = '/Member/CheckBankAccount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateBankAccount(self, data):
        # 更新銀行資料
        path = '/Member/UpdateBankAccount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBankHistories(self, data):
        # 取得銀行修改紀錄
        path = '/Member/GetBankHistories'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAlipayAccountHistories(self, data):
        # 取得支付寶修改紀錄
        path = '/Member/GetAlipayAccountHistories'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberLoginEveryWhere(self, data):
        # 更新區域驗證限制
        path = '/Member/UpdateMemberLoginEveryWhere'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberSmsLoginValidationEnable(self, data):
        # 手機簡訊驗證
        path = '/Member/UpdateMemberSmsLoginValidationEnable'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def audit(self):
        # 稽核頁面
        path = '/Member/Audit'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAuditDetail(self, data):
        # 取得稽核詳細資料
        path = '/Member/GetAuditDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def auditModify(self):
        # 修改稽核頁面
        path = '/Member/AuditModify'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDepositList(self, data):
        # 取得會員稽核資料
        path = '/Member/GetDepositList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDepositAudit(self, data):
        # 更新稽核 - 1129
        path = '/Member/UpdateDepositAudit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def clearAudit(self, data):
        # 清除稽核
        path = '/Member/ClearAudit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetPassword(self, data):
        # 重設密碼
        path = '/Member/ResetPassword'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def walletUpdateMember(self, data):
        # 娛樂城錢包更新 - 尚未實作案例
        path = '/Member/WalletUpdateMember'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def walletBackMember(self, data):
        # 娛樂城錢包取回 - 尚未實作案例
        path = '/Member/WalletBackMember'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allWalletBackMember(self, data):
        # 娛樂城錢包全取回 - 尚未實作案例
        path = '/Member/AllWalletBackMember'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allWalletUpdateMember(self, data):
        # 娛樂城錢包全更新
        path = '/Member/AllWalletUpdateMember'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetMoneyPassword(self, data):
        # 重設取款密碼
        path = '/Member/ResetMoneyPassword'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # 更新備註
        path = '/Member/UpdateMemo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def changeAgent(self):
        # 更換代理商頁面 -1129
        path = '/Member/ChangeAgent'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAgents(self, data):
        # 取得代理
        path = '/Member/GetAgents'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def changeAgentSubmit(self, data):
        # 更換代理
        path = '/Member/ChangeAgentSubmit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def history(self):
        # 會員歷史紀錄頁面
        path = '/Member/History'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def historyInit(self, data):
        # 會員歷史紀錄
        path = '/Member/HistoryInit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # 讀取會員歷史紀錄
        path = '/Member/LoadHistory'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberIsNeedRegionValidate(self, data):
        # 更新區域驗證限制 - 1206
        path = '/Member/UpdateMemberIsNeedRegionValidate'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetMemberGoogleAuthenticatorEnable(self, data):
        # 重置二次驗證 - 1206
        path = '/Member/ResetMemberGoogleAuthenticatorEnable'
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

    def get_all_level(self):
        # 取得所有代理層級
        path = '/Agent/GetAllLevel'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_member_levels(self):
        # 取得所有會員層級
        path = '/Home/GetAllMemberLevels'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_discount_settings(self):
        # 取得所有返水等級
        path = '/Home/GetAllDiscountSettings'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_commission_settings(self):
        # 取得所有佣金設定
        path = '/Agent/GetAllCommissionSettings'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllLevel(self):
        # 取得所有的代理等級
        path = '/Agent/GetAllLevel'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # 搜尋
        path = '/Agent/Search'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # 匯出Excel
        path = '/Agent/Export'
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

    def getAllDiscountSettings(self):
        # 取得所有的返水設定
        path = '/Home/GetAllDiscountSettings'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllMemberLevels(self):
        # 取得所有的會員等級
        path = '/Home/GetAllMemberLevels'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllCommissionSettings(self):
        # 取得所有的傭金設定
        path = '/Agent/GetAllCommissionSettings'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCustomizedAgentLinks(self, data):
        # 修改自訂推廣鏈接
        path = '/Agent/UpdateCustomizedAgentLinks'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCommissionSetting(self, data):
        # 更新佣金設定
        path = '/Agent/UpdateCommissionSetting'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentLink(self, data):
        # 更新代理推廣鏈接
        path = '/Agent/UpdateAgentLink'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentLinkStatus(self, data):
        # 更新自訂代理推廣鏈接狀態
        path = '/Agent/UpdateAgentLinkStatus'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDefaultMemberLevelSetting(self, data):
        # 更新預設會員等級
        path = '/Agent/UpdateDefaultMemberLevelSetting'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDefaultDiscountSetting(self, data):
        # 更新預設返水等級
        path = '/Agent/UpdateDefaultDiscountSetting'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkUpdateAgentAuthority(self, data):
        # 檢查更新代理商權限
        path = '/Agent/CheckUpdateAgentAuthority'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyAgentInfo(self):
        # 修改代理商基本資料頁面
        path = '/Agent/ModifyAgentInfo'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def updateAgentInfo(self, data):
        # 更新代理商基本資料
        path = '/Agent/UpdateAgentInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllBanks(self):
        # 取得所有銀行
        path = '/Home/GetAllBanks'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyBankAccount(self):
        # 修改銀行基本資料頁面
        path = '/Agent/ModifyBankAccount'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def updateBankAccount(self, data):
        # 更新銀行基本資料
        path = '/Agent/UpdateBankAccount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBankHistories(self, data):
        # 銀行修改紀錄
        path = '/Agent/GetBankHistories'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        #  更新備註
        path = '/Agent/UpdateMemo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetPassword(self, data):
        # 重設密碼
        path = '/Agent/ResetPassword'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def history(self):
        # 代理商歷史紀錄頁面
        path = '/Agent/History'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def historyInit(self, data):
        # 歷史紀錄資訊
        path = '/Agent/HistoryInit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # 讀取歷史紀錄
        path = '/Agent/LoadHistory'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 新增会员
class MemberCreate(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def createPage(self):
        # 新增會員頁面
        path = '/Member/Create'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def isEnableAddMemberSite(self):
        # 是否能夠新增會員頁面
        path = '/Home/IsEnableAddMemberSite'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDefaultPasswords(self):
        # 取得預設密碼
        path = '/Member/GetDefaultPasswords'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkAccountIsInUse(self, data):
        # 確認使用者是否能夠新增
        path = '/Member/CheckAccountIsInUse'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # 新增會員
        path = '/Member/CreateSubmit'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 会员汇入
class MemberImport(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def index(self):
        # 會員匯入頁面
        path = '/MemberImport/Index'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def checkHasMemberImporting(self):
        # 確認是否有會員匯入
        path = '/MemberImport/CheckHasMemberImporting'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRecord(self):
        # 取得會員匯入紀錄
        path = '/MemberImport/GetRecord'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def downloadExample(self):
        # 下載範本
        path = '/MemberImport/DownloadExample'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getExcelSum(self, data):
        #  上傳Excel檔案
        path = '/MemberImport/GetExcelSum'
        data = data
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def submit(self, data):
        # 開始匯入
        path = '/MemberImport/Submit'
        data = data
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data


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

    def get_all_level_with_create(self):
        # 新增時取得所有代理層級
        path = '/Agent/GetAllLevelWithCreate'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_banks(self):
        # 銀行資訊-新增時取得所有銀行名稱
        path = '/Home/GetAllBanks'
        data = {}
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

    def checkAllUpdateAgentAuthority(self):
        # 檢查並更新所有代理權限_2019/11/06-update
        path = '/Agent/CheckAllUpdateAgentAuthority'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 代理申请审核


# 会员注册审核
class MemberVerifyPage(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def getSetting(self):
        # 取得各站資訊
        path = '/MemberRegisterVerify/GetSetting'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllStatus(self):
        # 取得所有狀態
        path = '/MemberRegisterVerify/GetAllStatus'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getList(self, data):
        # 取得看板資料
        path = '/MemberRegisterVerify/GetList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # 取得會員註冊審核詳細資料
        path = '/MemberRegisterVerify/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSetting(self):
        # 取得會員註冊審核設定
        path = '/MemberRegisterVerify/GetSetting'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAvailableMinutes(self, data):
        # 更新審核有效分鐘數
        path = '/MemberRegisterVerify/UpdateAvailableMinutes'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWebSiteMemberRegisterVerifySwitch(self, data):
        # 更新會員註冊審核開關
        path = '/MemberRegisterVerify/UpdateWebSiteMemberRegisterVerifySwitch'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDomainNameStatus(self, data):
        # 更新域名狀態
        path = '/MemberRegisterVerify/UpdateDomainNameStatus'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createDomainNameItem(self, data):
        # 新增域名
        path = '/MemberRegisterVerify/CreateDomainNameItem'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteDomainNameItem(self, data):
        # 刪除域名
        path = '/MemberRegisterVerify/DeleteDomainNameItem'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentStatus(self, data):
        # 更新代理商狀態
        path = '/MemberRegisterVerify/UpdateAgentStatus'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createAgentItem(self, data):
        # 新增代理商項目
        path = '/MemberRegisterVerify/CreateAgentItem'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteAgentItem(self, data):
        # 刪除代理商項目
        path = '/MemberRegisterVerify/DeleteAgentItem'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getHistoryList(self, data):
        # 會員註冊審核設定歷史紀錄
        path = '/MemberRegisterVerify/GetHistoryList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkAccountIsInUse(self, data):
        # 審核會員
        path = '/Member/CheckAccountIsInUse'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deny(self, data):
        # 會員審核-拒絕
        path = '/MemberRegisterVerify/Deny'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def approve(self, data):
        # 會員審核-確認
        path = '/MemberRegisterVerify/Approve'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # 更新備註
        path = '/MemberRegisterVerify/UpdateMemo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

# 试玩审核
