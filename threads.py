#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from time import ctime, sleep


# 创建听音乐任务
def music(func):
    for i in range(2):
        print('I was listening to %s! %s' % (func, ctime()))
        sleep(2)


# 创建看电影任务
def move(func):
    for i in range(2):
        print('I was at the  %s! %s' % (func, ctime()))
        sleep(5)


# 创建线程数组
threads = []

# 创建线程 t1,并添加到线程数组
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)

# 创建线程 t2,并添加到线程数组
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':

    # 启动线程
    for i in threads:
        i.start()  # 开始线程活动

    # 守护线程
    for i in threads:
        i.join()  # 等待线程终止

    print('all end: %s' % ctime())
