# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/24

day = 0

# 这里也可以是个函数
swicher = {
    0: 'sunday',
    1: 'monday',
    2: 'tuedday'
}

day_name = swicher.get(day,'None')
print(day_name)