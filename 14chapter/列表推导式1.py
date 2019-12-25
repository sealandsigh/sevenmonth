# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/24

student = {
    '朱嘉骏': 18,
    '刘迪': 20,
    '猪猪': 21
}

r = {v:k for k,v in student.items()}
print(r)
r1 = (k for k,v in student.items())
print(r1)

for x in r1:
    print(x)