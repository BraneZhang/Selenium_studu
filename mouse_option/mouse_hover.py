#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 全屏
driver.maximize_window()

# 定位到要悬停的元素
above = driver.find_element_by_id("s-usersetting-top")

# 对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

time.sleep(5)
driver.quit()
