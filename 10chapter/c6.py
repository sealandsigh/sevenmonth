import re
# 匹配0次或无限多次

a = 'pythonaaaa0pytho0python1pythonn2'

print(re.findall('pythona+',a))