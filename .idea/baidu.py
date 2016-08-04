#-*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

sreach_window = driver.current_window_handle
print sreach_window

driver.find_element_by_link_text(u"登录").click()
driver.find_element_by_link_text(u"立即注册").click()

all_handle = driver.window_handles

print all_handle

print sreach_window