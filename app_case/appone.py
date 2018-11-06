#coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep

desired_caps = {
    'platformName': 'Android',

    'deviceName': '127.0.0.1:62001',

    'platformVersion': '4.4.2',

    'appPackage': 'com.wandoujia.phoenix2',

    'appActivity': 'com.pp.assistant.activity.PPMainActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

sleep(5)
driver.find_element_by_id("com.wandoujia.phoenix2:id/apn").click()
sleep(3)
driver.find_element_by_name(u"分类").click()
sleep(3)
driver.find_element_by_name(u"必备").click()
sleep(3)
driver.find_element_by_name(u"推荐").click()