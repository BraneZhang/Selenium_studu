#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import ctime, sleep


# 创建听音乐任务
def music(func):
    for i in range(2):
        print('I was listening to music! %s' % ctime())
        sleep(2)


# 创建看电影任务
def move(func):
    for i in range(2):
        print('I was at the movies! %s' % ctime())
        sleep(5)


if __name__ == '__main__':
    music(u'爱情买卖')
    move(u'阿凡达')
    print('all end:', ctime())
