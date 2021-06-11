#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)

diver = webdriver.Chrome()
diver.get("http://www.baidu.com")

diver.find_element_by_id("kw").send_keys("selenium")
diver.find_element_by_id("su").click()

diver.quit()
