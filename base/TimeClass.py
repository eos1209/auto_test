import datetime
import calendar
import time
from datetime import date, timedelta


def get_yesterday():
    # 今天日期
    today = datetime.date.today()
    # 昨天时间
    yesterday = today - datetime.timedelta(days = 1)
    return yesterday


def get_today():
    # 今天日期
    today = datetime.date.today()
    return today


def betRecord_start():
    # 投注紀錄查詢 -- 取得上個月一號的日期
    WagersTimeBegin = (date.today().replace(day = 1) - timedelta(1)).replace(day = 1).strftime("%Y/%m/%d")
    return WagersTimeBegin


def get_todaynow():
    # 格式化成2016-03-20 11:45形式
    nows = time.strftime("%Y/%m/%d %H:%M", time.localtime())
    return nows


def get_todaynow_Y():
    # 格式化成2016-03-20 11:45形式
    nows = time.strftime("%Y%m%d", time.localtime())
    return nows


def get_first_day():
    """ 當月的第一天 到 最後一天"""
    time = datetime.datetime.now()  # 年，月，日
    # 求該月第一天
    first_day = datetime.date(time.year, time.month, 1)
    days_num = calendar.monthrange(first_day.year, first_day.month)[1]  # 獲取一個月有多少天
    first_day_of_month = first_day + datetime.timedelta(days = days_num - 1)  # 當月的最後一天只需要days_num-1即可
    return str(first_day), str(first_day_of_month)


def get_next_first_day():
    """ 下個月的第一天 到 最後一天"""
    time = datetime.datetime.now()  # 年，月，日
    # 求該月第一天
    first_day = datetime.date(time.year, time.month, 1)
    days_num = calendar.monthrange(first_day.year, first_day.month)[1]  # 獲取一個月有多少天
    first_day_of_next_month = first_day + datetime.timedelta(days = days_num)  # 當月的最後一天只需要days_num-1即可
    xx = calendar.monthrange(first_day_of_next_month.year, first_day_of_next_month.month)[1]  # 獲取一個月有多少天
    first_day_of_month = first_day_of_next_month + datetime.timedelta(days = xx - 1)  # 當月的最後一天只需要days_num-1即可

    return str(first_day_of_next_month), str(first_day_of_month)

# time = datetime.datetime.now()  # 年，月，日
# # 求該月第一天
# first_day = datetime.date(time.year, time.month, 1)
# print('該月第一天:' + str(first_day))
# # 求前一個月的第一天
# # 前一個月最後一天
# pre_month = first_day - datetime.timedelta(days=1)  # timedelta是一個不錯的函式
# print('前一個月最後一天:' + str(pre_month))
# # 前一個月的第一天
# first_day_of_pre_month = datetime.date(pre_month.year, pre_month.month, 1)
# print('前一個月的第一天:' + str(first_day_of_pre_month))
# # 求後一個月的第一天
# days_num = calendar.monthrange(first_day.year, first_day.month)[1]  # 獲取一個月有多少天
# first_day_of_next_month = first_day + datetime.timedelta(days=days_num)  # 當月的最後一天只需要days_num-1即可
# print('後一個月的第一天:' + str(first_day_of_next_month))
