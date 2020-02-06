'''
@Created by loka
@Date : 2020/01/15
'''
import unittest

from data_config import common_config
from base.HTMLTestReportCN import HTMLTestRunner
from base.httpRequest import HttpRequest
from master_api import reports
from master_api.account_login import User


class WalletTransferRecordBaseTest(unittest.TestCase):
    """ 优惠钱包额度移转 - 相關 API 調用狀態"""

    def setUp(self):
        self.__http = HttpRequest()
        self.user = User(self.__http)
        self.walletTransferRecord = reports.WalletTransferRecord(self.__http)
        self.user.login()

    def tearDown(self):
        self.user.logout()

    def test_GameSupplierTransaction_relatedApi_status_01(self):
        """ 优惠钱包额度移转 - 搜尋"""
        data = {"TransactionTimeStart": common_config.BeginDate, "TransactionTimeEnd": common_config.EndDate}
        response_data = self.walletTransferRecord.search(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)

    def test_GameSupplierTransaction_relatedApi_status_02(self):
        """ 优惠钱包额度移转 - 匯出"""
        data = {"TransactionTimeStart": common_config.BeginDate, "TransactionTimeEnd": common_config.EndDate}
        response_data = self.walletTransferRecord.export(data)
        status_code = response_data[0]
        self.assertEqual(status_code, common_config.Status_Code)


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
