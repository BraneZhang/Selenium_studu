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
def movie(func):
    for i in range(2):
        print('I was at the  %s! %s' % (func, ctime()))
        sleep(5)


# 判断文件类型，交给相应的函数执行
def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        movie(name)
    else:
        print('error: The format is not recognized!')


list = ['爱情买卖.mp3', '阿凡达.mp4']
files = range(len(list))

# 创建线程数组
threads = []

# 创建线程
for i in files:
    t = threading.Thread(target=player, args=(list[i],))
    threads.append(t)

if __name__ == '__main__':

    # 启动线程
    for i in threads:
        i.start()  # 开始线程活动

    # 守护线程
    for i in threads:
        i.join()  # 等待线程终止

    print('all end: %s' % ctime())
