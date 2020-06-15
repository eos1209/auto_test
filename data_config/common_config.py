'''
@Created by yuhsiang
@Date : 2019/11/18
'''

import datetime as datetime
# Global setting
from datetime import date, timedelta
import time
import calendar

# 延遲時間
DelayTime = 60

# 狀態碼
Status_Code = '200'

# 時間區間
BeginDate = (date.today() - timedelta(7)).strftime("%Y/%m/%d")
EndDate = date.today().strftime("%Y/%m/%d")
TodayDate = date.today().strftime("%Y/%m/%d")

# 月初1號&月底
FirstDay = datetime.date(date.today().year, date.today().month, day = 1).strftime("%Y/%m/%d")
weekDay, Day = calendar.monthrange(datetime.date.today().year, datetime.date.today().month)
EndDay = datetime.date(datetime.date.today().year, datetime.date.today().month, day = Day).strftime("%Y/%m/%d")
# 美東時間轉換
transactionDateBegin = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
transactionDateEnd = (datetime.datetime.now() + timedelta(hours = 2)).strftime("%Y-%m-%d %H:%M:%S")

# 投注紀錄查詢 -- 取得上個月一號的日期
WagersTimeBegin = (date.today().replace(day = 1) - timedelta(1)).replace(day = 1).strftime("%Y/%m/%d")

# 新增會員-會員流水號
"""使用現在時間當流水編碼，格式為:月份+日期+分+秒"""
now = time.strftime("%m%d%M%S", time.localtime())

