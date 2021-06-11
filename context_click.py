#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://yunpan.360.cn")

# 定位到要右击的元素
right_click = driver.find_element_by_id("xx")

# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()
