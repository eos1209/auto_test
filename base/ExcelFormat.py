'''
@Created by yuhsiang
@Date : 2019/4/23
'''

import xlrd
import openpyxl


class ReadExcel(object):
    def __init__(self, path, sheet_value):
        self.path = path
        self.sheetValue = sheet_value

    @property
    def getSheet(self):
        # 獲取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(self.sheetValue)
        return sheet

    @property
    def getRows(self):
        # 獲取行数
        row = self.getSheet.nrows
        return row

    @property
    def getCol(self):
        # 獲取列数
        col = self.getSheet.ncols
        return col

    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.getSheet.cell_value(i, 0))
        return TestData
