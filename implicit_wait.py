#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
input_ = driver.find_element_by_id("kw22")
input_.send_keys('selenium')
driver.quit()
