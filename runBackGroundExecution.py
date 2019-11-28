'''
@Created by yuhsiang
@Date : 2018/12/10
'''

import unittest

loader = unittest.TestLoader()
suite = loader.discover("./case/test_execution/")
unittest.TextTestRunner().run(suite)


