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
TouchAction(driver).tap(x=444, y=49).perform()
sleep(5)
TouchAction(driver).tap(x=89, y=108).perform()
sleep(5)
TouchAction(driver).tap(x=177, y=764).perform()
sleep(5)
TouchAction(driver).tap(x=146, y=63).perform()
sleep(5)
TouchAction(driver).tap(x=144, y=50).perform()
sleep(5)
TouchAction(driver).tap(x=94, y=156).perform()