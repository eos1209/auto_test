'''
@Created by yuhsiang
@Date : 2019/11/1
'''


# 公司入款审核
class VerifyDeposit(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def get_apply_states(self, data):
        # API Name =>公司入款审核-取得訂單狀態
        # body--
        path = '/VerifyDeposit/GetApplyStates'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_index_page(self, data):
        # API Name =>公司入款审核-取得頁面
        # body--
        path = '/VerifyDeposit'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_load_data(self, data):
        # API Name =>公司入款审核-取得列表資料
        # body--/{count}/{minId}/{query}
        path = '/VerifyDeposit/Load'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def order_allow(self, data):
        # API Name =>公司入款审核-更新訂單狀態(確認)
        # body--/{id}
        path = '/VerifyDeposit/Allow'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def order_deny(self, data):
        # API Name =>公司入款审核-更新訂單狀態(拒絕)
        # body--/{id}
        path = '/VerifyDeposit/Deny'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notify_update(self, data):
        # API Name =>公司入款审核-
        # body--/{id}
        path = '/VerifyDeposit/NotifyUpdate'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def new_message(self, data):
        # API Name =>公司入款审核-通知新訂單產生
        # body--/{id}
        path = '/VerifyDeposit/New'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_detail_page(self, data):
        # API Name =>公司入款审核-取得詳細頁面
        # body--
        path = '/VerifyDeposit/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail(self, data):
        # API Name =>公司入款审核-取得詳細資料
        # body--/{id}
        path = '/VerifyDeposit/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export_data(self, data):
        # API Name =>公司入款审核-匯出
        # body--/{query}/{maxId}
        path = '/VerifyDeposit/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_total_info(self, data):
        # API Name =>公司入款审核-取得總計資訊
        # body--/{query}/{maxId}
        path = '/VerifyDeposit/GetTotalInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 線上支付看板
class ThirdPartyPayment(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def get_apply_states(self, data):
        # API Name =>线上支付看板-取得申請狀態
        # body--
        path = '/ThirdPartyPayment/GetApplyStates'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def load_new(self, data):
        # API Name =>线上支付看板-取得訂單列表
        # body--/{count}/{minId}/{query}
        path = '/ThirdPartyPayment/LoadNew'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allow_dTPP_manual(self, data):
        # API Name =>线上支付看板-詳細資料手動入款(新金流)
        # body--/{id}
        path = '/ThirdPartyPayment/DTPPManualAllow'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def cancel_dtpp_order(self, data):
        # API Name =>线上支付看板-詳細資料取消訂單(新金流)
        # body--/{id}
        path = '/ThirdPartyPayment/DTPPCancel'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notify_add(self, data):
        # API Name =>线上支付看板-通知新增(須走流程)
        # body--/{id}/{isDTPP}
        path = '/ThirdPartyPayment/NotifyAdd'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notify_update(self, data):
        # API Name =>线上支付看板-通知更新(須走流程)
        # body--/{id}/{isDTPP}
        path = '/ThirdPartyPayment/NotifyUpdate'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_index_page(self, data):
        # API Name =>线上支付看板-取得訂單詳細頁面
        # body--
        path = '/ThirdPartyPayment'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail_page(self, data):
        # API Name =>线上支付看板-取得訂單詳細頁面
        # body--
        path = '/ThirdPartyPayment/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail(self, data):
        # API Name =>线上支付看板-訂單詳細資料(舊金流)
        # body--/{id}
        path = '/ThirdPartyPayment/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_dtpp_detail(self, data):
        # API Name =>线上支付看板-訂單詳細資料(新金流)
        # body--/{id}
        path = '/ThirdPartyPayment/DTPPGetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>线上支付看板-匯出
        # body--/{query}/{isDTPP}/{maxId}
        path = '/ThirdPartyPayment/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_total_info(self, data):
        # API Name =>线上支付看板-取得總計資訊
        # body--/{query}/{maxId}
        path = '/ThirdPartyPayment/GetTotalInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 取款申请审核
class VerifyWithdraw(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def new(self, data):
        # API Name =>取款申请审核-通知取款申請訂單產生
        # body--/{id}
        path = '/VerifyWithdraw/New'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getApplyStates(self, data):
        # API Name =>取款申请审核-取得審核狀態
        # body--
        path = '/VerifyWithdraw/GetApplyStates'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getWithdrawTypeList(self, data):
        # API Name =>取款申请审核-取得提款類型列表
        # body--
        path = '/VerifyWithdraw/GetWithdrawTypeList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def index(self, data):
        # API Name =>取款申请审核-取得頁面
        # body--
        path = '/VerifyWithdraw'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def load(self, data):
        # API Name =>取款申请审核-載入取款申請審核資料
        # body--/{count}/{minId}/{query}
        path = '/VerifyWithdraw/Load'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>取款申请审核-取得取款申請詳細資料頁面
        # body--
        path = '/VerifyWithdraw/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detailDialog(self, data):
        # API Name =>取款申请审核-取得搜尋取款申请條件框頁面
        # body--
        path = '/VerifyWithdraw/DetailDialog'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>取款申请审核-取得取款審核申請詳細資料
        # body--/{id}
        path = '/VerifyWithdraw/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allow(self, data):
        # API Name =>取款申请审核-申請狀態(確認)
        # body--/{id}
        path = '/VerifyWithdraw/Allow'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deny(self, data):
        # API Name =>取款申请审核-申請狀態(退回)
        # body--/{id}
        path = '/VerifyWithdraw/Deny'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def reject(self, data):
        # API Name =>取款申请审核-申請狀態(拒絕)
        # body--/{id}
        path = '/VerifyWithdraw/Reject'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # API Name =>取款申请审核-更新備注
        # body--/{id}/{memo}
        path = '/VerifyWithdraw/UpdateMemo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updatePortalMemo(self, data):
        # API Name =>取款申请审核-更新交易紀錄的前台備注
        # body--/{id}/{portalMemo}
        path = '/VerifyWithdraw/UpdatePortalMemo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def auditDetail(self, data):
        # API Name =>取款申请审核-取得稽核明細頁面
        # body--
        path = '/VerifyWithdraw/AuditDetail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAuditDetail(self, data):
        # API Name =>取款申请审核-取得稽核明細詳細資料
        # body--/{id}
        path = '/VerifyWithdraw/GetAuditDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>取款申请审核-匯出
        # body--/{query}/{maxId}
        path = '/VerifyWithdraw/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exitReadWithdraw(self, data):
        # API Name =>取款申请审核-結束檢視
        # body--/{id}
        path = '/VerifyWithdraw/ExitReadWithdraw'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def releaseReaderCachde(self, data):
        # API Name =>取款申请审核-清空快取
        # body--
        path = '/VerifyWithdraw/ReleaseReaderCachde'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getTotalInfo(self, data):
        # API Name =>取款申请审核-取得總計資訊
        # body--/{query}/{maxId}
        path = '/VerifyWithdraw/GetTotalInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 余额宝看板
class YuebaoBoard(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>余额宝看板-
        # body--/{search}/{minTime}/{pageSize}
        path = '/YuebaoList'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def list(self, data):
        # API Name =>余额宝看板-
        # body--/{search}/{minTime}/{pageSize}
        path = '/YuebaoBoard/List'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def summary(self, data):
        # API Name =>余额宝看板-
        # body--/{search}
        path = '/YuebaoBoard/Summary'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>余额宝看板-
        # body--/{id}/{transferId}
        path = '/YuebaoBoard/Detail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSetting(self, data):
        # API Name =>余额宝看板-
        # body--
        path = '/YuebaoBoard/GetSetting'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getStatus(self, data):
        # API Name =>余额宝看板-
        # body--
        path = '/YuebaoBoard/GetStatus'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberLevelSetting(self, data):
        # API Name =>余额宝看板-
        # body--
        path = '/YuebaoBoard/GetMemberLevelSetting'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 交易记录查询
class MemberTransaction(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def query(self):
        # API Name =>交易记录查询-取得頁面
        # body--
        path = '/MemberTransaction/Query'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self):
        # API Name =>交易记录查询-取得詳細頁面
        # body--
        path = '/MemberTransaction/Detail'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>交易记录查询-取得單筆紀錄明細
        # body--/{id}
        path = '/MemberTransaction/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def queryInit(self):
        # API Name =>交易记录查询-取得交易紀錄類型
        # body--
        path = '/MemberTransaction/QueryInit'
        data = {}
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>交易记录查询-查詢
        # body--/{search}/{pageIndex}
        path = '/MemberTransaction/Search'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateIsReal(self, data):
        # API Name =>交易记录查询-更新實際存提
        # body--/{id}/{isReal}
        path = '/MemberTransaction/UpdateIsReal'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>交易记录查询-匯出
        # body--/{search}
        path = '/MemberTransaction/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAnytimeDiscountDetail(self, data):
        # API Name =>交易记录查询-時返明細
        # body--/{id}
        path = '/MemberTransaction/GetAnytimeDiscountDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 返水计算
class Discount(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>返水计算-取得頁面
        # body--
        path = '/Discount/Index'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>返水计算-取得歷史紀錄明細頁面
        # body--
        path = '/Discount/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def revocation(self, data):
        # API Name =>返水计算-取得沖銷紀錄明細頁面
        # body--
        path = '/Discount/Revocation'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def calculate(self, data):
        # API Name =>返水计算-計算
        # body--/{dateBegin}/{dateEnd}/{account}/{takeId}/{take}/{skip}
        path = '/Discount/Calculate'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def isFunctionControlDisable(self, data):
        # API Name =>返水计算-檢查本站功能開關設定
        # body--/{functionKey}
        path = '/Discount/IsFunctionControlDisable'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def send(self, data):
        # API Name =>返水计算-發送返水
        # body--/{name}/{discountTempId}/{intendToDuplicate}
        path = '/Discount/Send'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRecord(self, data):
        # API Name =>返水计算-取得發送紀錄明細
        # body--/{id}
        path = '/Discount/GetRecord'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRecordDetail(self, data):
        # API Name =>返水计算-取得該筆紀錄的各娛樂城金額
        # body--/{id}/{connectionId}
        path = '/Discount/GetRecordDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # API Name =>返水计算-載入返水發送紀錄
        # body--/{skip}/{take}
        path = '/Discount/LoadHistory'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDiscountRecordName(self, data):
        # API Name =>返水计算-修改返水名稱
        # body--/{id}/{name}
        path = '/Discount/UpdateDiscountRecordName'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>返水计算-匯出(發送明細)
        # body--/{id}/{connectionId}
        path = '/Discount/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportTemp(self, data):
        # API Name =>返水计算-匯出(計算明細)
        # body--/{id}
        path = '/Discount/ExportTemp'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def revokeDiscount(self, data):
        # API Name =>返水计算-返水沖銷
        # body--/{id}/{detailIds}
        path = '/Discount/RevokeDiscount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRevokedRecordSummary(self, data):
        # API Name =>返水计算-取得返水發放已沖銷資訊
        # body--/{id}
        path = '/Discount/GetRevokedRecordSummary'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRevokedRecordData(self, data):
        # API Name =>返水计算-取得返水發放沖銷詳細記錄
        # body--/{id}/{connectionId}
        path = '/Discount/GetRevokedRecordData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateIsApprovedTemp(self, data):
        # API Name =>返水计算-取得返水暫存是否發放
        # body--/{tempId}/{isApproved}
        path = '/Discount/UpdateIsApprovedTemp'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateIsApprovedTempDetail(self, data):
        # API Name =>返水计算-更新返水暫存是否發放
        # body--/{tempId}/{detailId}/{isApproved}
        path = '/Discount/UpdateIsApprovedTempDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 佣金计算
class CommissionService(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>佣金计算-取得頁面
        # body--
        path = '/CommissionService/Index'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getCommission(self, data):
        # API Name =>佣金计算-取得結果
        # body--/{param}/{connectionId}
        path = '/CommissionService/GetCommission'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>佣金计算-匯出
        # body--/{param}
        path = '/CommissionService/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportDataToVerify(self, data):
        # API Name =>佣金计算-匯出(個別代理)
        # body--/{param}
        path = '/CommissionService/ExportDataToVerify'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 時返異常紀錄
class LostDiscountMembers(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getLostDiscountMembers(self, data):
        # 時返異常紀錄
        path = '/AnyTimeDiscount/GetLostDiscountMembers'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)


# 转帐额度确认
class TransferUnknownMoney(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>转帐额度确认-頁面
        # body--
        path = '/TransferUnknownMoney/Index'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>转帐额度确认-詳細頁面
        # body--
        path = '/TransferUnknownMoney/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>转帐额度确认-取得列表
        # body--/{query}/{count}/{minId}
        path = '/TransferUnknownMoney/GetList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getStates(self, data):
        # API Name =>转帐额度确认-取得狀態
        # body--
        path = '/TransferUnknownMoney/GetStates'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallSearchList(self, data):
        # API Name =>转帐额度确认-取得娛樂城列表
        # body--
        path = '/TransferUnknownMoney/GetGameHallSearchList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetailStatusBar(self, data):
        # API Name =>转帐额度确认-查詢單筆詳細狀態
        # body--/{Id}
        path = '/TransferUnknownMoney/GetDetailStatusBar'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>转帐额度确认-取得單筆詳細資料
        # body--/{Id}
        path = '/TransferUnknownMoney/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def fillMoneyCount(self, data):
        # API Name =>转帐额度确认-取得手動補額度筆數
        # body--/{MaxId}/{query}
        path = '/TransferUnknownMoney/FillMoneyCount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def doFillAllMoney(self, data):
        # API Name =>转帐额度确认-查詢頁面手動補額度
        # body--/{MaxId}/{query}
        path = '/TransferUnknownMoney/DoFillAllMoney'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def fillSingleTrace(self, data):
        # API Name =>转帐额度确认-詳細頁面手動補額度
        # body--/{Id}
        path = '/TransferUnknownMoney/FillSingleTrace'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def cancelFillMoney(self, data):
        # API Name =>转帐额度确认-單筆取消
        # body--/{id}
        path = '/TransferUnknownMoney/CancelFillMoney'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyAdd(self, data):
        # API Name =>转帐额度确认-通知管端的SignalR新增一筆轉帳不明紀錄
        # body--/{id}
        path = '/TransferUnknownMoney/NotifyAdd'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyUpdate(self, data):
        # API Name =>转帐额度确认-通知管端的SignalRUpdate一筆既有的轉帳不明紀錄
        # body--/{id}/{detailString}
        path = '/TransferUnknownMoney/NotifyUpdate'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 优惠汇入
class DepositImport(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self):
        # API Name =>优惠汇入-取得頁面
        # body--
        path = '/DepositImport/Index'
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def downloadExcel(self, data):
        # API Name =>优惠汇入-範本下載
        # body--
        path = '/DepositImport/DownloadExcel'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def exportResult(self, data):
        # API Name =>优惠汇入-結果下載匯出
        # body--/{id}/{relatedPath}/{isRevoke}
        path = '/DepositImport/ExportResult'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportFailResult(self, data):
        # API Name =>优惠汇入-匯出錯誤結果
        # body--/{id}
        path = '/DepositImport/ExportFailResult'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def upLoadDepositeExcel_V2(self, data):
        # API Name =>优惠汇入-執行
        # body--/{filebase}/{password}
        path = '/DepositImport/UpLoadDepositeExcel_V2'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def upLoadDepositeForId(self, data):
        # API Name =>优惠汇入-
        # body--/{id}/{password}
        path = '/DepositImport/UpLoadDepositeForId'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>优惠汇入-取得匯入紀錄
        # body--/{take}/{skip}
        path = '/DepositImport/GetList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateStatus(self, data):
        # API Name =>优惠汇入-更改狀態
        # body--
        path = '/DepositImport/UpdateStatus'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getExcelSum(self, data):
        # API Name =>优惠汇入-取得檔案內容總計
        # body--/{filebase}
        path = '/DepositImport/GetExcelSum'
        data = data
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def getRetrySum(self, data):
        # API Name =>优惠汇入-
        # body--/{id}
        path = '/DepositImport/GetRetrySum'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkRevocation(self, data):
        # API Name =>优惠汇入-
        # body--/{id}
        path = '/DepositImport/CheckRevocation'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def revoke(self, data):
        # API Name =>优惠汇入-
        # body--/{request}
        path = '/DepositImport/Revoke'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRevokeDetail(self, data):
        # API Name =>优惠汇入-
        # body--/{id}
        path = '/DepositImport/GetRevokeDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getNoticeFromSignalR(self, data):
        # API Name =>优惠汇入-
        # body--/{noticeDto}
        path = '/DepositImport/GetNoticeFromSignalR'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def submitDepositImport(self, data):
        # 優惠匯入
        path = '/DepositImport/SubmitDepositImport'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def cancelReserveImport(self, data):
        # 取消預約匯入
        path = '/DepositImport/CancelReserveImport'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 总存取款汇出
class TransactionReportSummary(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def summary(self, data):
        # API Name =>总存取款汇出-取得頁面
        # body--
        path = '/TransactionReport/Summary'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def reportExport(self, data):
        # API Name =>总存取款汇出-匯出
        # body--/{beginDate}/{endDate}
        path = '/TransactionReport/ReportExport'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data
