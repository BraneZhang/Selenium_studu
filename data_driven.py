#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver

file_info = open('info.txt', 'r')
values = file_info.readlines()
file_info.close()

for search in values:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    driver.quit()
