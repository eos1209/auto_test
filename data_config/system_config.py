'''
@Created by loka
@Date : 2020/02/17
'''

""" 整理系統參數 """
# 1.讀取已填寫完成的資料分別帶入
import xlrd
import os


class systemSetting(object):
    def __init__(self):
        path = "D:/automation_test_project/test_data/document/system_config.xlsx"
        # self.path = os.path.abspath(path)
        self.file = xlrd.open_workbook(path)
        self.sheet = self.file.sheet_by_index(0)  # 0:05環境 1:06環境 2:07環境

    def Portal_config(self):  # Portal網址設定
        data = self.sheet.cell_value(1, 1)
        return data

    def Mobile_config(self):  # Mobile網址設定
        data = self.sheet.cell_value(2, 1)
        return data

    def Master_config(self):  # Master網址設定
        data = self.sheet.cell_value(3, 1)
        return data

    def siteName_config(self):  # Master站名
        data = self.sheet.cell_value(4, 1)
        return data

    def test_Member_config(self):  # 測試會員設定
        data = self.sheet.cell_value(5, 1)
        return data

    def test_Password_config(self):  # 會員密碼設定
        data = self.sheet.cell_value(6, 1)
        return data

    def MemberLevelSetting_config(self):  # 會員等及設定
        data = self.sheet.cell_value(7, 1)
        return data

    def MemberLevelSetting_2_config(self):  # 會員等及Id-2設定
        data = self.sheet.cell_value(8, 1)
        return data

    def DiscountSetting_config(self):  # 反水Id設定
        data = self.sheet.cell_value(9, 1)
        return data

    def DiscountSetting_2_config(self):  # 反水Id-2設定
        data = self.sheet.cell_value(10, 1)
        return data

    def other_Website_config(self):
        data = self.sheet.cell_value(11, 1)
        return data

    def batchTag_config(self):  # 批次標籤設定
        data = self.sheet.cell_value(12, 1)
        return data

    def singleTag_config(self):  # 會員標籤設定
        data = self.sheet.cell_value(13, 1)
        return data

    def agentLv1(self):  # 大股東設定
        data = self.sheet.cell_value(14, 1)
        return data

    def agentLv2(self):  # 股東設定
        data = self.sheet.cell_value(15, 1)
        return data

    def agentLv3(self):  # 總代理設定
        data = self.sheet.cell_value(16, 1)
        return data

    def agentLv4(self):  # 代理設定
        data = self.sheet.cell_value(17, 1)
        return data

    def commissionSetting_config(self):  # 傭金等級設定
        data = self.sheet.cell_value(18, 1)
        return data

    def commissionSetting_2_config(self):  # 傭金等級設定
        data = self.sheet.cell_value(19, 1)
        return data

    def batch_Member_config(self):
        data = self.sheet.cell_value(20, 1)
        return data

    def SabaSportMixParlaySubTickets_config(self):
        data = self.sheet.cell_value(21, 1)
        return data

    def SabaVirtualSportMixParlaySubTickets_config(self):
        data = self.sheet.cell_value(22, 1)
        return data

    def CmdParlaySubRawData_config(self):
        data = self.sheet.cell_value(23, 1)
        return data

    def IboParlaySubRawData(self):
        data = self.sheet.cell_value(24, 1)
        return data

    def SingParlaySubRawData(self):
        data = self.sheet.cell_value(25, 1)
        return data

    def ImsParlaySubRawData(self):
        data = self.sheet.cell_value(26, 1)
        return data

    def ImParlaySubRawData(self):
        data = self.sheet.cell_value(27, 1)
        return data

    def BetRecordHistory(self):
        data = self.sheet.cell_value(28, 1)
        return data

    def Contribution_gameSupplier(self):
        data = self.sheet.cell_value(29, 1)
        return int(data)

    def MasterMember(self):
        data = self.sheet.cell_value(30, 1)
        return data

    def NewLuckyWheel(self):
        data = self.sheet.cell_value(31, 1)
        return data

    def verifyDeposit(self):
        data = self.sheet.cell_value(32, 1)
        return data

    def LuckyWheel(self):
        data = self.sheet.cell_value(33, 1)
        return data

    def NewTimeLimitedEvent(self):
        data = self.sheet.cell_value(34, 1)
        return data

    def report_title(self):  # 報表標題
        data = self.sheet.cell_value(35, 1)
        return data

    def agent_link(self):  # 代理網址
        data = self.sheet.cell_value(38, 1)
        return data
