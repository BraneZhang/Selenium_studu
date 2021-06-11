#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from time import ctime, sleep


# 创建超级播放器
def super_player(file, times):
    for i in range(2):
        print('Start playing： %s! %s' % (file, ctime()))
        sleep(times)


# 播放的文件与播放时长
list = {'爱情买卖.mp3': 3, '阿凡达.mp4': 5, '我和你.mp3': 4}
threads = []
files = range(len(list))

# 创建线程
for file, times in list.items():
    t = threading.Thread(target=super_player, args=(file, times))
    threads.append(t)

if __name__ == '__main__':

    # 启动线程
    for i in threads:
        i.start()  # 开始线程活动

    # 守护线程
    for i in threads:
        i.join()  # 等待线程终止

    print('all end: %s' % ctime())
