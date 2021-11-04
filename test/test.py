print('1----------------------------------------------------------------------\n')
total = []
try:
    with open('sample.txt', 'r', encoding='utf-8') as f:  #with로 파일을 오픈
        while True:                                       #while문으로 무한루프를 돌리고
            a = f.readline()
            if not a: break                               #파일에 더이상 라인이없으면 break
            total.append(int(a))
except FileNotFoundError as e:
     print('파일을 찾을 수 없음................///에러코드 -', e)

print('점수의 총합은 %d점 입니다.' % sum(total))              #sum내장함수로 total의 총합계산
print('점수의 평균은 %.2f점 입니다.' % (sum(total) / len(total)))#sum(total)로 평균계산

print('\n2----------------------------------------------------------------------\n')
total = []
try:
    with open('dream.txt','r',encoding='utf-8') as f:
        while True:
            a = f.readline()
            if not a: break
            total.append(a)
except FileNotFoundError as e:
    print('파일을 찾을 수 없음................///에러코드 -', e)

for idx,i in enumerate(total):
    print(str(idx)+'--'+i,end="")   #total을 하나씩 가져오는데 enumerate로 인덱스값도 같이 출력되게함


print('\n\n3----------------------------------------------------------------------\n')


count = 0
try:
    with open('dream.txt','r',encoding='utf-8')as f:
        a = f.read()
        for i in a:
            count += 1
        print("총 글자의 수 : %d" % count)
        print("총 단어의 수 : %d" % len(a.split(" ")))
        print("총 줄의 수 : %d" % len(a.split("\n")))
except FileNotFoundError as e:
    print('파일을 찾을 수 없음................///에러코드 -', e)


print('\n4----------------------------------------------------------------------\n')
import os
from datetime import datetime
import random
def createF(directoryname,filename):
    try:
        if not os.path.exists(directoryname):
            os.makedirs(directoryname)
            with open(filename, 'w', encoding='utf-8') as f:
                for i in range(10):
                    f.write(str(datetime.now()) + str(random.randrange(10))+'\n')
        print('파일이 정상적으로 작성되었습니다.')
    except OSError as e:
        print("OS 오류가 발생하였습니다. 에러코드 - ",e)

createF('logtemp','logtemp/temp_log.txt')

print('\n5----------------------------------------------------------------------\n')

