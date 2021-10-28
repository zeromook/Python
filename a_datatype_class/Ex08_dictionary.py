"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사***** )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three', 1:"first", 3:"third"}
# value 추출  사전[key이름]
print(dt[1]) #first 1:one이 덮어져서 first로 나온다.
print(dt[2]) #two
print(dt['3']) #three '3'과 3은 다른 key값이다.
print()
# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}
print(dt2[(3,4)])
print()


print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
dt2['korea'] = 'seoul' #존재하지 않는 키를 넣으면 자동으로 추가가됨
print(dt2)
dt2['korea'] = '대한민국'#존재하는 키를 넣으면 덮어씌워짐
print(dt2)
# 여러개 추가할 때
dt2.update({5:'five', 6:"six"})
print(dt2)
print()


print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt2[5])  #둘다 결과는 동일
print(dt2.get(5))

# Key와 Value만 따로 검색
print(dt2.keys())
print(dt2.values())
print(dt2.items())


#쭉 검색해서 출력
for k,v in dt2.items():
    print(k,'=', v)
print()



