'''
@Created by yuhsiang
@Date : 2019/12/17
'''

import logging
from time import sleep
from data_config import common_config


def get_logger():
    global logPath
    try:
        logPath
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    return logging


def SetDelayTime():
    # 因修改查詢頻率限制抽公用
    sleep(common_config.DelayTime)
