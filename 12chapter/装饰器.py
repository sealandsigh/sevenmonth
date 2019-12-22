# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/22

import time

def zhuangshiqi(func):
    def wrapper(*args,**kwargs):
        print(time.time())
        func(*args,**kwargs)
    return wrapper

@zhuangshiqi
def a(func_name):
    print('this is a'+func_name)

# def zhuangshiqi1(func):
#     print(time.time())
#     return func

# f = zhuangshiqi1(a)
# f()

a('nihao')