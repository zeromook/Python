"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****************************)
    4- 소괄호 () 사용
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = (1,2,3,1)
print(t)
print(t[1])
print()

# (2) 튜플은 요소를 변경하거나 삭제 안됨
print('------------------- 2 -----------------')
#t[1] = 0 에러남
#del t[1] 에러남
#del t 요소를 변경/삭제하는것만 안되고 통으로 삭제는 가능
print()
"""
    - list
        a = list()
        a = [] 대괄호
    - set
        b = set()
        b = {x,y} 값이 들어있는 중괄호
    - dictionary
        c = dictionary()
        c = {} 중괄호
    - tuple
        d = tuple()
        d = () 소괄호
"""


# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')
# t2 = 1,2,3,1  #괄호를 생략해도 됨 권장하진않음 가독성 떨어지기때문
# print(type(t2))
t2 = (9,) #******************************
#하나의 요소의 튜플을 만드려면 ,를 붙여주어야함!!!!!!!!!
print(type(t2))
print()


# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')
print(t2[0])
print(t + t2)
print(t * 3)