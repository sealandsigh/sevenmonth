# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/22

firstwalk = 0

def wak(step):
    global firstwalk
    a = firstwalk + step
    firstwalk = a
    return  firstwalk

print(wak(2))
print(wak(3))
print(wak(4))
