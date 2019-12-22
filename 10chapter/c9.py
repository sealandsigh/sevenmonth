import json

json_str = '{"name":"zhujiajun","age":18}'
json_str1 = '[{"name":"zhujiajun","age":18},{"name":"zhujiajun","age":18}]'

student = json.loads(json_str1)
print(type(student))
print(student[0]['name'])