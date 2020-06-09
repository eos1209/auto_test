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
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_index_page(self, data):
        # API Name =>公司入款审核-取得頁面
        # body--
        path = '/VerifyDeposit'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_load_data(self, data):
        # API Name =>公司入款审核-取得列表資料
        # body--/{count}/{minId}/{query}
        path = '/VerifyDeposit/Load'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def order_allow(self, data):
        # API Name =>公司入款审核-更新訂單狀態(確認)
        # body--/{id}
        path = '/VerifyDeposit/Allow'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def order_deny(self, data):
        # API Name =>公司入款审核-更新訂單狀態(拒絕)
        # body--/{id}
        path = '/VerifyDeposit/Deny'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notify_update(self, data):
        # API Name =>公司入款审核-
        # body--/{id}
        path = '/VerifyDeposit/NotifyUpdate'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def new_message(self, data):
        # API Name =>公司入款审核-通知新訂單產生
        # body--/{id}
        path = '/VerifyDeposit/New'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_detail_page(self, data):
        # API Name =>公司入款审核-取得詳細頁面
        # body--
        path = '/VerifyDeposit/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail(self, data):
        # API Name =>公司入款审核-取得詳細資料
        # body--/{id}
        path = '/VerifyDeposit/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export_data(self, data):
        # API Name =>公司入款审核-匯出
        # body--/{query}/{maxId}
        path = '/VerifyDeposit/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_total_info(self, data):
        # API Name =>公司入款审核-取得總計資訊
        # body--/{query}/{maxId}
        path = '/VerifyDeposit/GetTotalInfo'
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
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def load_new(self, data):
        # API Name =>线上支付看板-取得訂單列表
        # body--/{count}/{minId}/{query}
        path = '/ThirdPartyPayment/LoadNew'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allow_dTPP_manual(self, data):
        # API Name =>线上支付看板-詳細資料手動入款(新金流)
        # body--/{id}
        path = '/ThirdPartyPayment/DTPPManualAllow'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def cancel_dtpp_order(self, data):
        # API Name =>线上支付看板-詳細資料取消訂單(新金流)
        # body--/{id}
        path = '/ThirdPartyPayment/DTPPCancel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notify_add(self, data):
        # API Name =>线上支付看板-通知新增(須走流程)
        # body--/{id}/{isDTPP}
        path = '/ThirdPartyPayment/NotifyAdd'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notify_update(self, data):
        # API Name =>线上支付看板-通知更新(須走流程)
        # body--/{id}/{isDTPP}
        path = '/ThirdPartyPayment/NotifyUpdate'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_index_page(self, data):
        # API Name =>线上支付看板-取得訂單詳細頁面
        # body--
        path = '/ThirdPartyPayment'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail_page(self, data):
        # API Name =>线上支付看板-取得訂單詳細頁面
        # body--
        path = '/ThirdPartyPayment/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_detail(self, data):
        # API Name =>线上支付看板-訂單詳細資料(舊金流)
        # body--/{id}
        path = '/ThirdPartyPayment/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_dtpp_detail(self, data):
        # API Name =>线上支付看板-訂單詳細資料(新金流)
        # body--/{id}
        path = '/ThirdPartyPayment/DTPPGetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>线上支付看板-匯出
        # body--/{query}/{isDTPP}/{maxId}
        path = '/ThirdPartyPayment/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_total_info(self, data):
        # API Name =>线上支付看板-取得總計資訊
        # body--/{query}/{maxId}
        path = '/ThirdPartyPayment/GetTotalInfo'
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
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getApplyStates(self, data):
        # API Name =>取款申请审核-取得審核狀態
        # body--
        path = '/VerifyWithdraw/GetApplyStates'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getWithdrawTypeList(self, data):
        # API Name =>取款申请审核-取得提款類型列表
        # body--
        path = '/VerifyWithdraw/GetWithdrawTypeList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def index(self, data):
        # API Name =>取款申请审核-取得頁面
        # body--
        path = '/VerifyWithdraw'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def load(self, data):
        # API Name =>取款申请审核-載入取款申請審核資料
        # body--/{count}/{minId}/{query}
        path = '/VerifyWithdraw/Load'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>取款申请审核-取得取款申請詳細資料頁面
        # body--
        path = '/VerifyWithdraw/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detailDialog(self, data):
        # API Name =>取款申请审核-取得搜尋取款申请條件框頁面
        # body--
        path = '/VerifyWithdraw/DetailDialog'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>取款申请审核-取得取款審核申請詳細資料
        # body--/{id}
        path = '/VerifyWithdraw/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def allow(self, data):
        # API Name =>取款申请审核-申請狀態(確認)
        # body--/{id}
        path = '/VerifyWithdraw/Allow'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deny(self, data):
        # API Name =>取款申请审核-申請狀態(退回)
        # body--/{id}
        path = '/VerifyWithdraw/Deny'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def reject(self, data):
        # API Name =>取款申请审核-申請狀態(拒絕)
        # body--/{id}
        path = '/VerifyWithdraw/Reject'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # API Name =>取款申请审核-更新備注
        # body--/{id}/{memo}
        path = '/VerifyWithdraw/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updatePortalMemo(self, data):
        # API Name =>取款申请审核-更新交易紀錄的前台備注
        # body--/{id}/{portalMemo}
        path = '/VerifyWithdraw/UpdatePortalMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def auditDetail(self, data):
        # API Name =>取款申请审核-取得稽核明細頁面
        # body--
        path = '/VerifyWithdraw/AuditDetail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAuditDetail(self, data):
        # API Name =>取款申请审核-取得稽核明細詳細資料
        # body--/{id}
        path = '/VerifyWithdraw/GetAuditDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>取款申请审核-匯出
        # body--/{query}/{maxId}
        path = '/VerifyWithdraw/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exitReadWithdraw(self, data):
        # API Name =>取款申请审核-結束檢視
        # body--/{id}
        path = '/VerifyWithdraw/ExitReadWithdraw'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def releaseReaderCachde(self, data):
        # API Name =>取款申请审核-清空快取
        # body--
        path = '/VerifyWithdraw/ReleaseReaderCachde'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getTotalInfo(self, data):
        # API Name =>取款申请审核-取得總計資訊
        # body--/{query}/{maxId}
        path = '/VerifyWithdraw/GetTotalInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getUseList(self, data):
        # API Name =>取款申请审核-取得可使用代付列表
        # body--
        path = '/ThirdPartyPayout/GetUseList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getHistories(self, data):
        # API Name =>取款申请审核-檢視代付歷程
        # body--
        path = '/ThirdPartyPayout/GetHistories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getViewers(self, data):
        # API Name =>取款申请审核-檢視代付歷程
        # body--
        path = '/VerifyWithdraw/GetViewers'
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
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def list(self, data):
        # API Name =>余额宝看板-取得列表
        # body--/{search}/{minTime}/{pageSize}
        path = '/YuebaoBoard/List'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def summary(self, data):
        # API Name =>余额宝看板-取得概要
        # body--/{search}
        path = '/YuebaoBoard/Summary'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>余额宝看板-詳細頁面
        # body--/{id}/{transferId}
        path = '/YuebaoBoard/Detail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSetting(self, data):
        # API Name =>余额宝看板-
        # body--
        path = '/YuebaoBoard/GetSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getStatus(self, data):
        # API Name =>余额宝看板-
        # body--
        path = '/YuebaoBoard/GetStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberLevelSetting(self, data):
        # API Name =>余额宝看板-
        # body--
        path = '/YuebaoBoard/GetMemberLevelSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # 餘額寶看板-匯出Excel
        path = '/YuebaoBoard/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 交易记录查询
class MemberTransaction(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def query(self, data):
        # API Name =>交易记录查询-取得頁面
        # body--
        path = '/MemberTransaction/Query'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>交易记录查询-取得詳細頁面
        # body--
        path = '/MemberTransaction/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>交易记录查询-取得單筆紀錄明細
        # body--/{id}
        path = '/MemberTransaction/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def queryInit(self, data):
        # API Name =>交易记录查询-取得交易紀錄類型
        # body--
        path = '/MemberTransaction/QueryInit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>交易记录查询-查詢
        # body--/{search}/{pageIndex}
        path = '/MemberTransaction/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateIsReal(self, data):
        # API Name =>交易记录查询-更新實際存提
        # body--/{id}/{isReal}
        path = '/MemberTransaction/UpdateIsReal'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>交易记录查询-匯出
        # body--/{search}
        path = '/MemberTransaction/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAnytimeDiscountDetail(self, data):
        # API Name =>交易记录查询-時返明細
        # body--/{id}
        path = '/MemberTransaction/GetAnytimeDiscountDetail'
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
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>返水计算-取得歷史紀錄明細頁面
        # body--
        path = '/Discount/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def revocation(self, data):
        # API Name =>返水计算-取得沖銷紀錄明細頁面
        # body--
        path = '/Discount/Revocation'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def calculate(self, data):
        # API Name =>返水计算-計算
        # body--/{dateBegin}/{dateEnd}/{account}/{takeId}/{take}/{skip}
        path = '/Discount/Calculate'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def isFunctionControlDisable(self, data):
        # API Name =>返水计算-檢查本站功能開關設定
        # body--/{functionKey}
        path = '/Discount/IsFunctionControlDisable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def send(self, data):
        # API Name =>返水计算-發送返水
        # body--/{name}/{discountTempId}/{intendToDuplicate}
        path = '/Discount/Send'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRecord(self, data):
        # API Name =>返水计算-取得發送紀錄明細
        # body--/{id}
        path = '/Discount/GetRecord'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRecordDetail(self, data):
        # API Name =>返水计算-取得該筆紀錄的各娛樂城金額
        # body--/{id}/{connectionId}
        path = '/Discount/GetRecordDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # API Name =>返水计算-載入返水發送紀錄
        # body--/{skip}/{take}
        path = '/Discount/LoadHistory'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDiscountRecordName(self, data):
        # API Name =>返水计算-修改返水名稱
        # body--/{id}/{name}
        path = '/Discount/UpdateDiscountRecordName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>返水计算-匯出(發送明細)
        # body--/{id}/{connectionId}
        path = '/Discount/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportTemp(self, data):
        # API Name =>返水计算-匯出(計算明細)
        # body--/{id}
        path = '/Discount/ExportTemp'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def revokeDiscount(self, data):
        # API Name =>返水计算-返水沖銷
        # body--/{id}/{detailIds}
        path = '/Discount/RevokeDiscount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRevokedRecordSummary(self, data):
        # API Name =>返水计算-取得返水發放已沖銷資訊
        # body--/{id}
        path = '/Discount/GetRevokedRecordSummary'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRevokedRecordData(self, data):
        # API Name =>返水计算-取得返水發放沖銷詳細記錄
        # body--/{id}/{connectionId}
        path = '/Discount/GetRevokedRecordData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateIsApprovedTemp(self, data):
        # API Name =>返水计算-取得返水暫存是否發放
        # body--/{tempId}/{isApproved}
        path = '/Discount/UpdateIsApprovedTemp'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateIsApprovedTempDetail(self, data):
        # API Name =>返水计算-更新返水暫存是否發放
        # body--/{tempId}/{detailId}/{isApproved}
        path = '/Discount/UpdateIsApprovedTempDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ClearTemp(self, data):
        # API Name =>返水计算-清除Temp
        # body--/{}
        path = '/Discount/ClearTemp'
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
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getCommission(self, data):
        # API Name =>佣金计算-取得結果
        # body--/{param}/{connectionId}
        path = '/CommissionService/GetCommission'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>佣金计算-匯出
        # body--/{param}
        path = '/CommissionService/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportDataToVerify(self, data):
        # API Name =>佣金计算-匯出(個別代理)
        # body--/{param}
        path = '/CommissionService/ExportDataToVerify'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 時返異常紀錄
class LostDiscountMembers(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getLostDiscountMembers(self, data):
        # API Name =>時返異常紀錄
        # body--
        path = '/AnyTimeDiscount/GetLostDiscountMembers'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 转帐额度确认
class TransferUnknownMoney(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>转帐额度确认-頁面
        # body--
        path = '/TransferUnknownMoney/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>转帐额度确认-詳細頁面
        # body--
        path = '/TransferUnknownMoney/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>转帐额度确认-取得列表
        # body--/{query}/{count}/{minId}
        path = '/TransferUnknownMoney/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getStates(self, data):
        # API Name =>转帐额度确认-取得狀態
        # body--
        path = '/TransferUnknownMoney/GetStates'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallSearchList(self, data):
        # API Name =>转帐额度确认-取得娛樂城列表
        # body--
        path = '/TransferUnknownMoney/GetGameHallSearchList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetailStatusBar(self, data):
        # API Name =>转帐额度确认-查詢單筆詳細狀態
        # body--/{Id}
        path = '/TransferUnknownMoney/GetDetailStatusBar'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>转帐额度确认-取得單筆詳細資料
        # body--/{Id}
        path = '/TransferUnknownMoney/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def fillMoneyCount(self, data):
        # API Name =>转帐额度确认-取得手動補額度筆數
        # body--/{MaxId}/{query}
        path = '/TransferUnknownMoney/FillMoneyCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def doFillAllMoney(self, data):
        # API Name =>转帐额度确认-查詢頁面手動補額度
        # body--/{MaxId}/{query}
        path = '/TransferUnknownMoney/DoFillAllMoney'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def fillSingleTrace(self, data):
        # API Name =>转帐额度确认-詳細頁面手動補額度
        # body--/{Id}
        path = '/TransferUnknownMoney/FillSingleTrace'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def cancelFillMoney(self, data):
        # API Name =>转帐额度确认-單筆取消
        # body--/{id}
        path = '/TransferUnknownMoney/CancelFillMoney'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyAdd(self, data):
        # API Name =>转帐额度确认-通知管端的SignalR新增一筆轉帳不明紀錄
        # body--/{id}
        path = '/TransferUnknownMoney/NotifyAdd'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyUpdate(self, data):
        # API Name =>转帐额度确认-通知管端的SignalRUpdate一筆既有的轉帳不明紀錄
        # body--/{id}/{detailString}
        path = '/TransferUnknownMoney/NotifyUpdate'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 优惠汇入
class DepositImport(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>优惠汇入-取得頁面
        # body--
        path = '/DepositImport/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def downloadExcel(self, data):
        # API Name =>优惠汇入-範本下載
        # body--
        path = '/DepositImport/DownloadExcel'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def exportResult(self, data):
        # API Name =>优惠汇入-結果下載匯出
        # body--/{id}/{relatedPath}/{isRevoke}
        path = '/DepositImport/ExportResult'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportFailResult(self, data):
        # API Name =>优惠汇入-匯出錯誤結果
        # body--/{id}
        path = '/DepositImport/ExportFailResult'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def upLoadDepositeExcel_V2(self, data):
        # API Name =>优惠汇入-執行
        # body--/{filebase}/{password}
        path = '/DepositImport/UpLoadDepositeExcel_V2'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def upLoadDepositeForId(self, data):
        # API Name =>优惠汇入-
        # body--/{id}/{password}
        path = '/DepositImport/UpLoadDepositeForId'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>优惠汇入-取得匯入紀錄
        # body--/{take}/{skip}
        path = '/DepositImport/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateStatus(self, data):
        # API Name =>优惠汇入-更改狀態
        # body--
        path = '/DepositImport/UpdateStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getExcelSum(self, data):
        # API Name =>优惠汇入-取得檔案內容總計
        # body--/{filebase}
        path = '/DepositImport/GetExcelSum'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def getRetrySum(self, data):
        # API Name =>优惠汇入-
        # body--/{id}
        path = '/DepositImport/GetRetrySum'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkRevocation(self, data):
        # API Name =>优惠汇入-
        # body--/{id}
        path = '/DepositImport/CheckRevocation'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def revoke(self, data):
        # API Name =>优惠汇入-
        # body--/{request}
        path = '/DepositImport/Revoke'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRevokeDetail(self, data):
        # API Name =>优惠汇入-
        # body--/{id}
        path = '/DepositImport/GetRevokeDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getNoticeFromSignalR(self, data):
        # API Name =>优惠汇入-
        # body--/{noticeDto}
        path = '/DepositImport/GetNoticeFromSignalR'
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
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def reportExport(self, data):
        # API Name =>总存取款汇出-匯出
        # body--/{beginDate}/{endDate}
        path = '/TransactionReport/ReportExport'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateStatus(self, data):
        # 大量匯出時更新狀態
        path = '/TransactionReport/UpdateStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


class Master(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def List(self, data):
        # API Name =>子帳號管理-取得頁面
        # body--{}
        path = '/Master/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def GetAll(self, data):
        # API Name =>子帳號管理-取得列表
        # body--{}
        path = '/Master/GetAll'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetRoleList(self, data):
        # API Name =>子帳號管理-獲取角色列表
        # body--{}
        path = '/Master/GetRoleList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetDetail(self, data):
        # API Name =>子帳號管理-獲取詳細資料
        # body--{account}
        path = '/Master/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetRoleAuthorityForDetail(self, data):
        # API Name =>子帳號管理-獲取角色授權已獲取詳細信息
        # body--{roleId}
        path = '/Master/GetRoleAuthorityForDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def History(self, data):
        # API Name =>子帳號管理-獲取歷史訊息
        # body--{}
        path = '/Master/History'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def LoadHistory(self, data):
        # API Name =>子帳號管理-獲取帳號歷史訊息
        # body-/{account}/{take}/{skip}/{query}
        path = '/Master/LoadHistory'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data
