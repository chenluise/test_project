#coding=utf-8
'''
使用suite套件遍历测试用例,并将测试报告以HTML格式展现
'''

import HTMLTestRunner
import unittest

from test_case.case import test_receiveorder, test_wangguanjia_login
from test_case.nocase import test_creatorder

suite = unittest.TestSuite()
suite.addTest(test_wangguanjia_login.WangguanjiaLogin('test_wangguanjia_login'))
suite.addTest(test_creatorder.Creatorder('test_creatorder'))
suite.addTest(test_receiveorder.Receiveorder('test_receiveorder'))



if __name__ == '__main__':
    filename = 'F:\photo\oresult1.html'
    fp = file(filename,'wb')

    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'套件测试用例',
        description=u'用例执行情况：'
    )

    runner.run(suite)
    fp.close()



























