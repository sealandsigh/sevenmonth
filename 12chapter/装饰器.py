# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/22

import time

def zhuangshiqi(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@zhuangshiqi
def a():
    print('this is a')

a()