#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')

# 鼠标悬停相“设置”链接
hover = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(hover).perform()

# 打开搜索设置
driver.find_element_by_class_name('setpref').click()

# 保存设置
driver.find_element_by_css_selector('#se-setting-7 > a.prefpanelgo').click()
time.sleep(1)

# 接收弹窗
driver.switch_to.alert.accept()
driver.quit()
