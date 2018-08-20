#coding=utf-8
'''
使用suite套件遍历测试用例,并将log写入txt文件
'''

import unittest
from test_case.case import test_baidu,test_youdao

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_baidu.BaiduTest("test_baidu"))
    suite.addTest(test_youdao.YoudaoTest("test_youdao"))

    with open("UnittestTextReport.txt","a+") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

