#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

# 向 cookie 的 name 和 value 添加会话信息。
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

# 遍历 cookies 中的 name 和 value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()
