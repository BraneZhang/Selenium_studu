#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

# 获得 cookie 信息
cookie = driver.get_cookies()

# 将获得 cookie 的信息打印
print(cookie)
driver.quit()
