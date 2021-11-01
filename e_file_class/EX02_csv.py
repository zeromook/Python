#Ex02_csv.py
#csv = common String value

import csv

#1. 리스트의 데이터를 csv로 저장하기
# data = [[1,'김','책임'],[2,'박','선임'],[3,'맹','연구원']]
#
# with open('./data/imsi.csv','wt',encoding='utf-8') as f:
#     cout = csv.writer(f)
#     cout.writerows(data)


#2. csv로 저장된 파일을 읽어서 리스트 저장하기
result = []
with open('./data/imsi.csv','rt',encoding='utf-8') as readcsv:
    rf = csv.reader(readcsv)
    result = [row for row in rf if row]
print(result) #csv읽을때는 숫자들이 다 문자형이됨 숫자형으로 쓰려면 형변환을 따로 해주어야함