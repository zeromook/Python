print('\n1----------------------------------------------------------------------\n')
alist = ["A","B","C"]
blist = ["ㄱ","ㄴ","ㄷ"]
result = []

for a, b in enumerate(zip(alist, blist)):
    try:
        result.append(b[a])
    except IndexError:
        result.append("Error")

print(result)

print('\n2----------------------------------------------------------------------\n')
def sum_data( data_a, data_b ):
    for i in data_a:
        for j in data_b:
            result = i + j
        return result

a=[1,2]
b=[3,4]
print(sum_data(a,b))

print('\n3----------------------------------------------------------------------\n')

class Calculater:
    li = []
    def __init__(self,li):
        self.li = li
    def sum(self):
        sum = 0
        for i in self.li:
            sum += i
        print(sum)
    def avg(self):
        sum = 0
        avg = 0
        for i in self.li:
            sum += i
        avg=sum/len(self.li)
        print(avg)

cal = Calculater([1,2,3,4,5])
cal.sum()
cal.avg()

print('\n4----------------------------------------------------------------------\n')
score = ['국어','영어','수학']
sum = 0
for i in score:
    sc = input(i+"점수를 입력 ->>")
    sum += int(sc)
print('총점 -> %d' % sum)
print('평균 -> %.2f' % (sum/len(score)))

print('\n5----------------------------------------------------------------------\n')
sentens = input('문자열을 입력 :').split()
never = input('금지어를 입력 :').split()
for i in range(len(sentens)):
    for n in never:
        if n in sentens[i]:
            sentens[i] = sentens[i].replace(n,'*'*len(n))
            print(sentens[i])
print(" ".join(sentens))


print('\n6----------------------------------------------------------------------\n')

sum = 0
count = 0
try:
    with open('score.txt','r',encoding='utf-8') as f:
        while True:
            a = f.readline()
            if not a: break
            sum += float(a)
            count += 1
except FileNotFoundError as e:
    print('파일을 찾을 수 없음................///에러코드 -', e)
finally:
    avg = sum / count

try:
    with open('score.txt','a',encoding='utf-8') as f:
        f.write('\n평균값 : %.2f' % avg)
        print('파일작성이 완료되었습니다.')
except FileNotFoundError as e:
    print('파일을 찾을 수 없음................///에러코드 -', e)


