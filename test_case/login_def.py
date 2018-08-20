#coding=utf-8
'''
----测试登录，遍历用例，断言，截图（每一个用例赋予一个方法def）---
 1用户名、密码正确
 2用户名正确、密码不正确
 3用户名正确、密码为空
 4用户名错误、密码正确
 5用户名为空、密码正确
'''
from selenium import webdriver
from test_case.public import wgj
import unittest
import time

class Testlogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(300)
        self.base_url = 'https://app.wang-guanjia.com/manage-dashboard/#/page/signin'

    def test_login(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(2)
        wgj.wgj_login(self,'chenlu','000000')
        time.sleep(2)
        self.assertEqual("CHENLU", driver.find_element_by_xpath("//*[@id=\"header\"]/header/div[4]/ul/li/a/span/span").text)
        self.driver.get_screenshot_as_file("F:\photo\o_1.jpg")
        wgj.wgj_logout(self)

    def test_psw_error(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(2)
        wgj.wgj_login(self,'chenlu','000001')
        self.assertEqual(u"用户名或密码错误", driver.find_element_by_css_selector("div.toast-message").text)
        self.driver.get_screenshot_as_file("F:\photo\o_2.jpg")
        time.sleep(2)

    def test_psw_null(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(2)
        wgj.wgj_login(self,'chenlu','')
        self.assertEqual(u"密码不能为空", driver.find_element_by_xpath("//div[@id='content']/section/div/div/div/div/div/div/form/fieldset/span/font").text)
        self.driver.get_screenshot_as_file("F:\photo\o_3.jpg")
        time.sleep(2)

    def test_user_error(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(2)
        wgj.wgj_login(self, 'chenl', '000000')
        self.assertEqual(u"账户不存在", driver.find_element_by_css_selector("div.toast-message").text)
        self.driver.get_screenshot_as_file("F:\photo\o_4.jpg")
        time.sleep(2)

    def test_user_null(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        wgj.wgj_login(self, '', '000000')
        self.assertEqual(u"用户名不能为空", driver.find_element_by_xpath("//div[@id='content']/section/div/div/div/div/div/div/form/fieldset/span/font").text)
        self.driver.get_screenshot_as_file("F:\photo\o_5.jpg")
        time.sleep(2)


    def tearDown(self):
        print ('自动测试完毕')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()