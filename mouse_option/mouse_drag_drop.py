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

# 定位元素的源位置
element = driver.find_element_by_css_selector('.s-hotsearch-content > li:nth-child(1) > a')
# print(element.text)
# ActionChains(driver).move_to_element(element).perform()

# 定位元素要移动到的目标位置
target = driver.find_element_by_id("kw")

# 对定位到的元素执行双击操作
ActionChains(driver).drag_and_drop(element, target).perform()

driver.quit()
