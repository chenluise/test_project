# # -*- coding: utf-8 -*-
#
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://test.wang-guanjia.com/manage-dashboard/index.html#/page/signin")
#
# time.sleep(3)
#
#
# driver.find_element_by_xpath("//input[@type='text']").click()
# driver.find_element_by_xpath("//input[@type='text']").clear()
# driver.find_element_by_xpath("//input[@type='text']").send_keys("chenlu")
# driver.find_element_by_xpath("//input[@type='password']").clear()
# driver.find_element_by_xpath("//input[@type='password']").send_keys("000000")
# driver.find_element_by_id("login").click()
# time.sleep(2)
# driver.find_element_by_xpath("//ul[@id='nav']/li[8]/a/span").click()
# driver.find_element_by_xpath("//ul[@id='nav']/li[8]/ul/li/a/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//header[@id='header']/header/div[4]/ul/li/a/span/span").click()
#
# time.sleep(2)
#
#
# try:
#     assert(u"服务订单管理", driver.find_element_by_xpath("//div[@id='content']/section/div/div/h3").text)
# except AssertionError as e:
#     verificationErrors.append(str(e))
#
#
# driver.find_element_by_link_text(u"注销").click()
#
# time.sleep(2)
#
# print("test_wangguanjia_login 测试结束")
#
# driver.quit()





#coding=utf-8
from selenium import webdriver
import unittest,time

class WangguanjiaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://test.wang-guanjia.com/manage-dashboard/index.html#/page/signin"

    def test_wangguanjia_login(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("chenlu")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("000000")
        driver.find_element_by_id("login").click()
        driver.find_element_by_xpath("//ul[@id='nav']/li[8]/a/span").click()
        driver.find_element_by_xpath("//ul[@id='nav']/li[8]/ul/li/a/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//header[@id='header']/header/div[4]/ul/li/a/span/span").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
