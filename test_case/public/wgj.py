#coding=utf-8

'''
公共调用模块，旺管家【登录】和【登出】
'''
import time


#登录

def wgj_login(self,username,password):
    driver = self.driver
    driver.find_element_by_xpath("//input[@type='text']").click()
    driver.find_element_by_xpath("//input[@type='text']").clear()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    driver.find_element_by_id("login").click()


#退出

def wgj_logout(self):
    driver = self.driver
    driver.find_element_by_xpath("//header[@id='header']/header/div[4]/ul/li/a/span/span").click()

    time.sleep(3)

    driver.find_element_by_xpath(u"//li[3]/a/span[contains(text(),'注销')]").click()