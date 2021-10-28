# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }

s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)

s = {1 ,2 ,3, 1, 2, 3}
print(s)
# print(s[0]) - set은 순서가 지정되있지 않아서 인덱스로 불러오기 불가능 에러

s3 = {3, 4, 5, 6}
print(s & s3) #교집합
print(s | s3) #합집합
print(s - s3) #차집합
#List 타입은 (& , | , -) 사용 불가능