'''
@Created by yuhsiang
@Date : 2019/5/20
'''


# 统计报表
class Statistics(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>统计报表-取得頁面
        # body--
        path = '/Statistics/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAgentInfo(self, data):
        # API Name =>统计报表-取得代理商或會員資訊
        # body--/{account}/{isMember}
        path = '/Statistics/GetAgentInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getCategoryInfo(self, data):
        # API Name =>统计报表-取得統計資訊
        # body--/{begin}/{end}/{agent}
        path = '/Statistics/GetCategoryInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberCount(self, data):
        # API Name =>统计报表-取得統計資料會員數
        # body--/{begin}/{end}/{agent}/{types}
        path = '/Statistics/GetMemberCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetailInfo(self, data):
        # API Name =>统计报表-取得詳細資料
        # body--/{input}
        path = '/Statistics/GetDetailInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>统计报表-匯出
        # body--/{begin}/{end}/{agent}/{types}
        path = '/Statistics/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateStatus(self, data):
        # API Name =>统计报表-更新狀態
        # body--/{}
        path = '/Statistics/UpdateStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def toManualExportFileFTP(self, data):
        # API Name =>统计报表-报表链接
        # body--
        path = '/Statistics/ToManualExportFileFTP'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data


# 投注记录查询
class BetRecords(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def query(self, data):
        # API Name =>投注记录查询-取得頁面
        # body--
        path = '/BetRecord/Query'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    # def queryAdvanced(self, data):
    #     # API Name =>投注记录查询-取得進階搜尋頁面，20200520應該是被移除
    #     # body--
    #     path = '/BetRecord/QueryAdvanced'
    #     self.response_data = self.__http.sendRequest('GET', path, data)
    #     return self.response_data

    def getSupplierCategories(self, data):
        # API Name =>投注记录查询-取得各娛樂城，以及所屬的遊戲類型
        # body--
        path = '/BetRecord/GetSupplierCategories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getKindCategories(self, data):
        # API Name =>投注记录查询-取得遊戲種類，以及所屬的遊戲類型
        # body--
        path = '/BetRecord/GetKindCategories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>投注记录查询-查詢
        # body--/{searchParams}/{connectionId}/{pageIndex}
        path = '/BetRecord/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>投注记录查询-取得詳細資訊頁面
        # body--
        path = '/BetRecord/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>投注记录查询-取得投注紀錄詳細資訊
        # body--/{id}
        path = '/BetRecord/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getLiveAndGameRawDataInfo(self, data):
        # API Name =>投注记录查询-取得視訊和機率的原始資料
        # body--/{id}
        path = '/BetRecord/GetLiveAndGameRawDataInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>投注记录查询-匯出
        # body--/{search}
        path = '/BetRecord/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateBetDetail(self, data):
        # API Name =>投注记录查询-更新單一筆注單
        # body--/{id}
        path = '/BetRecord/UpdateBetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRawData(self, data):
        # API Name =>投注记录查询-取得單筆注單原始詳細資料
        # body--/{id}
        path = '/BetRecord/GetRawData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSabaSportMixParlaySubTickets(self, data):
        # API Name =>投注记录查询-取得 Saba 體育子/混合過關注單
        # body--/{parlaySportBetId}
        path = '/BetRecord/GetSabaSportMixParlaySubTickets'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSabaVirtualSportMixParlaySubTickets(self, data):
        # API Name =>投注记录查询-取得 Saba 虛擬體育子/混合過關注單
        # body--/{parlaySportBetId}
        path = '/BetRecord/GetSabaVirtualSportMixParlaySubTickets'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSingParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Sing 體育子/混合過關注單
        # body--/{rawDataId}
        path = '/BetRecord/GetSingParlaySubRawData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getCmdParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Cmd 體育子/混合過關注單
        # body--/{socTransId}
        path = '/BetRecord/GetCmdParlaySubRawData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getImParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Im 體育子/混合過關注單(ESB 電競)
        # body--/{betId}
        path = '/BetRecord/GetImParlaySubRawData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getIboParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Ibo 體育子/混合過關注單(CR 體育)
        # body--/{betId}
        path = '/BetRecord/GetIboParlaySubRawData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getImsParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Ims 體育子/混合過關注單(IM 體育)
        # body--/{wagerId}
        path = '/BetRecord/GetImsParlaySubRawData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBetDetailUrl(self, data):
        # API Name =>投注记录查询-取得單筆注單詳細外部連結(小紅)
        # body--/{id}/{rawDataType}
        path = '/BetRecord/GetBetDetailUrl'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def advanced(self, data):
        # API Name =>投注记录查询-取得進階顯示頁面
        # body--
        path = '/BetRecord/Advanced'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def advancedCategories(self, data):
        # API Name =>投注记录查询-取得所有進階顯示的種類
        # body--
        path = '/BetRecord/AdvancedCategories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def advancedLoadV2(self, data):
        # API Name =>投注记录查询-取得進階顯示資料
        # body--/{searchParams}/{pageIndex}/{pageSize}
        path = '/BetRecord/AdvancedLoadV2'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def advancedExportV2(self, data):
        # API Name =>投注记录查询-進階顯示匯出
        # body--/{searchParams}/{category}
        path = '/BetRecord/AdvancedExportV2'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameTypeNames(self, data):
        # API Name =>投注记录查询-取得所有 GameType 的名稱
        # body--
        path = '/BetRecord/GetGameTypeNames'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 历史投注记录查询
class BetRecordHistory(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def query(self, data):
        # API Name =>历史投注记录查询-取得頁面
        # body--
        path = '/BetRecordHistory/Query'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getSupplierCategories(self, data):
        # API Name =>历史投注记录查询-取得各娛樂城，以及所屬的遊戲類型
        # body--
        path = '/BetRecordHistory/GetSupplierCategories'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getHistoryDateRange(self, data):
        # API Name =>历史投注记录查询-取得注單查詢的有效邊界值
        # body--
        path = '/BetRecordHistory/GetHistoryDateRange'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>历史投注记录查询-查詢
        # body--/{searchParams}/{connectionId}/{pageIndex}
        path = '/BetRecordHistory/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>历史投注记录查询-取得詳細資料頁面
        # body--
        path = '/BetRecordHistory/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>历史投注记录查询-取得投注紀錄詳細資訊
        # body--/{id}
        path = '/BetRecordHistory/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>历史投注记录查询-匯出
        # body--/{search}
        path = '/BetRecordHistory/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 登入记录查询
class MemberLogin(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def query(self, data):
        # API Name =>登入记录查询-取得查詢頁面
        # body--
        path = '/MemberLogin/Query'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>登入记录查询-取得詳細頁面
        # body--
        path = '/MemberLogin/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>登入记录查询-查詢
        # body--/{search}/{pageIndex}
        path = '/MemberLogin/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def searchV2(self, data):
        # API Name =>登入记录查询-查詢
        # body--/{search}/{pageIndex}/{pageSize}
        path = '/MemberLogin/SearchV2'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>登入记录查询-匯出
        # body--/{search}
        path = '/MemberLogin/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>登入记录查询-取得詳細資料
        # body--/{id}
        path = '/MemberLogin/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 娱乐城转帐记录查询
class GameSupplierTransaction(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>娱乐城转帐记录查询-取得頁面
        # body--
        path = '/GameSupplierTransaction/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>娱乐城转帐记录查询-搜尋
        # body--/{searchParams}/{pageIndex}
        path = '/GameSupplierTransaction/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>娱乐城转帐记录查询-匯出
        # body--/{searchParams}
        path = '/GameSupplierTransaction/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 优惠钱包额度移转
class WalletTransferRecord(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def search(self, data):
        # API Name =>优惠钱包额度移转-搜尋
        # body--
        path = '/WalletTransferRecord/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>优惠钱包额度移转-匯出
        # body--
        path = '/WalletTransferRecord/Export'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# AG交易记录汇出
class AgTransferRecord(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>AG交易记录汇出-取得頁面
        # body--
        path = '/AgTransferRecord/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAgTrTypeList(self, data):
        # API Name =>AG交易记录汇出-取得 AG TR 種類
        # body--
        path = '/AgTransferRecord/GetAgTrTypeList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportAgTransferRecord(self, data):
        # API Name =>投注记录查询-匯出(Ag交易紀錄)
        # body--/{dateBegin}/{dateEnd}/{trtype}
        path = '/BetRecord/ExportAgTransferRecord'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 贡献金查询
class Contribution(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>贡献金查询-取得頁面
        # body--
        path = '/Contribution/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getContributionGameSuppliers(self, data):
        # API Name =>贡献金查询-取得有貢獻金的娛樂城清單
        # body--
        path = '/Contribution/GetContributionGameSuppliers'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSummary(self, data):
        # API Name =>贡献金查询-取得當期累計貢獻金
        # body--/{date}/{halfYear}
        path = '/Contribution/GetSummary'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>贡献金查询-取得詳情
        # body--/{date}/{halfYear}
        path = '/Contribution/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameSupplierDetail(self, data):
        # API Name =>贡献金查询-取得娛樂城詳情
        # body--/{gameSupplier}/{date}/{halfYear}
        path = '/Contribution/GetGameSupplierDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllGameSupplierSummary(self, data):
        # API Name =>贡献金查询-取得全部
        # body--/{date}/{halfYear}
        path = '/Contribution/GetAllGameSupplierSummary'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameJackPotMemberList(self, data):
        # API Name =>贡献金查询-取得娛樂城獎池彩金清單
        # body--/{gameSupplier}/{gameTypeId}/{date}/{halfYear}/{pageIndex}/{pageSize}
        path = '/Contribution/GetGameJackPotMemberList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSupplierJackPotMemberList(self, data):
        # API Name =>贡献金查询-取得遊戲獎池彩金清單
        # body--/{gameSupplier}/{date}/{halfYear}/{pageIndex}/{pageSize}
        path = '/Contribution/GetSupplierJackPotMemberList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data
