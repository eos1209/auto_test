'''
@Created by yuhsiang
@Date : 2019/5/20
'''


# 会员等级管理
class MemberLevelSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>会员等级管理-取得頁面
        # body--
        path = '/MemberLevelSetting/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>会员等级管理-取得列表清單
        # body--
        path = '/MemberLevelSetting/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberCount(self, data):
        # API Name =>会员等级管理-取得各等級的會員數
        # body--
        path = '/MemberLevelSetting/GetMemberCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getEventList(self, data):
        #  取得各等級的參加活動數量
        path = '/MemberLevelSetting/GetEventList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>会员等级管理-新增等級頁面
        # body--
        path = '/MemberLevelSetting/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getWalletRemmitanceEnabled(self, data):
        # API Name =>会员等级管理-啟用電子錢包
        # body--
        path = '/MemberLevelSetting/GetWalletRemmitanceEnabled'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>会员等级管理-新增等級
        # body--/{createParams}
        path = '/MemberLevelSetting/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>会员等级管理-刪除等級
        # body--/{id}
        path = '/MemberLevelSetting/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modify(self, data):
        # API Name =>会员等级管理-取得修改頁面
        # body--
        path = '/MemberLevelSetting/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>会员等级管理-取得詳細資料
        # body--/{id}
        path = '/MemberLevelSetting/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetailMemberCount(self, data):
        # API Name =>会员等级管理-取得該等級會員數
        # body--/{id}
        path = '/MemberLevelSetting/GetDetailMemberCount'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def update(self, data):
        # API Name =>会员等级管理-修改等級(更新)
        # body--/{updateParams}
        path = '/MemberLevelSetting/Update'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>会员等级管理-取得設定詳細資料頁面
        # body--
        path = '/MemberLevelSetting/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def updateIsDangerous(self, data):
        # API Name =>会员等级管理-更改危險等級設定
        # body--/{id}/{isDangerous}
        path = '/MemberLevelSetting/UpdateIsDangerous'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 公司入款帐户
class GroupAccount(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>公司入款帐户管理-取得頁面
        # body--
        path = '/GroupAccount/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>公司入款帐户管理-取得新增頁面
        # body--
        path = '/GroupAccount/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>公司入款帐户管理-取得詳細頁面
        # body--
        path = '/GroupAccount/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modify(self, data):
        # API Name =>公司入款帐户管理-取得修改頁面
        # body--
        path = '/GroupAccount/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>公司入款帐户管理-新增
        # body--/{createAccountParams}
        path = '/GroupAccount/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>公司入款帐户管理-取得公司入款帳戶詳細資料
        # body--/{id}
        path = '/GroupAccount/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateSubmit(self, data):
        # API Name =>公司入款帐户管理-修改
        # body--/{updateAccountParams}
        path = '/GroupAccount/UpdateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>公司入款帐户管理-刪除
        # body--/{id}
        path = '/GroupAccount/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>公司入款帐户管理-取得公司入款帳戶列表
        # body--
        path = '/GroupAccount/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def disable(self, data):
        # API Name =>公司入款帐户管理-停用
        # body--/{id}
        path = '/GroupAccount/Disable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def active(self, data):
        # API Name =>公司入款帐户管理-啟用
        # body--/{id}
        path = '/GroupAccount/Active'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def adjustSum(self, data):
        # API Name =>公司入款帐户管理-變更目前累積(調整)(歸零)
        # body--/{id}/{targetNumber}
        path = '/GroupAccount/AdjustSum'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def broadcastSumInfoUpdated(self, data):
        # API Name =>公司入款帐户管理-廣播更新
        # body--/{id}
        path = '/GroupAccount/BroadcastSumInfoUpdated'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllGroupAccountType(self, data):
        # API Name =>公司入款帐户管理-取得所有公司入款帳戶類型
        # body--
        path = '/GroupAccount/GetAllGroupAccountType'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def confirmAllCdnQrCodeImage(self, data):
        # API Name =>公司入款帐户管理-確認 CDN 上 QRCode 圖片
        # body--
        path = '/GroupAccount/ConfirmAllCdnQrCodeImage'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAvailableMinutes(self, data):
        # API Name =>公司入款帐户管理-更新有效分鐘數
        # body--/{id}/{args}
        path = '/GroupAccount/UpdateAvailableMinutes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateImage(self, data):
        # API Name =>公司入款帐户管理-更新圖片
        # body--/{qrCodefile}
        path = '/GroupAccount/UpdateImage'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data


# 线上支付商户
class GroupThirdParty(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>线上支付商户管理-取得列表頁面
        # body--
        path = '/GroupThirdParty/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_list(self, data):
        # API Name =>线上支付商户管理-取得線上支付商戶列表
        # body--
        path = '/GroupThirdParty/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>线上支付商户管理-取得新增頁面
        # body--
        path = '/GroupThirdParty/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_types(self, data):
        # API Name =>线上支付商户管理-取得線上商戶類型
        # body--
        path = '/GroupThirdParty/GetTypes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_third_party_type_list(self, data):
        # API Name =>线上支付商户管理-取得目前支付種類
        # body--
        path = '/GroupThirdParty/GetThirdPartyTypeList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>线上支付商户管理-取得明細頁面
        # body--
        path = '/GroupThirdParty/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modify(self, data):
        # API Name =>线上支付商户管理-取得修改頁面
        # body--
        path = '/GroupThirdParty/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create_dtpp_submit(self, data):
        # API Name =>线上支付商户管理-新增金流公司商戶資料
        # body--/{createDTPPSettingParams}
        path = '/GroupThirdParty/CreateDTPPSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_dtpp_detail(self, data):
        # API Name =>线上支付商户管理-取得新版金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/GetDTPPDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dtpp_disable(self, data):
        # API Name =>线上支付商户管理-停用金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/DTPPDisable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dtpp_active(self, data):
        # API Name =>线上支付商户管理-啟用金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/DTPPActive'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dtpp_reset(self, data):
        # API Name =>线上支付商户管理-歸零目前商戶累計金額
        # body--/{id}
        path = '/GroupThirdParty/DTPPReset'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def update_dtpp_name(self, data):
        # API Name =>线上支付商户管理-更新名稱
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def broad_cast_dtpp_sum_info_updated(self, data):
        # API Name =>线上支付商户管理-廣播累計資訊更新
        # body--/{id}
        path = '/GroupThirdParty/BroadcastDTPPSumInfoUpdated'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPMerchantData(self, data):
        # API Name =>线上支付商户管理-更新商戶資料
        # body--/{id}/{args}/{isNew}
        path = '/GroupThirdParty/UpdateDTPPMerchantData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPRange(self, data):
        # API Name =>线上支付商户管理-更新單次存款限額
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPRange'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPLimit(self, data):
        # API Name =>线上支付商户管理-更新總存款限額
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPLevelSettingIds(self, data):
        # API Name =>线上支付商户管理-更新可用之會員等級
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPLevelSettingIds'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPMemo(self, data):
        # API Name =>线上支付商户管理-更新備註
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPAvailableMinutes(self, data):
        # API Name =>线上支付商户管理-更新有效分鐘數
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPAvailableMinutes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dTPPDelete(self, data):
        # API Name =>线上支付商户管理-刪除金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/DTPPDelete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDepositLimitsCn(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}
        path = '/GroupThirdParty/GetDepositLimitsCn'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPDepositLimitsCn(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPDepositLimitsCn'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateDTPPRecommendationMemo(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPRecommendationMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPAmountLock(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPAmountLock'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPRecommendationAmountSettings(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPRecommendationAmountSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateThirdPartySettingSort(self, data):
        # API Name =>线上支付商户管理-
        # body--/{SettingId}/{PreviousSort}/{NextSort}
        path = '/GroupThirdParty/UpdateThirdPartySettingSort'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getDTPPTypeList(self, data):
        # 新增商戶取得支付商戶列表
        path = '/GroupThirdParty/GetDTPPTypeList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSettingDetail(self, data):
        # 取得商戶詳細設定資料
        path = '/GroupThirdParty/GetSettingDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getValidDTPP(self, data):
        # 新增商戶取得支付商戶
        path = '/GroupThirdParty/GetValidDTPP'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 余额宝管理
class Yuebao(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def create(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Create'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def setEnableTime(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/SetEnableTime'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def setMemberLevelSetting(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/SetMemberLevelSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def sort(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Sort'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def withdraw(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Withdraw'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def query(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Query'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def list(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/List'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Detail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def orderUserDetail(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/OrderUserDetail'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def history(self, data):
        # API Name =>余额宝管理-
        # body--/{id}/{pageSize}/{pageIndex}
        path = '/Yuebao/History'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberLevelSetting(self, data):
        # API Name =>余额宝管理-
        # body--
        path = '/Yuebao/GetMemberLevelSetting'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data


# 会员端设定
class PortalSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>会员端设定-取得會員端設定列表頁面
        # body--
        path = '/PortalSetting/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>会员端设定-取得新增頁面
        # body--
        path = '/PortalSetting/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>会员端设定-取得詳細資料頁面
        # body--
        path = '/PortalSetting/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>会员端设定-取得會員端設定列表
        # body--
        path = '/PortalSetting/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>会员端设定-會員端設定-新增成功
        # body--/{args}
        path = '/PortalSetting/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>会员端设定-取得會員端設定詳細資料
        # body--/{id}
        path = '/PortalSetting/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateName(self, data):
        # API Name =>会员端设定-取得會員端設定-修改設定名稱
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMarquee(self, data):
        # API Name =>会员端设定-取得會員端設定-修改跑馬燈內容
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateMarquee'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateRegisterSetting(self, data):
        # API Name =>会员端设定-會員注冊設定更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateRegisterSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentRegisterSetting(self, data):
        # API Name =>会员端设定-代理注冊設定更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateAgentRegisterSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # API Name =>会员端设定-備註更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>会员端设定-刪除
        # body--/{id}/{args}
        path = '/PortalSetting/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCompanyDepositToggle(self, data):
        # API Name =>会员端设定-關閉公司入款(false)
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateCompanyDepositToggle'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCompanyDepositMessage(self, data):
        # API Name =>会员端设定-公司入款修改內容更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateCompanyDepositMessage'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWithdrawToggle(self, data):
        # API Name =>会员端设定-關閉取款申請(false)
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWithdrawToggle'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWithdrawMessage(self, data):
        # API Name =>会员端设定-取款申請修改內容更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateWithdrawMessage'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWalletDepositToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWalletDepositToggle'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletDepositMessage(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateWalletDepositMessage'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletWithdrawToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWalletWithdrawToggle'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletWithdrawMessage(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateWalletWithdrawMessage'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletRemittancePortalToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWalletRemittancePortalToggle'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateIsYuebaoToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateIsYuebaoToggle'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 返水设定
class AnyTimeDiscountSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>时时返水-取得返水設定列表頁面
        # body--
        path = '/AnyTimeDiscount/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def createForBatch(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/CreateForBatch'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modifyForBatch(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ModifyForBatch'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modifyForATD(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ModifyForATD'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def activeDialog(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ActiveDialog'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def resetDialog(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ResetDialog'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detailDialog(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/DetailDialog'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>时时返水-
        # body--/{createParams}/{setting}/{detail}
        path = '/AnyTimeDiscount/CreateSubmit'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def verifyParams(self, data):
        # API Name =>时时返水-
        # body--/{createParams}
        path = '/AnyTimeDiscount/VerifyParams'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>时时返水-
        # body--/{id}
        path = '/AnyTimeDiscount/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>时时返水-
        # body--/{id}
        path = '/AnyTimeDiscount/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateHasDiscount(self, data):
        # API Name =>时时返水-
        # body--/{id}/{isDiscount}
        path = '/AnyTimeDiscount/UpdateHasDiscount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # API Name =>时时返水-
        # body--/{id}/{memo}
        path = '/AnyTimeDiscount/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateName(self, data):
        # API Name =>时时返水-
        # body--/{id}/{name}
        path = '/AnyTimeDiscount/UpdateName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDetails(self, data):
        # API Name =>时时返水-
        # body--/{id}/{details}
        path = '/AnyTimeDiscount/UpdateDetails'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyResetFinish(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/NotifyResetFinish'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getATDSetting(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}
        path = '/AnyTimeDiscount/GetATDSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getATDSettingDetail(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}
        path = '/AnyTimeDiscount/GetATDSettingDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getATDSupplierDetail(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetATDSupplierDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDSetting(self, data):
        # API Name =>时时返水-
        # body--/{setting}/{detail}
        path = '/AnyTimeDiscount/AlterATDSetting'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def alterATDLimit(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{limit}
        path = '/AnyTimeDiscount/AlterATDLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDMaxAmountLimit(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{Maxlimint}
        path = '/AnyTimeDiscount/AlterATDMaxAmountLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDAppointment(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{EnableAppointment}/{DisableAppointment}
        path = '/AnyTimeDiscount/AlterATDAppointment'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDAudit(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{audit}
        path = '/AnyTimeDiscount/AlterATDAudit'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def alterATDReceiveSwitch(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{receiveSwitch}
        path = '/AnyTimeDiscount/AlterATDReceiveSwitch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDPercentages(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{viewModel}
        path = '/AnyTimeDiscount/AlterATDPercentages'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDResetByDiscountSetting(self, data):
        # API Name =>时时返水-
        # body--/{password}/{discountSettingId}
        path = '/AnyTimeDiscount/AlterATDResetByDiscountSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDResetByOneMember(self, data):
        # API Name =>时时返水-
        # body--/{password}/{id}
        path = '/AnyTimeDiscount/AlterATDResetByOneMember'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getMemberDiscountTotalAmount(self, data):
        # API Name =>时时返水-
        # body--/{memberId}/{isClearCache}
        path = '/AnyTimeDiscount/GetMemberDiscountTotalAmount'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getMemberDiscountDetail(self, data):
        # API Name =>时时返水-
        # body--/{memberId}
        path = '/AnyTimeDiscount/GetMemberDiscountDetail'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getSettingRecords(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}
        path = '/AnyTimeDiscount/GetSettingRecords'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getIsATDResetRunning(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetIsATDResetRunning'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGPKReceivSwitchStatus(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetGPKReceivSwitchStatus'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def refreshMemberDiscountDetail(self, data):
        # API Name =>时时返水-
        # body--/{memberId}
        path = '/AnyTimeDiscount/RefreshMemberDiscountDetail'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getATDResetByDiscountSettingRecord(self, data):
        # 時返歸零歷程記錄 -2019/12/20
        path = '/AnyTimeDiscount/GetATDResetByDiscountSettingRecord'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getATDWithdrawSwitchLog(self, data):
        # 時返歸零歷程記錄 -2019/12/20
        path = '/AnyTimeDiscount/GetATDWithdrawSwitchLog'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 佣金设定
class CommissionSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>佣金设定-取得列表頁面
        # body--
        path = '/CommissionSetting/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>佣金设定-取得設定頁面
        # body--
        path = '/CommissionSetting/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>佣金设定-取得詳細資料頁面
        # body--
        path = '/CommissionSetting/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modify(self, data):
        # API Name =>佣金设定-取得修改頁面
        # body--
        path = '/CommissionSetting/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>佣金设定-取得設定列表
        # body--
        path = '/CommissionSetting/GetList'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>佣金设定-取得列表詳細資料
        # body--/{id}
        path = '/CommissionSetting/GetDetail'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def changeState(self, data):
        # API Name =>佣金设定-佣金設定更改狀態
        # body--/{id}
        path = '/CommissionSetting/ChangeState'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>佣金设定-刪除佣金設定
        # body--/{id}
        path = '/CommissionSetting/Delete'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def update(self, data):
        # API Name =>佣金设定-更新佣金設定
        # body--/{commissionSetting}
        path = '/CommissionSetting/Update'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>佣金设定-新增佣金設定
        # body--/{commissionSetting}
        path = '/CommissionSetting/CreateSubmit'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 娱乐城管理
class GameHallManagement(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理頁面
        # body--
        path = '/GameHallManagement/List'

        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理詳細資料頁面
        # body--
        path = '/GameHallManagement/Detail'

        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def history(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理歷史紀錄頁面
        # body--
        path = '/GameHallManagement/History'

        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getGameHallList(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理列表
        # body--
        path = '/GameHallManagement/GetGameHallList'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallListInfo(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理列表資訊
        # body--
        path = '/GameHallManagement/GetGameHallListInfo'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameCategoryTypes(self, data):
        # API Name =>娱乐城管理-取得娛樂城所有遊戲類型
        # body--/{gameSupplierType}
        path = '/GameHallManagement/GetGameCategoryTypes'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallDetail(self, data):
        # API Name =>娱乐城管理-取得娛樂城詳細
        # body--/{gameHallUrlText}/{jaguar}
        path = '/GameHallManagement/GetGameHallDetail'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallStatus(self, data):
        # API Name =>娱乐城管理-取得指定娛樂城狀態
        # body--/{gameHallUrlText}/{jaguar}
        path = '/GameHallManagement/GetGameHallStatus'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBackofficeUrl(self, data):
        # API Name =>娱乐城管理-取得娛樂城後台連結 Url
        # body--/{gameSupplierType}
        path = '/GameHallManagement/GetBackofficeUrl'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # API Name =>娱乐城管理-載入指定娛樂城歷史紀錄
        # body--/{gameHallUrlText}/{take}/{skip}/{query}
        path = '/GameHallManagement/LoadHistory'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def transferGameHallUrlText(self, data):
        # API Name =>娱乐城管理-把url的Text改成要顯示的Text
        # body--/{gameHallUrlText}/{jaguar}
        path = '/GameHallManagement/TransferGameHallUrlText'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyGameHallStatus(self, data):
        # API Name =>娱乐城管理-變更指定娛樂城狀態
        # body--/{gameSupplierType}/{isEnterable}
        path = '/GameHallManagement/ModifyGameHallStatus'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exitGameHall(self, data):
        # API Name =>娱乐城管理-踢出指定娛樂城所有會員
        # body--/{gameSupplierType}
        path = '/GameHallManagement/ExitGameHall'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def transferMoneyBack(self, data):
        # API Name =>娱乐城管理-轉回指定娛樂城所有錢包
        # body--/{gameSupplierType}
        path = '/GameHallManagement/TransferMoneyBack'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAllWallet(self, data):
        # API Name =>娱乐城管理-更新指定娛樂城所有錢包
        # body--/{gameSupplierType}
        path = '/GameHallManagement/UpdateAllWallet'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def calculateValidBet(self, data):
        # API Name =>娱乐城管理-娛樂城計算有效投注
        # body--/{searchParam}
        path = '/GameHallManagement/CalculateValidBet'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 站内信
class SiteMail(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>站内信-取得列表頁面
        # body--
        path = '/SiteMail/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def send(self, data):
        # API Name =>站内信-取得發送信件頁面
        # body--
        path = '/SiteMail/Send'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getInboxList(self, data):
        # API Name =>站内信-取得收件匣的信件列表
        # body--/{input}
        path = '/SiteMail/GetInboxList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getUnreadCount(self, data):
        # API Name =>站内信-取得未讀信件總數
        # body--
        path = '/SiteMail/GetUnreadCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSentboxList(self, data):
        # API Name =>站内信-取得寄件匣的信件列表
        # body--/{input}
        path = '/SiteMail/GetSentboxList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSearchMailDateList(self, data):
        # API Name =>站内信-取得搜尋日期用的列表
        # body--
        path = '/SiteMail/GetSearchMailDateList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteInboxMails(self, data):
        # API Name =>站内信-刪除收件匣的信件
        # body--/{inboxMailIds}
        path = '/SiteMail/DeleteInboxMails'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteSentboxMails(self, data):
        # API Name =>站内信-刪除寄件匣的信件
        # body--/{sentboxMailIds}
        path = '/SiteMail/DeleteSentboxMails'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def setInboxMailsAsReadOrUnread(self, data):
        # API Name =>站内信-設定收件匣信件已讀未讀
        # body--/{inboxMailIds}/{isRead}
        path = '/SiteMail/SetInboxMailsAsReadOrUnread'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMailDetail(self, data):
        # API Name =>站内信-取得信件詳細內容
        # body--/{mailId}
        path = '/SiteMail/GetMailDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMailReceiverList(self, data):
        # API Name =>站内信-取得收件人清單
        # body--/{input}
        path = '/SiteMail/GetMailReceiverList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllSiteMemberCount(self, data):
        # API Name =>站内信-取得全站會員數量
        # body--
        path = '/SiteMail/GetAllSiteMemberCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def sendMail(self, data):
        # API Name =>站内信-發送信件
        # body--/{input}
        path = '/SiteMail/SendMail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberSiteMailInfo(self, data):
        # API Name =>站内信-取得管端收件匣中，會員寄送的信件總數以及未讀的信件總數 (For 會員詳細頁)
        # body--/{memberId}
        path = '/SiteMail/GetMemberSiteMailInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyNewInboxMail(self, data):
        # API Name =>站内信-通知管端Client收件匣有新的信件 (供Portal/Mobile使用)
        # body--/{input}
        path = '/SiteMail/NotifyNewInboxMail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def uploadCustomExcel(self, data):
        # API Name =>站内信-
        # body--/{excelFile}
        path = '/SiteMail/UploadCustomExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def downloadCustomExcelValidateResult(self, data):
        # API Name =>站内信-
        # body--/{excelPath}
        path = '/SiteMail/DownloadCustomExcelValidateResult'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def downloadSampleExcel(self, data):
        # API Name =>站内信-下載匯入發信範本
        # body--
        path = '/SiteMail/DownloadSampleExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def downloadSiteMailExcelContent(self, data):
        # API Name =>站内信-
        # body--/{siteMailId}
        path = '/SiteMail/DownloadSiteMailExcelContent'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def announcement_GetList(self, data):
        # 站內信 - 促銷匣列表
        path = '/AnnouncementSiteMail/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def announcement_SendMail(self, data):
        path = '/AnnouncementSiteMail/SendMail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def announcement_Delete(self, data):
        path = '/AnnouncementSiteMail/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 前台网站管理


# 子帐号管理


# 站台系统值设置


# 活动管理
class ActivityManagement(object):
    # 红包派送
    class RedEnvelopeManagement:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def getList(self, data):
            # API Name =>红包派送-取得列表資料
            # body--
            path = '/RedEnvelopeManagement/GetList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def get_detail(self, data):
            # API Name =>红包派送-詳細資料
            # body--
            path = '/RedEnvelopeManagement/GetDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def addRedEnvelope(self, data):
            # 紅包匯入 - 1205
            path = '/RedEnvelopeManagement/AddRedEnvelope'
            self.response_data = self.__http.sendRequestForUploadFile(path, data)
            return self.response_data

    # 限时优惠
    class TimeLimitedEvent:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def loadNew(self, data):
            # API Name =>限时优惠-取得列表資料
            # body--
            path = '/TimeLimitedEvent/LoadNew'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getDetail(self, data):
            # API Name =>限时优惠-詳細資料
            # body--
            path = '/TimeLimitedEvent/GetDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getEventName(self, data):
            # API Name =>限时优惠-取得活動名稱
            # body--
            path = '/TimeLimitedEvent/GetEventName'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def memberJoinListLoadNew(self, data):
            # API Name =>限时优惠-會員參與名單
            # body--
            path = '/TimeLimitedEvent/MemberJoinListLoadNew'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 幸运转盘
    class LuckyWheelManagement:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def index(self, data):
            # API Name =>活动管理-取得列表頁面
            # body--
            path = '/LuckyWheelManagement/Index'
            self.response_data = self.__http.sendRequest('GET', path, data)
            return self.response_data

        def detail(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/Detail'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def createAndModify(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/CreateAndModify'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def preview(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/Preview'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def rewardRecord(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/RewardRecord'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def serialNumber(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/SerialNumber'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getEventList(self, data):
            # API Name =>活动管理-
            # body--/{filters}
            path = '/LuckyWheelManagement/GetEventList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def uploadRewardImage(self, data):
            # API Name =>活动管理-
            # body--/{imageFile}
            path = '/LuckyWheelManagement/UploadRewardImage'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def createNewEvent(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/CreateNewEvent'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getEventDetail(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/GetEventDetail'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def deleteEvent(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/DeleteEvent'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def updateEvent(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/UpdateEvent'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getRewardRecord(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/GetRewardRecord'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getRewardStatistics(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/GetRewardStatistics'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def createSerialNumber(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/CreateSerialNumber'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getSerialNumberList(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/GetSerialNumberList'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def sendRewards(self, data):
            # API Name =>活动管理-
            # body--/{eventID}/{recordIDs}
            path = '/LuckyWheelManagement/SendRewards'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getEventTypeList(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetEventTypeList'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getRewardTypeList(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetRewardTypeList'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getRuleTypeList(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetRuleTypeList'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getPortalUrl(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetPortalUrl'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def checkEventDateTimeDuplicated(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/CheckEventDateTimeDuplicated'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

    # 签到奖励
    class CheckInEvent:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def loadNew(self, data):
            # API Name =>签到奖励-取得列表資料
            # body--
            path = '/CheckInOffer/LoadNew'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 任务挑战
    class MissionReward:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def getList(self, data):
            # API Name =>任务挑战-取得列表資料
            # body--
            path = '/MissionReward/GetList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 时来运转
    class NewLuckyWheel:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def getList(self, data):
            # API Name =>时来运转-取得列表資料
            # body--
            path = '/NewLuckyWheel/GetList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data


# 封锁名单管理

class BlockListManagement(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def bankAccountGetList(self, data):
        # 封鎖名單管理-取得銀行帳戶列表
        path = '/BankAccountBlockManagement/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountGetGroupBank(self, data):
        # 封鎖名單管理-取得銀行列表
        path = '/BankAccountBlockManagement/GetGroupBank'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountExportExcel(self, data):
        # 封鎖名單管理-匯出銀行封鎖名單Excel
        path = '/BankAccountBlockManagement/ExportExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountAddBankAccountBlockInfo(self, data):
        # 封鎖名單管理-新增銀行帳戶封鎖名單
        path = '/BankAccountBlockManagement/AddBankAccountBlockInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountDeleteBankBlocks(self, data):
        # 封鎖名單管理-刪除銀行帳戶封鎖名單
        path = '/BankAccountBlockManagement/DeleteBankBlocks'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountDownloadSampleExcel(self, data):
        # 封鎖名單管理-下載銀行帳戶匯入範本
        path = '/BankAccountBlockManagement/DownloadSampleExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountCheckImportExcel(self, data):
        # 封鎖名單管理-檢查銀行帳戶匯入範本上傳
        path = '/BankAccountBlockManagement/CheckImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def bankAccountImportExcel(self, data):
        # 封鎖名單管理-銀行帳戶匯入範本上傳
        path = '/BankAccountBlockManagement/ImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def ipGetList(self, data):
        # 封鎖名單管理-取得IP列表
        path = '/IPBlockManagement/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipExportExcel(self, data):
        # 封鎖名單管理-匯出IP封鎖名單Excel
        path = '/IPBlockManagement/ExportExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipAddIPBlockInfo(self, data):
        # 封鎖名單管理-新增IP封鎖名單
        path = '/IPBlockManagement/AddIPBlockInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipDeleteIPBlocks(self, data):
        # 封鎖名單管理-刪除IP封鎖名單
        path = '/IPBlockManagement/DeleteIPBlocks'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipCheckImportExcel(self, data):
        # 封鎖名單管理-檢查IP匯入範本上傳
        path = '/IPBlockManagement/CheckImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def ipImportExcel(self, data):
        # 封鎖名單管理-IP匯入範本上傳
        path = '/IPBlockManagement/ImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def getCountrySetting(self, data):
        # 封鎖名單管理-取得國別阻擋名單
        path = '/CountryBlockManagement/GetCountrySetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getWhiteListSetting(self, data):
        # 封鎖名單管理-取得白名單IP名單
        path = '/CountryBlockManagement/GetWhiteListSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCountryBlockSetting(self, data):
        # 封鎖名單管理-更新國別阻擋名單
        path = '/CountryBlockManagement/UpdateCountryBlockSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkWhiteIpWhenAdd(self, data):
        # 封鎖名單管理-檢查新增白名單IP
        path = '/CountryBlockManagement/CheckWhiteIpWhenAdd'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWhiteListSetting(self,data):
        # 封鎖名單管理-更新白名單IP
        path = '/CountryBlockManagement/UpdateWhiteListSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data



# MyMine 金流设置
class MyMine(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getOrderInfos(self, data):
        # API Name =>MyMine 金流设置 -
        # body--
        path = '/MyMine/GetOrderInfos'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getMonthOrderInfo(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetMonthOrderInfo'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getDayOrderInfo(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetDayOrderInfo'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getLastSixMonthOrderInfo(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetLastSixMonthOrderInfo'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getGpkMerchant(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetGpkMerchant'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def uploadDocument(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{file}
        path = '/MyMine/UploadDocument'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data
