#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")
driver.find_element_by_id('translateContent').send_keys('hello')

# 提交输入框的内容
driver.find_element_by_id('translateContent').submit()
driver.quit()
