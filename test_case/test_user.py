#coding=utf-8
'''
参数化，读取txt数据
'''
from selenium import webdriver
import time


sourse = open('C:\Python27\data\user.txt','r')
values = sourse.readlines()
sourse.close()

driver = webdriver.Chrome()
driver.get("https://app.wang-guanjia.com/manage-dashboard/index.html#/page/signin")


for line in values:
    driver.find_element_by_xpath("//input[@type='text']").click()
    driver.find_element_by_xpath("//input[@type='text']").clear()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(line.split(",")[0])
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys(line.split(",")[1])
    driver.find_element_by_id("login").click()

    time.sleep(3)

driver.quit()




