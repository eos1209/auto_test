import datetime
import calendar
import time
from datetime import date, timedelta


class EncryptError(Exception):
    pass


def get_yesterday():
    # 今天日期
    today = datetime.date.today()
    # 昨天时间
    yesterday = today - datetime.timedelta(days=1)
    return yesterday


def get_today():
    # 今天日期
    today = datetime.date.today()
    return today


def betRecord_start():
    # 投注紀錄查詢 -- 取得上個月一號的日期
    WagersTimeBegin = (date.today().replace(day=1) - timedelta(1)).replace(day=1).strftime("%Y/%m/%d")
    return WagersTimeBegin


def betRecord_end():
    #  -- 取得今天的日期
    WagersTimeBegin = date.today().replace().replace().strftime("%Y/%m/%d")
    return WagersTimeBegin


def get_todaynow():
    # 格式化成2016-03-20 11:45形式
    nows = time.strftime("%Y/%m/%d %H:%M", time.localtime())
    return nows


def get_todaynowS():
    # 格式化成2016-03-20 11:45:30形式
    nows = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
    return nows


def get_yesterdayS():
    # 取當前日期的前一天！格式化成2016-03-20 11:45:30形式
    now = datetime.datetime.now()
    yesterdayNow = now - datetime.timedelta(hours=23, minutes=59)
    return str(yesterdayNow)


def get_todaynow_Y():
    # 格式化成2016-03-20形式
    nows = time.strftime("%Y%m%d", time.localtime())
    return nows


def get_first_day():
    """ 當月的第一天 到 最後一天"""
    time = datetime.datetime.now()  # 年，月，日
    # 求該月第一天
    first_day = datetime.date(time.year, time.month, 1)
    days_num = calendar.monthrange(first_day.year, first_day.month)[1]  # 獲取一個月有多少天
    first_day_of_month = first_day + datetime.timedelta(days=days_num - 1)  # 當月的最後一天只需要days_num-1即可
    return str(first_day), str(first_day_of_month)


def get_next_first_day():
    """ 下個月的第一天 到 最後一天"""
    time = datetime.datetime.now()  # 年，月，日
    # 求該月第一天
    first_day = datetime.date(time.year, time.month, 1)
    days_num = calendar.monthrange(first_day.year, first_day.month)[1]  # 獲取一個月有多少天
    first_day_of_next_month = first_day + datetime.timedelta(days=days_num)  # 當月的最後一天只需要days_num-1即可
    xx = calendar.monthrange(first_day_of_next_month.year, first_day_of_next_month.month)[1]  # 獲取一個月有多少天
    first_day_of_month = first_day_of_next_month + datetime.timedelta(days=xx - 1)  # 當月的最後一天只需要days_num-1即可

    return str(first_day_of_next_month), str(first_day_of_month)


def timestamp_to_time(timestamp, ft='%Y-%m-%d %H:%M:%S'):
    """ 將時間戳轉換成固定格式的日期時間字符串 """
    time_local = time.localtime(timestamp)
    return time.strftime(ft, time_local)


def time_to_timestamp(dtime, ft='%Y-%m-%d %H:%M:%S'):
    """ 將日期時間字符串轉換成時間戳 """
    try:
        time_array = time.strptime(dtime, ft)
    except ValueError:
        time_array = time.strptime(dtime, '%Y-%m-%d')
    return int(time.mktime(time_array))


def days(d=3):
    """ 取 d 天前（負值）或 d 天后（正）的時間戳 """
    day_cal = datetime.datetime.now() + datetime.timedelta(days=d)
    # 转换为时间戳
    return int(time.mktime(day_cal.timetuple()))


if __name__ == '__main__':
    t = '2017-12-09'
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
    # print(encrypt('100000307111111'))
    # print(get_newest_file_of_path(os.path.join(os.path.dirname(os.path.abspath(".")), "report")))
    # print(get_files_by_createtime(os.path.join(os.path.dirname(os.path.abspath(".")), "report")))
    t = '2017-12-09'
    # tm = time_to_timestamp(t)
    # print(tm)
    # print(timestamp_to_time(tm))

    # print(timestamp_to_time(days(3)))
    # print(timestamp_to_time(days(-3)))
