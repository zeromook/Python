"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""
# name = input("이름을 입력하세요")
# print("당신의 이름은",name,"입니다.")
# print("당신의 이름은 %s 입니다" % name)
# print("당신의 이름은 {} 입니다.".format(name))

#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input("나이를 입력하세요"))
# height = float(input("키를 입력하세요"))
# print("당신의 나이는 %s살 입니다." % (age+1))
# print("당신의 키는 %.1fcm 입니다." % height)

#----------------------------------
# 단을 입력받아 구구단을 구하기
dan = int(input("구할 단수를 입력하세요"))
for i in range(1,10):
    print(dan," X ",i," = ",dan*i)

print()
#-----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕' , '친구')
print('안녕' '친구')

for i in range(1,10,3):
    print(i, end=',' if i<5 else "") # print안에 if식 가능

print()

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3

import sys
args = sys.argv[1:]
for i in args:
    print(i)