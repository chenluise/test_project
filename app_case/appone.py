#coding=utf-8

from appium import webdriver

desired_caps = {
    'platformName': 'Android',

    'deviceName': '127.0.0.1:62001',

    'platformVersion': '4.4.2',

    'appPackage': 'com.wandoujia.phoenix2',

    'appActivity': 'com.pp.assistant.activity.PPMainActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
