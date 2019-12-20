import re
a = 'Java|C|C++|python|abc'

b = re.findall('php',a)
if len(b) > 0:
    print('字符串包含python')
else:
    print('字符串不包含python')

