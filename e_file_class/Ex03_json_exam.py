#Ex03_json_exam.py

import json

with open('./data/sample.json','rt',encoding='utf-8') as f:
    op = f.read()

jsfile = json.loads(op)

for k,v in jsfile.items():
    sum = int(v['price'])*int(v['count'])
    fruit = ['사과','망고','딸기']
    if k in fruit:
        print('%s는 %s개이고 가격은 %s$입니다.' % (k,v['count'],v['price']))
        print('%s의 총금액은 %d$입니다. \n' % (k,int(sum)))



