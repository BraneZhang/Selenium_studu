#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from selenium.webdriver import Remote

driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities={'browserName': 'firefox',
                                      'version': '',
                                      'platform': 'ANY',
                                      'javascriptEnabled': True}
                )
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys('remote')
driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()
