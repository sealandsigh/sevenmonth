# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/22

origin = 0

def factory(pos):
    def walk(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return pos
    return walk

tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(4))