'''
@Created by yuhsiang
@Date : 2018/12/20
'''

import logging


def get_logger():
    global logPath
    try:
        logPath
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    return logging
