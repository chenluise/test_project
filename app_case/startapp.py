#coding=utf-8

from appium import webdriver

desired_caps = {
                'platformName':'Android',

                'deviceName':'0079e9828532ae57',

                'platformVersion':'7.0',

                'appPackage':'com.ningstech.edjyun',
                
                'appActivity':'com.vmanager.vgj.act.main.LogoActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
