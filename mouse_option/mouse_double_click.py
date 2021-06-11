#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 全屏
driver.maximize_window()
time.sleep(2)

# 定位到要悬停的元素
double_click = driver.find_element_by_css_selector("#hotsearch-refresh-btn")

# 对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()

time.sleep(5)
driver.quit()
