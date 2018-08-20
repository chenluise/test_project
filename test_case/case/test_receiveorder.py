#coding=utf-8
'''
旺管家接单全流程
'''
from selenium import webdriver
from test_case.public import wgj
import unittest,time

class Receiveorder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3000)
        self.base_url = "https://app.wang-guanjia.com/manage-dashboard/index.html#/page/signin"

    def test_receiveorder(self):
        driver = self.driver
        driver.get(self.base_url)

        time.sleep(3)

        wgj.wgj_login(self,"feiziying","666666")

        time.sleep(3)

        driver.find_element_by_xpath(u"//a/span[contains(text(),'订单管理')]").click()

        time.sleep(3)

        driver.find_element_by_xpath("//a[contains(@href, '#/supplierOrderSystem/normalOrder/userServiceOrderList')]").click()

        time.sleep(3)

        driver.find_element_by_link_text(u"全部").click()

        time.sleep(3)

        driver.find_element_by_xpath(u"//div[@id='content']/section/div/div[2]/div/div/div/div[2]/div/div/ul/li/table/tbody/tr/td[9]/button/span[contains(text(),'接单')]").click()

        time.sleep(3)

        driver.find_element_by_xpath("//md-radio-button/div/div").click()

        time.sleep(3)

        driver.find_element_by_xpath("//md-dialog-actions/div/button/span").click()

        time.sleep(3)

        driver.find_element_by_xpath(u"//div[@id='content']/section/div/div[2]/div/div/div/div[2]/div/div/ul/li/table/tbody/tr/td[9]/button/span[contains(text(),'上门服务')]").click()

        time.sleep(3)

        driver.find_element_by_xpath("//md-dialog-actions/button").click()

        time.sleep(3)

        driver.find_element_by_xpath(u"//div[@id='content']/section/div/div[2]/div/div/div/div[2]/div/div/ul/li/table/tbody/tr/td[9]/button/span[contains(text(),'确认服务完成')]").click()

        time.sleep(5)

        driver.find_element_by_xpath("//md-dialog-actions/button[2]").click()

        time.sleep(5)

        driver.find_element_by_xpath("//md-dialog-actions/button").click()

        time.sleep(5)

        wgj.wgj_logout(self)

        time.sleep(5)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
