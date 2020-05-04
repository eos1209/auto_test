import time
import datetime


def get_yesterday():
    # 今天日期
    today = datetime.date.today()
    # 昨天时间
    yesterday = today - datetime.timedelta(days=1)
    return yesterday
