#coding=utf-8
'''
旺管家新建订单流程，使用代客下单方法
'''
from selenium import webdriver
from test_case.public import wgj
import unittest,time

class Creatorder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3000)
        self.base_url = "https://app.wang-guanjia.com/manage-dashboard/index.html#/page/signin"


    def test_creatorder(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        wgj.wgj_login(self,"chenlu","000000")

        time.sleep(3)

        driver.find_element_by_xpath("//ul[@id='nav']/li[7]/a/span").click()
        driver.find_element_by_xpath("//li[7]/ul/li/a/span").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(u"测试渠道cl")
        driver.find_element_by_link_text(u"测试渠道cl").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("1")
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("13476006547")
        driver.find_element_by_xpath("//div[@id='content']/section/div/div/div[4]/form/div[2]/button/span").click()
        driver.find_element_by_xpath("//tr[9]/td/md-radio-button/div/div").click()
        driver.find_element_by_xpath("//div[@id='content']/section/div/div/div[5]/div[6]/button").click()
        driver.find_element_by_xpath("//div[@id='content']/section/div/div/div/div/md-input-container/input").click()
        driver.find_element_by_xpath("//div[@id='content']/section/div/div/div/div/md-input-container/input").clear()
        driver.find_element_by_xpath("//div[@id='content']/section/div/div/div/div/md-input-container/input").send_keys("cl")

        time.sleep(3)

        driver.find_element_by_xpath("//div[@id='content']/section/div/div/div/div[4]/md-input-container/button").click()

        time.sleep(3)

        driver.find_element_by_xpath(u"(//a[contains(text(),'购买')])[3]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'购买')])[3]").click()
        driver.find_element_by_xpath(u"//a[contains(text(),'立即购买')]").click()

        time.sleep(3)

        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

        time.sleep(3)

        driver.find_element_by_xpath("//div[@id='content']/section/div/md-input-container[2]/button").click()

        time.sleep(5)

        driver.find_element_by_xpath("//md-dialog-actions/button/span").click()

        time.sleep(5)

        wgj.wgj_logout(self)

        time.sleep(5)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


