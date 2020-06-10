'''
@Created by loka
@Date : 2020/05/22
'''

import unittest

from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from base.TimeClass import betRecord_start
from base.TimeClass import get_todaynow
from master_api import reports
from master_api.account_login import User
from data_config.system_config import systemSetting


class test_kindCategories(unittest.TestCase):
    """Master投注记录查询 -- 驗證資料"""

    def setUp(self):
        self.config = systemSetting()  # 系統參數
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.betRecords = reports.BetRecords(self.__http)
        self.user.login()
        self.first_day = betRecord_start()
        self.today = get_todaynow()

    def tearDown(self):
        self.user.logout()

    def game_type(self, array):  # 取得每個娛樂廳參數
        # 0:Video 1:Sport 2:Lottery 3:Slot 4:Board 5:Fish
        response_data = self.betRecords.getKindCategories({})
        get_list = response_data[1][array]['Categories']
        kind_list = list()
        for i in range(len(get_list)):
            kind_list.append(get_list[i]['PropertyName'])
        return kind_list

    def export_file_validate(self, data):
        # 注單查詢匯出檔案 驗證
        print(data)  # 注單Id
        response_data = self.betRecords.export(data)
        if not response_data[1]['fileVirtualPath'] is None:
            return 0
        else:
            return 1

    def advance_export_file_validate(self, data):
        response_data = self.betRecords.advancedExportV2(data)
        if not response_data[1]['fileVirtualPath'] is None:
            return 0
        else:
            return 1

    def get_BetIdDetail_validate(self, data):
        response_data = self.betRecords.search(data)
        if not response_data[1]['PageData'] is None:
            return 0
        else:
            return 1

    def advance_BetIdDetail_validate(self, data, betId):
        response_data = self.betRecords.advancedLoadV2(data)
        response_betId = response_data[1]['Data'][0]['BetId']
        print(response_betId)
        if response_betId == betId:
            return 0
        else:
            return 1

    def advance_SingSport_BetIdDetail_validate(self, data, betId):
        response_data = self.betRecords.advancedLoadV2(data)
        response_betId = response_data[1]['Data'][0]['TransactionId']
        print(response_betId)
        if response_betId == betId:
            return 0
        else:
            return 1

    def advance_PrgSlot_BetIdDetail_validate(self, data, betId):
        response_data = self.betRecords.advancedLoadV2(data)
        response_betId = response_data[1]['Data'][0]['BetId']
        betId = betId + 'B'
        print(response_betId)
        if response_betId == betId:
            return 0
        else:
            return 1

    def advance_Pt2Slot_BetIdDetail_validate(self, data, betId):
        response_data = self.betRecords.advancedLoadV2(data)
        response_betId = response_data[1]['Data'][0]['GameCode']
        print(response_betId)
        if response_betId == betId:
            return 0
        else:
            return 1

    def advance_Mg_BetIdDetail_validate(self, data, betId):
        response_data = self.betRecords.advancedLoadV2(data)
        response_betId = response_data[1]['Data'][0]['GameCode']
        print(response_betId)
        if response_betId == betId:
            return 0
        else:
            return 1

    def game_Type_Name_search(self, data, gameTypeName):
        response_data = self.betRecords.search(data)
        response_gameType = response_data[1]['PageData'][0]['GameType']
        if gameTypeName == response_gameType:
            return 0
        else:
            return 1

    def test_Video_BetRecord_AllProcess_0(self):
        """取得真人聽所有注單流程"""
        global RawWagersId
        game_list = self.game_type(0)
        for i in range(len(game_list)):
            gameCategories = game_list.pop()  # 取得所有娛樂廳種類
            if gameCategories == 'Mg2Real':  # 針對Mg2進行個案處理
                pass
            else:
                search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                               "connectionId": self.user.info()}
                response_data = self.betRecords.search(search_data)  # 查詢
                if not response_data[1]['PageData']:
                    print(str(gameCategories) + '沒有注單')
                    pass
                else:
                    print(gameCategories + '將進行這些驗證')
                    get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
                    get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
                    betRecord_detail = {"id": get_betRecord_Id}
                    response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
                    for i in range(len(response_data[1]['List'])):
                        if response_data[1]['List'][i]['Name'] == '注单号码':
                            RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                            # print(RawWagersId)
                    rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                        "RawWagersId": RawWagersId, "connectionId": self.user.info()}
                    rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)  # 注單號查詢
                    rawWagers_search_advance = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories], "RawWagersId": RawWagersId},
                        "pageSize": 100}
                    self.betRecords.advancedLoadV2(rawWagers_search_advance)  # 注單號進階查詢
                    export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
                    export_data_result = self.export_file_validate(export_data)  # 匯出
                    advance_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "pageSize": 100}
                    advance_data_result = self.advance_BetIdDetail_validate(advance_data, RawWagersId)  # 注單號進階查詢
                    advance_export_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "category": gameCategories}
                    advance_export_result = self.advance_export_file_validate(advance_export_data)  # 進階匯出
                    gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                           "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                           "connectionId": self.user.info()}
                    gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                            get_Game_type)  # 遊戲名稱查詢
                    print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                          gameTypeName_search_result)
                    self.assertEqual(
                        bool(
                            rawWagers_search_result == export_data_result == advance_data_result == advance_export_result
                            == gameTypeName_search_result), True)

    def test_Sport_BetRecord_AllProcess_1(self):
        """取得體育聽所有注單流程"""
        global RawWagersId
        game_list = self.game_type(1)
        for i in range(len(game_list)):
            gameCategories = game_list.pop()  # 取得所有娛樂廳種類
            if gameCategories == 'SingSport':  # 針對3Sing進行個案處理
                pass
            else:
                search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                               "connectionId": self.user.info()}
                response_data = self.betRecords.search(search_data)  # 查詢
                if not response_data[1]['PageData']:
                    print(str(gameCategories) + '沒有注單')
                    pass
                else:
                    print(gameCategories + '將進行這些驗證')
                    get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
                    get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
                    betRecord_detail = {"id": get_betRecord_Id}
                    response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
                    for i in range(len(response_data[1]['List'])):
                        if response_data[1]['List'][i]['Name'] == '注单号码' \
                                or response_data[1]['List'][i]['Name'] == '交易标号':
                            RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                            # print(RawWagersId)
                    rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                        "RawWagersId": RawWagersId, "connectionId": self.user.info()}
                    rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
                    export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
                    export_data_result = self.export_file_validate(export_data)
                    advance_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "pageSize": 100}
                    advance_data_result = self.advance_BetIdDetail_validate(advance_data, RawWagersId)
                    advance_export_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "category": gameCategories}
                    advance_export_result = self.advance_export_file_validate(advance_export_data)
                    gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                           "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                           "connectionId": self.user.info()}
                    gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                            get_Game_type)  # 遊戲名稱查詢
                    print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                          gameTypeName_search_result)
                    self.assertEqual(bool(rawWagers_search_result == export_data_result == advance_data_result
                                          == advance_export_result == gameTypeName_search_result), True)

    def test_Lottery_BetRecord_AllProcess_2(self):
        """取得彩票聽所有注單流程"""
        global RawWagersId
        game_list = self.game_type(2)
        for i in range(len(game_list)):
            gameCategories = game_list.pop()  # 取得所有娛樂廳種類
            search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                           "connectionId": self.user.info()}
            response_data = self.betRecords.search(search_data)  # 查詢
            if not response_data[1]['PageData']:
                print(str(gameCategories) + '沒有注單')
                pass
            else:
                print(gameCategories + '將進行這些驗證')
                get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
                get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
                betRecord_detail = {"id": get_betRecord_Id}
                response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
                for i in range(len(response_data[1]['List'])):
                    if response_data[1]['List'][i]['Name'] == '注单号码' or response_data[1]['List'][i]['Name'] == '注单号' or \
                            response_data[1]['List'][i]['Name'] == '交易单序号':
                        RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                        # print(RawWagersId)
                rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                    "RawWagersId": RawWagersId, "connectionId": self.user.info()}
                rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
                export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
                export_data_result = self.export_file_validate(export_data)
                advance_data = {
                    "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                     "GameCategories": [gameCategories]}, "pageSize": 100}
                advance_data_result = self.advance_BetIdDetail_validate(advance_data, RawWagersId)
                advance_export_data = {
                    "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                     "GameCategories": [gameCategories]}, "category": gameCategories}
                advance_export_result = self.advance_export_file_validate(advance_export_data)
                gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                       "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                       "connectionId": self.user.info()}
                gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                        get_Game_type)  # 遊戲名稱查詢
                print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                      gameTypeName_search_result)
                self.assertEqual(
                    bool(
                        rawWagers_search_result == export_data_result
                        == advance_data_result == advance_export_result == gameTypeName_search_result), True)

    def test_Slot_BetRecord_AllProcess_3(self):
        """取得電子廳所有注單流程"""
        global RawWagersId
        game_list = self.game_type(3)
        for i in range(len(game_list)):
            gameCategories = game_list.pop()  # 取得所有娛樂廳種類
            if gameCategories == 'PrgSlot' or gameCategories == 'Pt2Slot' or gameCategories == 'Mg2Slot' \
                    or gameCategories == 'Mg2Html5' or gameCategories == 'Cq9Slot':  # 針對PP電子和PT電子還有MG電子、Html5進行個案處裡
                pass
            else:
                search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                               "connectionId": self.user.info()}
                response_data = self.betRecords.search(search_data)  # 查詢
                if not response_data[1]['PageData']:
                    print(str(gameCategories) + '沒有注單')
                    pass
                else:
                    print(gameCategories + '將進行這些驗證')
                    get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
                    get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
                    betRecord_detail = {"id": get_betRecord_Id}
                    response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
                    for i in range(len(response_data[1]['List'])):
                        if response_data[1]['List'][i]['Name'] == '注单号码':
                            RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                        # print(RawWagersId)
                    rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                        "RawWagersId": RawWagersId, "connectionId": self.user.info()}
                    rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
                    export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
                    export_data_result = self.export_file_validate(export_data)
                    advance_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "pageSize": 100}
                    advance_data_result = self.advance_BetIdDetail_validate(advance_data, RawWagersId)
                    advance_export_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "category": gameCategories}
                    advance_export_result = self.advance_export_file_validate(advance_export_data)
                    gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                           "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                           "connectionId": self.user.info()}  # 遊戲名稱查詢
                    gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                            get_Game_type)  # 遊戲名稱查詢
                    print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                          gameTypeName_search_result)
                    self.assertEqual(bool(
                        rawWagers_search_result == export_data_result == advance_data_result
                        == advance_export_result == gameTypeName_search_result), True)

    def test_Board_BetRecord_AllProcess_4(self):
        """取得棋牌廳所有注單流程"""
        global RawWagersId
        game_list = self.game_type(4)
        for i in range(len(game_list)):
            gameCategories = game_list.pop()  # 取得所有娛樂廳種類
            search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                           "connectionId": self.user.info()}
            response_data = self.betRecords.search(search_data)  # 查詢
            if not response_data[1]['PageData']:
                print(str(gameCategories) + '沒有注單')
                pass
            else:
                print(gameCategories + '將進行這些驗證')
                get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
                get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
                betRecord_detail = {"id": get_betRecord_Id}
                response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
                for i in range(len(response_data[1]['List'])):
                    if response_data[1]['List'][i]['Name'] == '注单号码':
                        RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                    # print(RawWagersId)
                rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                    "RawWagersId": RawWagersId, "connectionId": self.user.info()}
                rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
                export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
                export_data_result = self.export_file_validate(export_data)
                advance_data = {
                    "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                     "GameCategories": [gameCategories]}, "pageSize": 100}
                advance_data_result = self.advance_BetIdDetail_validate(advance_data, RawWagersId)
                advance_export_data = {
                    "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                     "GameCategories": [gameCategories]}, "category": gameCategories}
                advance_export_result = self.advance_export_file_validate(advance_export_data)
                gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                       "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                       "connectionId": self.user.info()}  # 遊戲名稱查詢
                gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                        get_Game_type)  # 遊戲名稱查詢
                print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                      gameTypeName_search_result)
                self.assertEqual(
                    bool(
                        rawWagers_search_result == export_data_result == advance_data_result
                        == advance_export_result == gameTypeName_search_result), True)

    def test_Fish_BetRecord_AllProcess_5(self):
        """取得捕魚廳所有住單流程"""
        global RawWagersId
        game_list = self.game_type(5)
        for i in range(len(game_list)):
            gameCategories = game_list.pop()  # 取得所有娛樂廳種類
            if gameCategories == 'Cq9Fish':  # 針對PP電子和PT電子還有MG電子、Html5進行個案處裡
                pass
            else:
                search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                               "connectionId": self.user.info()}
                response_data = self.betRecords.search(search_data)  # 查詢
                if not response_data[1]['PageData']:
                    print(str(gameCategories) + '沒有注單')
                    pass
                else:
                    print(gameCategories + '將進行這些驗證')
                    get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
                    get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
                    betRecord_detail = {"id": get_betRecord_Id}
                    response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
                    for i in range(len(response_data[1]['List'])):
                        if response_data[1]['List'][i]['Name'] == '注单号码':
                            RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                            print(RawWagersId)
                    rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                        "RawWagersId": RawWagersId, "connectionId": self.user.info()}
                    rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
                    # rawWagers_search_advance = {
                    #     "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                    #                      "GameCategories": [gameCategories], "RawWagersId": RawWagersId}, "pageSize": 100}
                    # self.betRecords.advancedLoadV2(rawWagers_search_advance)  # 注單號進階查詢
                    export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
                    export_data_result = self.export_file_validate(export_data)
                    advance_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "pageSize": 100}
                    advance_data_result = self.advance_BetIdDetail_validate(advance_data, RawWagersId)
                    advance_export_data = {
                        "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                         "GameCategories": [gameCategories]}, "category": gameCategories}
                    advance_export_result = self.advance_export_file_validate(advance_export_data)
                    gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                           "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                           "connectionId": self.user.info()}  # 遊戲名稱查詢
                    gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                            get_Game_type)  # 遊戲名稱查詢
                    print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                          gameTypeName_search_result)
                    self.assertEqual(
                        bool(
                            rawWagers_search_result == export_data_result
                            == advance_data_result == advance_export_result == gameTypeName_search_result), True)

    def test_Round_RM_search(self):
        """個案處理-RM棋牌局號查詢驗證"""
        global RoundId
        gameCategories = 'DhBoard'
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '局编号':
                    RoundId = response_data[1]['List'][i]['Value']  # 局號
                    print(RoundId)
            round_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                          "Round": RoundId, "connectionId": self.user.info()}
            response_data = self.betRecords.advancedLoadV2(round_data)
            response_SerialId = response_data[1]['Data'][0]['SerialId']
            if RoundId == response_SerialId:
                round_data_result = 0
            else:
                round_data_result = 1
            self.assertEqual(round_data_result, 0)

    def test_Round_Rg2LotteryBeauty_search(self):
        """個案處理-GPK視訊彩票局號查詢驗證"""
        global RoundId
        gameCategories = 'Rg2LotteryBeauty'
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '游戏局号':
                    RoundId = response_data[1]['List'][i]['Value']  # 局號
                    print(RoundId)
            round_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                          "Round": RoundId, "connectionId": self.user.info()}
            response_data = self.betRecords.advancedLoadV2(round_data)
            response_SerialId = response_data[1]['Data'][0]['GameSerialId']
            if RoundId == response_SerialId:
                round_data_result = 0
            else:
                round_data_result = 1
            self.assertEqual(round_data_result, 0)

    def test_Round_Rg2Slot_search(self):
        """個案處理-GPK電子局號查詢驗證"""
        global RoundId
        gameCategories = 'Rg2Slot'
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '游戏局编号':
                    RoundId = response_data[1]['List'][i]['Value']  # 局號
                    print(RoundId)
            round_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                          "Round": RoundId, "connectionId": self.user.info()}
            response_data = self.betRecords.advancedLoadV2(round_data)
            response_SerialId = response_data[1]['Data'][0]['SerialId']
            if RoundId == response_SerialId:
                round_data_result = 0
            else:
                round_data_result = 1
            self.assertEqual(round_data_result, 0)

    def test_Round_Rg2Fish_search(self):
        """個案處理-GPK捕魚局號查詢驗證"""
        global RoundId
        gameCategories = 'Rg2Fish'
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '游戏局编号':
                    RoundId = response_data[1]['List'][i]['Value']  # 局號
                    print(RoundId)
            round_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                          "Round": RoundId, "connectionId": self.user.info()}
            response_data = self.betRecords.advancedLoadV2(round_data)
            response_SerialId = response_data[1]['Data'][0]['SerialId']
            if RoundId == response_SerialId:
                round_data_result = 0
            else:
                round_data_result = 1
            self.assertEqual(round_data_result, 0)

    def test_Round_Rg2Real_search(self):
        """個案處理-GPK真人局號查詢驗證"""
        global RoundId
        gameCategories = 'Rg2Real'
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '游戏局编号':
                    RoundId = response_data[1]['List'][i]['Value']  # 局號
                    print(RoundId)
            round_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                          "Round": RoundId, "connectionId": self.user.info()}
            response_data = self.betRecords.advancedLoadV2(round_data)
            response_SerialId = response_data[1]['Data'][0]['SerialId']
            if RoundId == response_SerialId:
                round_data_result = 0
            else:
                round_data_result = 1
            self.assertEqual(round_data_result, 0)

    def test_Round_PngSlot_search(self):
        """個案處理-Png電子局號查詢驗證"""
        global RoundId
        gameCategories = 'PngSlot'
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '局号':
                    RoundId = response_data[1]['List'][i]['Value']  # 局號
                    print(RoundId)
            round_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                          "Round": RoundId, "connectionId": self.user.info()}
            response_data = self.betRecords.advancedLoadV2(round_data)
            response_SerialId = response_data[1]['Data'][0]['SerialId']
            if RoundId == response_SerialId:
                round_data_result = 0
            else:
                round_data_result = 1
            self.assertEqual(round_data_result, 0)

    def test_3Sing_process(self):
        """個案處理-3Sing體育查詢驗證"""
        global RawWagersId
        gameCategories = 'SingSport'  # 取得所有娛樂廳種類
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            print(gameCategories + '將進行這些驗證')
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '交易标号':
                    RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                    # print(RawWagersId)
            rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                "RawWagersId": RawWagersId, "connectionId": self.user.info()}
            rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
            export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
            export_data_result = self.export_file_validate(export_data)
            advance_data = {
                "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                 "GameCategories": [gameCategories]}, "pageSize": 100}
            advance_data_result = self.advance_SingSport_BetIdDetail_validate(advance_data, RawWagersId)
            advance_export_data = {
                "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                 "GameCategories": [gameCategories]}, "category": gameCategories}
            advance_export_result = self.advance_export_file_validate(advance_export_data)
            gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                   "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                   "connectionId": self.user.info()}
            gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                    get_Game_type)  # 遊戲名稱查詢
            print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                  gameTypeName_search_result)
            self.assertEqual(bool(rawWagers_search_result == export_data_result == advance_data_result
                                  == advance_export_result == gameTypeName_search_result), True)

    def test_pt_slot_process(self):
        """個案處理-Pt電子查詢驗證"""
        global RawWagersId
        gameCategories = 'Pt2Slot'  # 取得所有娛樂廳種類
        search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                       "connectionId": self.user.info()}
        response_data = self.betRecords.search(search_data)  # 查詢
        if not response_data[1]['PageData']:
            print(str(gameCategories) + '沒有注單')
            pass
        else:
            print(gameCategories + '將進行這些驗證')
            get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
            get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
            betRecord_detail = {"id": get_betRecord_Id}
            response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
            for i in range(len(response_data[1]['List'])):
                if response_data[1]['List'][i]['Name'] == '游戏代碼':
                    RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
                    # print(RawWagersId)
            rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                "RawWagersId": RawWagersId, "connectionId": self.user.info()}
            rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
            export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
            export_data_result = self.export_file_validate(export_data)
            advance_data = {
                "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                 "GameCategories": [gameCategories]}, "pageSize": 100}
            advance_data_result = self.advance_Pt2Slot_BetIdDetail_validate(advance_data, RawWagersId)
            advance_export_data = {
                "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
                                 "GameCategories": [gameCategories]}, "category": gameCategories}
            advance_export_result = self.advance_export_file_validate(advance_export_data)
            gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
                                   "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
                                   "connectionId": self.user.info()}
            gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
                                                                    get_Game_type)  # 遊戲名稱查詢
            print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
                  gameTypeName_search_result)
            self.assertEqual(bool(rawWagers_search_result == export_data_result == advance_data_result
                                  == advance_export_result == gameTypeName_search_result), True)

    # def test_pp_slot_process(self):
    #     """個案處理-PP電子查詢驗證"""
    #     global RawWagersId
    #     gameCategories = 'PrgSlot'  # 取得所有娛樂廳種類
    #     search_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
    #                    "connectionId": self.user.info()}
    #     response_data = self.betRecords.search(search_data)  # 查詢
    #     if not response_data[1]['PageData']:
    #         print(str(gameCategories) + '沒有注單')
    #         pass
    #     else:
    #         print(gameCategories + '將進行這些驗證')
    #         get_betRecord_Id = response_data[1]['PageData'][0]['Id']  # 注單Id
    #         get_Game_type = response_data[1]['PageData'][0]['GameType']  # 遊戲名稱
    #         betRecord_detail = {"id": get_betRecord_Id}
    #         response_data = self.betRecords.getRawData(betRecord_detail)  # 注單原始資料
    #         for i in range(len(response_data[1]['List'])):
    #             if response_data[1]['List'][i]['Name'] == '交易标号':
    #                 RawWagersId = response_data[1]['List'][i]['Value']  # 注單號
    #             # print(RawWagersId)
    #         rawWagers_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
    #                             "RawWagersId": RawWagersId, "connectionId": self.user.info()}
    #         rawWagers_search_result = self.get_BetIdDetail_validate(rawWagers_search)
    #         export_data = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories]}
    #         export_data_result = self.export_file_validate(export_data)
    #         advance_data = {
    #             "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
    #                              "GameCategories": [gameCategories]}, "pageSize": 100}
    #         advance_data_result = self.advance_PrgSlot_BetIdDetail_validate(advance_data, RawWagersId)
    #         advance_export_data = {
    #             "searchParams": {"WagersTimeBegin": self.first_day, "WagersTimeEnd": self.today,
    #                              "GameCategories": [gameCategories]}, "category": gameCategories}
    #         advance_export_result = self.advance_export_file_validate(advance_export_data)
    #         gameTypeName_search = {"WagersTimeBegin": self.first_day, "GameCategories": [gameCategories],
    #                                "GameTypeName": get_Game_type, "GameTypeNameIsLike": 'false',
    #                                "connectionId": self.user.info()}
    #         gameTypeName_search_result = self.game_Type_Name_search(gameTypeName_search,
    #                                                                 get_Game_type)  # 遊戲名稱查詢
    #         print(rawWagers_search_result, export_data_result, advance_data_result, advance_export_result,
    #               gameTypeName_search_result)
    #         self.assertEqual(bool(rawWagers_search_result == export_data_result == advance_data_result
    #                               == advance_export_result == gameTypeName_search_result), True)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
