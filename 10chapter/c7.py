import re
# 边界匹配

qq = "100010000"

print(re.findall('0001$',qq))
print(re.match('1000',qq))
print(re.search('1000',qq))
t = re.search('1000',qq)
print(t.group())
