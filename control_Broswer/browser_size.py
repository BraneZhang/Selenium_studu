#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 参数数字为像素点
print("设置浏览器宽 480、高 800 显示")
driver.set_window_size(480, 800)
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.quit()
