#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


if __name__ == '__main__':
    # para = [1,2]
    # a = calc(*para)
    # print(a)

    # person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
    #
    # person('Jack', 24, city='Beijing', job='Engineer')
    #
    # dic = {'status': 'single', 'wealth': 'poor'}
    # person('Dan', '30', **dic)
    # 定义元组
    tup1 = ('a', 'b', 3, 4)
    tup2 = (1, 2, 3)
    # 查看元组
    print(tup1[0])
    print(tup2[0:2])
    # 连接元组
    tup3 = tup1 + tup2
    print(tup3)
    # 复制元组
    tup4 = ("Hi!")
    print(tup4 * 3)