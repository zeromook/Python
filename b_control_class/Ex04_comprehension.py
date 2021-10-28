"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""


# 컨프리핸션 사용하지 않은 리스트 생성
"""
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,7):
    alist.append(n)
print(alist)

alist = list(range(1,7))
print(alist)

"""
#------------------------------------------------
# 리스트 컨프리핸션
blist = [ n for n in range(1,7)]#for문을 통해 1~6의 수를 n에 지정.
print(blist)

blist = [ n*2 for n in range(1,7)]#for문을 통해 1~6의 수를 n에 지정 그값에 *2를 한다.
print(blist)

blist = [ n*2 for n in range(1,7) if n%2==1]#for문을 통해 1~6의 수를 n에 지정하고 if를 통해 홀수인 경우에만 리스트로 담고 그값에 *2를 한다.
print(blist)

#r = 1~3
#c = 1~2

#밑코드와 결과는 동일
clist = [ (r,c) for r in range(1,4) for c in range(1,3)]
print(clist)

#위 코드를 이중 for문으로 풀어서 원래 스타일대로 작성
clist = []
for r in range(1,4):
    for c in range(1,3):
        clist.append((r,c))
print(clist)

#-------------------------------------------
# 딕셔러니 컨프리핸션

datas = (2,3,4)
adic = {i : i**2 for i in datas }
print(adic)
print()

word = "LOVE LOL"
wcnt = { letter : word.count(letter) for letter in word}
print(wcnt)


#------------------------------------------------
# 셋 컨프리핸션
print()
blist = { n for n in range(1,7)}#for문을 통해 1~6의 수를 n에 지정 그값에 *2를 한다.
print(blist)
print()














# -------------------------------------------------
# 프로젝트할 때 팀구호
#우리의결의= """취하고싶으면달려라
#맡은업무는반드시마치자
#노력없는성과는없다
#구글신과함께공부하자
#"""
#result = [ j[i*2] for i, j in enumerate(우리의결의.split('\n')]
#print(result)