#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver import Remote

# 浏览器列表
lists = {'http://localhost:5556/wd/hub': 'chrome',
         # 'http://192.168.0.3:5558/wd/hub': 'chrome',
         'http://localhost:5555/wd/hub': 'firefox'}

# 读取不同的浏览器执行脚本
for host, browser in lists.items():
    print(host, browser)
    driver = Remote(
        command_executor=host,
        desired_capabilities={'platform': 'ANY',
                              'browserName': browser,
                              'version': '',
                              'javascriptEnabled': True
                              })
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys('remote')
    driver.find_element_by_id("su").click()
    driver.close()
