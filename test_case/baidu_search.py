#coding=utf-8
'''
参数化，从txt中取数据进行百度搜索功能
'''

from selenium import webdriver
import time

sourse = open('C:\Python27\data\user.txt','r')
values = sourse.readlines()
sourse.close()

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

for line in values:
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(line.split(",")[0])
    driver.find_element_by_id("su").click()
    time.sleep(2)

driver.quit()

