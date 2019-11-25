'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import time
import unittest

from base import HTMLTestReportCN

loader = unittest.TestLoader()
suite = loader.discover("./case/test_api")

now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
# 確定生成報告的路徑
filePath = "./test_reports/" + now + "-Test_Result.html"
fp = open(filePath, 'wb')
# 設定
setting = {
    "stream": fp,
    "title": 'API[AB005]-自動化測試報告',
    # description=None
    "tester": '格明 - QA Team'
}
# 生成報告
runner = HTMLTestReportCN.HTMLTestRunner(**setting)

# 運行測試用例
runner.run(suite)
# 關閉文件，否則會無法生成文件
fp.close()
# sendMail.send_mail()
