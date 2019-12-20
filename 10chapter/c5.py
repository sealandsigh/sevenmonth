import re
a = "python abcd123&&\njava234c++"

print(re.findall('[a-z][a-z]',a))
print(re.findall('[a-z]{3,6}?',a))
