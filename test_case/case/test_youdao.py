# coding=utf-8
'''
有道云查询用例
'''

from selenium import webdriver
import unittest,time

class YoudaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        u'''有道搜索'''
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u"你好")
        driver.find_element_by_id("translateContent").submit()
        time.sleep(3)
        page_source = driver.page_source
        self.assertIn("hello",page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



