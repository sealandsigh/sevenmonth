import re
a = 'abc,acc,acd,adc,aca'

print(re.findall('a[^cd]c',a))
