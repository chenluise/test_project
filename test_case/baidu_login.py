# -*- coding: utf-8 -*-
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

time.sleep(5)

driver.find_element_by_xpath(u"(//a[contains(text(),'登录')])[2]").click()
time.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
driver.find_element_by_id("TANGRAM__PSP_10__userName").clear()
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("luxchan")
driver.find_element_by_id("TANGRAM__PSP_10__password").clear()
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("13476006547lux")
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
try:
    assert("luxchan", driver.find_element_by_xpath("//a[@id='s_username_top']/span").text)
except AssertionError as e:
    self.verificationErrors.append(str(e))

time.sleep(3)
driver.find_element_by_link_text(u"退出").click()
driver.find_element_by_link_text(u"确定").click()

