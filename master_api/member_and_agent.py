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

    def query_page(self, data):
        path = '/Member/Query'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def search(self, data):
        path = '/Member/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_detail(self, data):
        path = '/Member/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def account_balance(self, data):
        path = '/Member/SumBalance'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_deposit_withdraw_info(self, data):
        path = '/Member/GetDepositWithdrawInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_audit_detail(self, data):
        path = '/Member/GetAuditDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def load_history(self, data):
        path = '/Member/LoadHistory'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def update_bank_account(self, data):
        # API Name =>会员新增&查询-更新銀行帳户
        # body--/{memberAccount}/{updateBankAccountParams}
        path = '/Member/UpdateBankAccount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllMemberLevels(self, data):
        # 取得所有會員等級 - 1127
        path = '/Home/GetAllMemberLevels'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberStates(self, data):
        # 會員狀態 - 1127
        path = '/Member/GetMemberStates'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllDiscountSettings(self, data):
        # 返水等級 - 1127
        path = '/Home/GetAllDiscountSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getColumnForExport(self, data):
        # 匯出會員excel檔案標籤 - 1127
        path = '/Member/GetColumnForExport'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getShelfFunctionSwitch(self, data):
        # 功能開關 - 1127
        path = '/Home/GetShelfFunctionSwitch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportMemberSearch(self, data):
        # 匯出檔案 - 1127
        path = '/Member/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def superSearch(self, data):
        # 超級會員查詢 -20200116
        path = '/Member/SuperSearch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetSuperSearchSumBalance(self, data):
        # 獲取超級搜索總餘額
        path = '/Member/GetSuperSearchSumBalance'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getColumnForSuperSearch(self, data):
        # 取得超級會員顯示欄位
        path = '/Member/getColumnForSuperSearch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSearchCount(self, data):
        # 取得總筆數
        path = '/Member/GetSearchCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSearchSumBalance(self, data):
        # 取得總金額
        path = '/Member/GetSearchSumBalance'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ExportForSuperSearch(self, data):
        # 超級會員 - 匯出檔案
        path = '/Member/ExportForSuperSearch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 會員標籤
class MemberTags(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def getTags(self, data):
        # 取得標籤
        path = '/MemberTag/GetTags'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def addMemberTag(self, data):
        # 新增會員標籤
        path = '/MemberTag/AddMemberTag'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def removeMamberTag(self, data):
        # 刪除會員標籤
        path = '/MemberTag/RemoveMamberTag'  # 這是正確可執行的
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberTags(self, data):
        # 取得會員標籤
        path = '/MemberTag/GetMemberTags'
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
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def batch_page(self, data):
        # 會員批次處理頁面
        path = '/Member/Batch'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def clearTemp(self, data):
        path = '/Member/ClearTemp'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberStates(self, data):
        # 取得會員所有狀態
        path = '/Member/GetMemberStates'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBatchData(self, data):
        # 取得批次會員資料
        path = '/Member/GetBatchData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchWithdrawYuebao(self, data):
        # 批次取回餘額寶
        path = '/Member/BatchWithdrawYuebao'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchUpdateMemberState(self, data):
        # 批次修改會員狀態
        path = '/Member/BatchUpdateMemberState'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchUpdateMemberLevel(self, data):
        # 批次修改會員等級
        path = '/Member/BatchUpdateMemberLevel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def anyTimeDiscountBatchReset(self, data):
        # 批次時時歸水歸零
        path = '/Member/AnyTimeDiscountBatchReset'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def depositSubmitForMemberBatchDeposit(self, data):
        # 批次人工存入
        path = '/Member/DepositSubmitForMemberBatchDeposit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchAddOrDeleteMemberTags(self, data):
        # 批次修改標籤
        path = '/MemberTag/BatchAddOrDeleteMemberTags'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchUpdateMemberSmsValidation(self, data):
        # 批次修改簡訊驗證
        path = '/Member/BatchUpdateMemberSmsValidation'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchUpdateMemberEmailValidation(self, data):
        # 批次修改電子郵件驗證
        path = '/Member/BatchUpdateMemberEmailValidation'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchDisableMemberGoogleAuthenticator(self, data):
        # 批次停用二次驗證
        path = '/Member/BatchDisableMemberGoogleAuthenticator'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def batchDisableMemberGpkAuthenticator(self, data):
        # 批次停用二次驗證
        path = '/Member/BatchDisableMemberGpkAuthenticator'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 會員詳細資料
class MemberDetail(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def detail_page(self, data):
        # 會員詳細資料頁面
        path = '/Member/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # 取得會員詳細資料
        path = '/Member/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDepositWithdrawInfo(self, data):
        # 取得存提款資訊
        path = '/Member/GetDepositWithdrawInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberEventList(self, data):
        # 取得會員正在參與的活動
        path = '/Member/GetMemberEventList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberState(self, data):
        # 更新會員狀態
        path = '/Member/UpdateMemberState'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberLevel(self, data):
        # 更新會員等級
        path = '/Member/UpdateMemberLevel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDiscountSetting(self, data):
        # 更新返水等級
        path = '/Member/UpdateDiscountSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyMemberInfo(self, data):
        # 修改會員資料頁面
        path = '/Member/ModifyMemberInfo'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getMemberInfo(self, data):
        # 取得會員基本資料
        path = '/Member/GetMemberInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberInfo(self, data):
        # 更新會員基本資料
        path = '/Member/UpdateMemberInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyBankAccount(self, data):
        # 修改銀行資料頁面
        path = '/Member/ModifyBankAccount'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getBankAccount(self, data):
        # 取得銀行資料
        path = '/Member/GetBankAccount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkBankAccount(self, data):
        # 檢查銀行帳戶
        path = '/Member/CheckBankAccount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateBankAccount(self, data):
        # 更新銀行資料
        path = '/Member/UpdateBankAccount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBankHistories(self, data):
        # 取得銀行修改紀錄
        path = '/Member/GetBankHistories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAlipayAccountHistories(self, data):
        # 取得支付寶修改紀錄
        path = '/Member/GetAlipayAccountHistories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberSmsLoginValidationEnable(self, data):
        # 手機簡訊驗證
        path = '/Member/UpdateMemberSmsLoginValidationEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def audit(self, data):
        # 稽核頁面
        path = '/Member/Audit'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAuditDetail(self, data):
        # 取得稽核詳細資料
        path = '/Member/GetAuditDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def auditModify(self, data):
        # 修改稽核頁面
        path = '/Member/AuditModify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDepositList(self, data):
        # 取得會員稽核資料
        path = '/Member/GetDepositList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDepositAudit(self, data):
        # 更新稽核 - 1129
        path = '/Member/UpdateDepositAudit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def clearAudit(self, data):
        # 清除稽核
        path = '/Member/ClearAudit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetPassword(self, data):
        # 重設密碼
        path = '/Member/ResetPassword'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def walletUpdateMember(self, data):
        # 娛樂城錢包更新 - 尚未實作案例
        path = '/Member/WalletUpdateMember'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def walletBackMember(self, data):
        # 娛樂城錢包取回 - 尚未實作案例
        path = '/Member/WalletBackMember'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allWalletBackMember(self, data):
        # 娛樂城錢包全取回 - 尚未實作案例
        path = '/Member/AllWalletBackMember'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allWalletUpdateMember(self, data):
        # 娛樂城錢包全更新
        path = '/Member/AllWalletUpdateMember'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetMoneyPassword(self, data):
        # 重設取款密碼
        path = '/Member/ResetMoneyPassword'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # 更新備註
        path = '/Member/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def changeAgent(self, data):
        # 更換代理商頁面 -1129
        path = '/Member/ChangeAgent'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAgents(self, data):
        # 取得代理
        path = '/Member/GetAgents'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def changeAgentSubmit(self, data):
        # 更換代理
        path = '/Member/ChangeAgentSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def history(self, data):
        # 會員歷史紀錄頁面
        path = '/Member/History'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def historyInit(self, data):
        # 會員歷史紀錄
        path = '/Member/HistoryInit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # 讀取會員歷史紀錄
        path = '/Member/LoadHistory'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberIsNeedRegionValidate(self, data):
        # 更新區域驗證限制 - 1206
        path = '/Member/UpdateMemberIsNeedRegionValidate'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetMemberGoogleAuthenticatorEnable(self, data):
        # 重置二次驗證 - 1206
        path = '/Member/ResetMemberGoogleAuthenticatorEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberInfoHistories(self, data):
        # 會員基本資料修改歷程 -1220
        path = '/Member/GetMemberInfoHistories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberEmailLoginValidationLimit(self, data):
        # 電子郵件發送信箱次數限制
        path = '/Member/UpdateMemberEmailLoginValidationLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UnsuspendLogin(self, data):
        # API Name =>會員詳細資料 - 解除暫停登入
        # body--////{memberId}
        path = '/Member/UnsuspendLogin'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMaliciouslyLoginEnable(self, data):
        # API Name =>會員詳細資料 - 恶意登入机制
        # body--////{memberId}
        path = '/Member/UpdateMaliciouslyLoginEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 人工存款
class MemberDeposit(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def deposit_page(self, data):
        # 人工存入頁面
        path = '/Member/Deposit'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_deposit_audit_types(self, data):
        # 取得人工存入稽核方式
        path = '/Member/GetDepositAuditTypes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_manual_member_types(self, data):
        # 取得人工存入可選類型
        path = '/Member/GetManualMemberTypes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_deposit_limit(self, data):
        # 取得人工存入限額
        path = '/Member/GetDepositLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deposit_token(self, data):
        # 取得存款的 Token
        path = '/Member/DepositToken'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deposit_submit(self, data):
        # 送出
        path = '/Member/DepositSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 人工提款
class MemberWithdraw(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def withdraw_page(self, data):
        # 人工提出頁面
        path = '/Member/Withdraw'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def withdraw_init(self, data):
        # 人工提出初始化
        path = '/Member/WithdrawInit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def withdraw_submit(self, data):
        # 人工提出送出
        path = '/Member/WithdrawSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 代理商查询
class AgentSearch(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def query(self, data):
        # 取得代理商查詢頁面
        path = '/Agent/Query'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    # def get_all_level(self, data):
    #     # 取得所有代理層級
    #     path = '/Agent/GetAllLevel'
    #     self.response_data = self.__http.sendRequest('POST', path, data)
    #     return self.response_data

    def get_all_member_levels(self, data):
        # 取得所有會員層級
        path = '/Home/GetAllMemberLevels'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_discount_settings(self, data):
        # 取得所有返水等級
        path = '/Home/GetAllDiscountSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_commission_settings(self, data):
        # 取得所有佣金設定
        path = '/Agent/GetAllCommissionSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllLevel(self, data):
        # 取得所有的代理等級
        path = '/Agent/GetAllLevel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # 搜尋
        path = '/Agent/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # 匯出Excel
        path = '/Agent/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 代理商詳細
class AgentDetail(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def detail(self, data):
        # 代理商查詢 - 取得代理詳細資料頁面
        path = '/Agent/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail(self, data):
        # 代理詳細資訊
        path = '/Agent/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def disable(self, data):
        # 停用此代理帳號
        path = '/Agent/Disable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def active(self, data):
        # 啟用此代理帳號
        path = '/Agent/Active'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllDiscountSettings(self, data):
        # 取得所有的返水設定
        path = '/Home/GetAllDiscountSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllMemberLevels(self, data):
        # 取得所有的會員等級
        path = '/Home/GetAllMemberLevels'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllCommissionSettings(self, data):
        # 取得所有的傭金設定
        path = '/Agent/GetAllCommissionSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCustomizedAgentLinks(self, data):
        # 修改自訂推廣鏈接
        path = '/Agent/UpdateCustomizedAgentLinks'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCommissionSetting(self, data):
        # 更新佣金設定
        path = '/Agent/UpdateCommissionSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentLink(self, data):
        # 更新代理推廣鏈接
        path = '/Agent/UpdateAgentLink'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentLinkStatus(self, data):
        # 更新自訂代理推廣鏈接狀態
        path = '/Agent/UpdateAgentLinkStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDefaultMemberLevelSetting(self, data):
        # 更新預設會員等級
        path = '/Agent/UpdateDefaultMemberLevelSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDefaultDiscountSetting(self, data):
        # 更新預設返水等級
        path = '/Agent/UpdateDefaultDiscountSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkUpdateAgentAuthority(self, data):
        # 檢查更新代理商權限 - 取得修改銀行帳戶資訊
        path = '/Agent/CheckUpdateAgentAuthority'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyAgentInfo(self, data):
        # 修改代理商基本資料頁面
        path = '/Agent/ModifyAgentInfo'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def updateAgentInfo(self, data):
        # 更新代理商基本資料
        path = '/Agent/UpdateAgentInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllBanks(self, data):
        # 取得所有銀行
        path = '/Home/GetAllBanks'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyBankAccount(self, data):
        # 修改銀行基本資料頁面
        path = '/Agent/ModifyBankAccount'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def updateBankAccount(self, data):
        # 更新銀行基本資料
        path = '/Agent/UpdateBankAccount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBankHistories(self, data):
        # 銀行修改紀錄
        path = '/Agent/GetBankHistories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        #  更新備註
        path = '/Agent/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def resetPassword(self, data):
        # 重設密碼
        path = '/Agent/ResetPassword'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def history(self, data):
        # 代理商歷史紀錄頁面
        path = '/Agent/History'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def historyInit(self, data):
        # 歷史紀錄資訊
        path = '/Agent/HistoryInit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # 讀取歷史紀錄
        path = '/Agent/LoadHistory'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAgentLayerDetail(self, data):
        # 讀取代理資料
        path = '/Agent/GetAgentLayerDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 新增会员
class MemberCreate(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def createPage(self, data):
        # 新增會員頁面
        path = '/Member/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def isEnableAddMemberSite(self, data):
        # 是否能夠新增會員頁面
        path = '/Home/IsEnableAddMemberSite'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDefaultPasswords(self, data):
        # 取得預設密碼
        path = '/Member/GetDefaultPasswords'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkAccountIsInUse(self, data):
        # 確認使用者是否能夠新增
        path = '/Member/CheckAccountIsInUse'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # 新增會員
        path = '/Member/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 会员汇入
class MemberImport(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def index(self, data):
        # 會員匯入頁面
        path = '/MemberImport/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def checkHasMemberImporting(self, data):
        # 確認是否有會員匯入
        path = '/MemberImport/CheckHasMemberImporting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRecord(self, data):
        # 取得會員匯入紀錄
        path = '/MemberImport/GetRecord'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def downloadExample(self, data):
        # 下載範本
        path = '/MemberImport/DownloadExample'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getExcelSum(self, data):
        #  上傳Excel檔案
        path = '/MemberImport/GetExcelSum'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def submit(self, data):
        # 開始匯入
        path = '/MemberImport/Submit'
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
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create(self, data):
        # 取得新增代理商頁面
        path = '/Agent/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_all_level_with_create(self, data):
        # 新增時取得所有代理層級
        path = '/Agent/GetAllLevelWithCreate'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_all_banks(self, data):
        # 銀行資訊-新增時取得所有銀行名稱
        path = '/Home/GetAllBanks'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def check_agent_account(self, data):
        # 代理商查詢 - 檢查新增代理帳號是否已存在
        path = '/Agent/CheckAgentAccount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def check_parent(self, data):
        # 檢查上層代理是否可用
        path = '/Agent/CheckParent'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create_submit(self, data):
        # 代理新增完後送出訂單 看是否建立成功
        path = '/Agent/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkAllUpdateAgentAuthority(self, data):
        # 檢查並更新所有代理權限_2019/11/06-update
        path = '/Agent/CheckAllUpdateAgentAuthority'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 代理申请审核


# 会员注册审核
class MemberVerifyPage(object):

    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def getSetting(self, data):
        # 取得各站資訊
        path = '/MemberRegisterVerify/GetSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllStatus(self, data):
        # 取得所有狀態
        path = '/MemberRegisterVerify/GetAllStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getList(self, data):
        # 取得看板資料
        path = '/MemberRegisterVerify/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # 取得會員註冊審核詳細資料
        path = '/MemberRegisterVerify/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSetting(self, data):
        # 取得會員註冊審核設定
        path = '/MemberRegisterVerify/GetSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAvailableMinutes(self, data):
        # 更新審核有效分鐘數
        path = '/MemberRegisterVerify/UpdateAvailableMinutes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWebSiteMemberRegisterVerifySwitch(self, data):
        # 更新會員註冊審核開關
        path = '/MemberRegisterVerify/UpdateWebSiteMemberRegisterVerifySwitch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDomainNameStatus(self, data):
        # 更新域名狀態
        path = '/MemberRegisterVerify/UpdateDomainNameStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createDomainNameItem(self, data):
        # 新增域名
        path = '/MemberRegisterVerify/CreateDomainNameItem'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteDomainNameItem(self, data):
        # 刪除域名
        path = '/MemberRegisterVerify/DeleteDomainNameItem'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentStatus(self, data):
        # 更新代理商狀態
        path = '/MemberRegisterVerify/UpdateAgentStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createAgentItem(self, data):
        # 新增代理商項目
        path = '/MemberRegisterVerify/CreateAgentItem'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteAgentItem(self, data):
        # 刪除代理商項目
        path = '/MemberRegisterVerify/DeleteAgentItem'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getHistoryList(self, data):
        # 會員註冊審核設定歷史紀錄
        path = '/MemberRegisterVerify/GetHistoryList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkAccountIsInUse(self, data):
        # 審核會員
        path = '/Member/CheckAccountIsInUse'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deny(self, data):
        # 會員審核-拒絕
        path = '/MemberRegisterVerify/Deny'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def approve(self, data):
        # 會員審核-確認
        path = '/MemberRegisterVerify/Approve'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # 更新備註
        path = '/MemberRegisterVerify/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 试玩审核
class Trial(object):
    def __init__(self, http):
        self.__http = http
        self.user = User(self.__http)
        self.response_data = {}

    def list(self, data):
        # 取得看板清單頁面
        path = '/Trial/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getMemberTrialSetting(self, data):
        # 取得試玩審核設定
        path = '/Trial/GetMemberTrialSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def load(self, data):
        # 讀取試玩帳號資料
        path = '/Trial/Load'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createNew(self, data):
        # 館端新增一組試玩
        path = '/Trial/CreateNew'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyAutoVerifyMemberTrial(self, data):
        # 更新自動審核按鈕
        path = '/Trial/ModifyAutoVerifyMemberTrial'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyMemberTrialViewType(self, data):
        # 試玩轉跳設定
        path = '/Trial/ModifyMemberTrialViewType'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyMemberTrialColumnType(self, data):
        # 試玩申請欄位
        path = '/Trial/ModifyMemberTrialColumnType'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allow(self, data):
        # 允許試玩帳號
        path = '/Trial/Allow'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deny(self, data):
        #  拒絕試玩帳號
        path = '/Trial/Deny'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data
