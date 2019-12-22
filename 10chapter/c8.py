import re

a = 'life is short, i use python'
b = 'life is short, i use python,is good python'
r = re.search('life(.*)python',a)
r1 = re.findall('life(.*)python',a)
r2 = re.search('life(.*)python(.*)python',b)
r3 = re.findall('life(.*)python(.*)python',b)
# print(r.group(1))
# print(r1)
print(r2.group(0,1,2))
print(r2.groups())
print(r3)
