import re

a = 'life is short, i use python'
r = re.search('life(.*)python',a)
print(r.group(1))
