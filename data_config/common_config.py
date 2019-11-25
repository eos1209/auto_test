'''
@Created by yuhsiang
@Date : 2019/11/18
'''

import datetime as datetime
# Global setting
from datetime import date, timedelta

# 狀態碼
Status_Code = '200'

# 時間區間
BeginDate = (date.today() - timedelta(7)).strftime("%Y/%m/%d")
EndDate = date.today().strftime("%Y/%m/%d")
TodayDate = date.today().strftime("%Y/%m/%d")

# 美東時間轉換
transactionDateBegin = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
transactionDateEnd = (datetime.datetime.now() + timedelta(hours = 2)).strftime("%Y-%m-%d %H:%M:%S")

# 投注紀錄查詢 -- 取得上個月一號的日期
WagersTimeBegin = (date.today().replace(day=1) - timedelta(1)).replace(day=1).strftime("%Y/%m/%d")