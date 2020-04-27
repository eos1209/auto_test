'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import time
import unittest
import os
from base import HTMLTestReportCN
from data_config.system_config import systemSetting

# 用例路径
case_path = os.path.join(os.getcwd(), "case/test_api")

print(case_path)


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern = "test*.py",
                                                   top_level_dir = None)
    return discover


#
# loader = unittest.TestLoader()
# suite = loader.discover("./case/test_api")

title = systemSetting()  # 報表選擇站台標題

now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
# 確定生成報告的路徑
filePath = "./test_reports/" + now + "-Test_Result.html"
fp = open(filePath, 'wb')
# 設定
setting = {
    "stream": fp,
    "title": 'API[' + title.report_title() + ']-自動化測試報告',
    # description=None
    "tester": '格明 - QA Team'
}
# 生成報告
runner = HTMLTestReportCN.HTMLTestRunner(**setting)

# 運行測試用例
runner.run(all_case())
# 關閉文件，否則會無法生成文件
fp.close()
