#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from time import ctime, sleep
from selenium import webdriver

# 启动参数（指定运行主机与浏览器）
list = {'http://127.0.0.1:4444/wd/hub': 'chrome',
        'http://127.0.0.1:5555/wd/hub': 'firefox',
        'http://192.168.0.3:5556/wd/hub': 'chrome'
        }


# 测试用例
def test_baidu(host, browser):
    print('start:%s' % ctime())
    print(host, browser)
    driver = webdriver.Remote(
        command_executor=host,
        desired_capabilities={'platform': 'ANY',
                              'browserName': browser,
                              'version': '',
                              'javascriptEnabled': True
                              })
    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(browser)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.close()


threads = []
files = range(len(list))

# 创建线程
for host, browser in list.items():
    t = threading.Thread(target=test_baidu, args=(host, browser))
    threads.append(t)

if __name__ == '__main__':

    # 启动线程
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    # 主线程
    print('end:%s' % ctime())
