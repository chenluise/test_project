#coding=utf-8

'''针对发送邮件的特例，百度搜索后输出html测试报告，并且打上时间标签'''

from selenium import webdriver
import unittest
import HTMLTestRunner
import time
# from test_case.case
import test_baidu,test_youdao


if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # suite.addTest(test_baidu.BaiduTest('test_baidu'))
    # suite.addTest(test_youdao.YoudaoTest('test_youdao'))

    suite = unittest.TestSuite()
    tests = [test_baidu.BaiduTest('test_baidu'),test_youdao.YoudaoTest('test_youdao')]
    suite.addTests(tests)

    now=time.strftime("%Y-%m-%d %H.%M.%S")

    '''方法一'''

    # filename = 'F:\photo\oresult.html'
    # fp = file(filename, 'wb')
    #
    # # runner = unittest.TextTestRunner()
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'百度搜索测试报告',
    #     description=u'用例执行情况：'
    # )
    # runner.run(suite)
    #
    # fp.close()



    '''方法二'''

    with open('F:\photo\oresult'+now+'.html','wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u"百度搜索测试报告",
            description=u"用例执行情况：",
            verbosity=2
        )
        runner.run(suite)

        f.close()

