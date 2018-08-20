#coding=utf-8
'''
用discover方法遍历测试用例
'''
import unittest

test_dir = './case'

def get_allcase():
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_allcase())


