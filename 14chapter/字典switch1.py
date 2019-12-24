# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/24

day = 100

def get_sunday():
    return 'sunday'

def monday():
    return  'monday'

def tuesday():
    return 'tuesday'

def get_default():
    return 'unkonw'

# 这里也可以是个函数
swicher = {
    0: get_sunday,
    1: monday,
    2: tuesday
}

def get_sunday():
    return 'sunday'

def monday():
    return  'monday'

def tuesday():
    return 'tuesday'

def get_default():
    return 'unkonw'

day_name = swicher.get(day, get_default)()
print(day_name)