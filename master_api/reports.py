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
        data = {}
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAgentInfo(self, data):
        # API Name =>统计报表-取得代理商或會員資訊
        # body--/{account}/{isMember}
        path = '/Statistics/GetAgentInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getCategoryInfo(self, data):
        # API Name =>统计报表-取得統計資訊
        # body--/{begin}/{end}/{agent}
        path = '/Statistics/GetCategoryInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberCount(self, data):
        # API Name =>统计报表-取得統計資料會員數
        # body--/{begin}/{end}/{agent}/{types}
        path = '/Statistics/GetMemberCount'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetailInfo(self, data):
        # API Name =>统计报表-取得詳細資料
        # body--/{input}
        path = '/Statistics/GetDetailInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>统计报表-匯出
        # body--/{begin}/{end}/{agent}/{types}
        path = '/Statistics/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def toManualExportFileFTP(self, data):
        # API Name =>统计报表-报表链接
        # body--
        path = '/Statistics/ToManualExportFileFTP'
        data = data
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
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def queryAdvanced(self, data):
        # API Name =>投注记录查询-取得進階搜尋頁面
        # body--
        path = '/BetRecord/QueryAdvanced'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getSupplierCategories(self, data):
        # API Name =>投注记录查询-取得各娛樂城，以及所屬的遊戲類型
        # body--
        path = '/BetRecord/GetSupplierCategories'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getKindCategories(self, data):
        # API Name =>投注记录查询-取得遊戲種類，以及所屬的遊戲類型
        # body--
        path = '/BetRecord/GetKindCategories'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>投注记录查询-查詢
        # body--/{searchParams}/{connectionId}/{pageIndex}
        path = '/BetRecord/Search'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>投注记录查询-取得詳細資訊頁面
        # body--
        path = '/BetRecord/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>投注记录查询-取得投注紀錄詳細資訊
        # body--/{id}
        path = '/BetRecord/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getLiveAndGameRawDataInfo(self, data):
        # API Name =>投注记录查询-取得視訊和機率的原始資料
        # body--/{id}
        path = '/BetRecord/GetLiveAndGameRawDataInfo'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>投注记录查询-匯出
        # body--/{search}
        path = '/BetRecord/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateBetDetail(self, data):
        # API Name =>投注记录查询-更新單一筆注單
        # body--/{id}
        path = '/BetRecord/UpdateBetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getRawData(self, data):
        # API Name =>投注记录查询-取得單筆注單原始詳細資料
        # body--/{id}
        path = '/BetRecord/GetRawData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSabaSportMixParlaySubTickets(self, data):
        # API Name =>投注记录查询-取得 Saba 體育子/混合過關注單
        # body--/{parlaySportBetId}
        path = '/BetRecord/GetSabaSportMixParlaySubTickets'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSabaVirtualSportMixParlaySubTickets(self, data):
        # API Name =>投注记录查询-取得 Saba 虛擬體育子/混合過關注單
        # body--/{parlaySportBetId}
        path = '/BetRecord/GetSabaVirtualSportMixParlaySubTickets'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSingParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Sing 體育子/混合過關注單
        # body--/{rawDataId}
        path = '/BetRecord/GetSingParlaySubRawData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getCmdParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Cmd 體育子/混合過關注單
        # body--/{socTransId}
        path = '/BetRecord/GetCmdParlaySubRawData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getImParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Im 體育子/混合過關注單
        # body--/{betId}
        path = '/BetRecord/GetImParlaySubRawData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getIboParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Ibo 體育子/混合過關注單
        # body--/{betId}
        path = '/BetRecord/GetIboParlaySubRawData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getImsParlaySubRawData(self, data):
        # API Name =>投注记录查询-取得 Ims 體育子/混合過關注單
        # body--/{wagerId}
        path = '/BetRecord/GetImsParlaySubRawData'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBetDetailUrl(self, data):
        # API Name =>投注记录查询-取得單筆注單詳細外部連結(小紅)
        # body--/{id}/{rawDataType}
        path = '/BetRecord/GetBetDetailUrl'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def advanced(self, data):
        # API Name =>投注记录查询-取得進階顯示頁面
        # body--
        path = '/BetRecord/Advanced'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def advancedCategories(self, data):
        # API Name =>投注记录查询-取得所有進階顯示的種類
        # body--
        path = '/BetRecord/AdvancedCategories'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def advancedLoadV2(self, data):
        # API Name =>投注记录查询-取得進階顯示資料
        # body--/{searchParams}/{pageIndex}/{pageSize}
        path = '/BetRecord/AdvancedLoadV2'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def advancedExportV2(self, data):
        # API Name =>投注记录查询-進階顯示匯出
        # body--/{searchParams}/{category}
        path = '/BetRecord/AdvancedExportV2'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameTypeNames(self, data):
        # API Name =>投注记录查询-取得所有 GameType 的名稱
        # body--
        path = '/BetRecord/GetGameTypeNames'
        data = data
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
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getSupplierCategories(self, data):
        # API Name =>历史投注记录查询-取得各娛樂城，以及所屬的遊戲類型
        # body--
        path = '/BetRecordHistory/GetSupplierCategories'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getHistoryDateRange(self, data):
        # API Name =>历史投注记录查询-取得注單查詢的有效邊界值
        # body--
        path = '/BetRecordHistory/GetHistoryDateRange'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>历史投注记录查询-查詢
        # body--/{searchParams}/{connectionId}/{pageIndex}
        path = '/BetRecordHistory/Search'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>历史投注记录查询-取得詳細資料頁面
        # body--
        path = '/BetRecordHistory/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>历史投注记录查询-取得投注紀錄詳細資訊
        # body--/{id}
        path = '/BetRecordHistory/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>历史投注记录查询-匯出
        # body--/{search}
        path = '/BetRecordHistory/Export'
        data = data
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
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>登入记录查询-取得詳細頁面
        # body--
        path = '/MemberLogin/Detail'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>登入记录查询-查詢
        # body--/{search}/{pageIndex}
        path = '/MemberLogin/Search'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def searchV2(self, data):
        # API Name =>登入记录查询-查詢
        # body--/{search}/{pageIndex}/{pageSize}
        path = '/MemberLogin/SearchV2'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>登入记录查询-匯出
        # body--/{search}
        path = '/MemberLogin/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>登入记录查询-取得詳細資料
        # body--/{id}
        path = '/MemberLogin/GetDetail'
        data = data
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
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def search(self, data):
        # API Name =>娱乐城转帐记录查询-搜尋
        # body--/{searchParams}/{pageIndex}
        path = '/GameSupplierTransaction/Search'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def export(self, data):
        # API Name =>娱乐城转帐记录查询-匯出
        # body--/{searchParams}
        path = '/GameSupplierTransaction/Export'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 优惠钱包额度移转


# AG交易记录汇出
class AgTransferRecord(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>AG交易记录汇出-取得頁面
        # body--
        path = '/AgTransferRecord/Index'
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getAgTrTypeList(self, data):
        # API Name =>AG交易记录汇出-取得 AG TR 種類
        # body--
        path = '/AgTransferRecord/GetAgTrTypeList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exportAgTransferRecord(self, data):
        # API Name =>投注记录查询-匯出(Ag交易紀錄)
        # body--/{dateBegin}/{dateEnd}/{trtype}
        path = '/BetRecord/ExportAgTransferRecord'
        data = data
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
        data = data
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getContributionGameSuppliers(self, data):
        # API Name =>贡献金查询-取得有貢獻金的娛樂城清單
        # body--
        path = '/Contribution/GetContributionGameSuppliers'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSummary(self, data):
        # API Name =>贡献金查询-取得當期累計貢獻金
        # body--/{date}/{halfYear}
        path = '/Contribution/GetSummary'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>贡献金查询-取得詳情
        # body--/{date}/{halfYear}
        path = '/Contribution/GetDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameSupplierDetail(self, data):
        # API Name =>贡献金查询-取得娛樂城詳情
        # body--/{gameSupplier}/{date}/{halfYear}
        path = '/Contribution/GetGameSupplierDetail'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllGameSupplierSummary(self, data):
        # API Name =>贡献金查询-取得全部
        # body--/{date}/{halfYear}
        path = '/Contribution/GetAllGameSupplierSummary'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameJackPotMemberList(self, data):
        # API Name =>贡献金查询-取得娛樂城獎池彩金清單
        # body--/{gameSupplier}/{gameTypeId}/{date}/{halfYear}/{pageIndex}/{pageSize}
        path = '/Contribution/GetGameJackPotMemberList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSupplierJackPotMemberList(self, data):
        # API Name =>贡献金查询-取得遊戲獎池彩金清單
        # body--/{gameSupplier}/{date}/{halfYear}/{pageIndex}/{pageSize}
        path = '/Contribution/GetSupplierJackPotMemberList'
        data = data
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data