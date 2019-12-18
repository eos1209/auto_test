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


class UploadFile(object):

    def __init__(self, path, upload_name, filename):
        self.path = common_config.file_Path + path  # 檔案路徑
        self.upload_name = upload_name  # 上傳欄位
        self.filename = filename  # 上傳檔名
        self.open_file = open(self.path, 'rb')  # 開啟檔案
        Type = path.split('/')  # 以檔案資料夾路徑來判斷檔案上傳類型，採切割字串方式
        if Type[0] == 'document':
            self.file_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # 上傳類型
        elif Type[0] == 'image':
            self.file_type = 'image/jpeg'  # 上傳類型

    def Upload_file(self):  # 上傳檔案-方法
        data = {self.upload_name: (self.filename, self.open_file, self.file_type, {'Expires': '0'})}
        return data

    def Close_file(self):  # 檔案關閉-方法
        self.open_file.close()
