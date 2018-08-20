# coding=utf-8
from selenium import webdriver
import  unittest
import time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="https://www.baidu.com"

    def test_baidu(self):
        u'''百度搜索用例ee'''
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title, U"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
