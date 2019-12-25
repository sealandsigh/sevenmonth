# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/24

# map 方法实现
a = [1,2,3,4,5,6,7,8]

r = map(lambda x:x*x,a)
print(list(r))

# 列表推导式方法实现

#b = [i*i for i in a]
b = [i**2 for i in a if i >5 ]
print(b)
