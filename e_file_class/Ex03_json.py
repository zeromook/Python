# Ex03_json
import json

with open('./data/temp.json','rt',encoding='utf-8')as f:
    data = f.read()

print('*'*50)
items = json.loads(data)

print(data)
print(items)


print(type(data))  #str 값임
print(type(items)) #dict 내가원하는 값만 빼오는거 쌉가능

for k,v in items.items():
    print(k,'-----',v)
    print(v['Job'])
