msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

#(1) unpacking : 각요소를 분해(풀기)
a , b ,c = di
print(a)
print(b)
print(c)

#(2) enumerate() : 각요소와 인덱스를 같이 추출 **********************
user_list = ['개발자','코더','전문가','분석가']
for value in user_list:
    print(value)

print()

for idx,value in enumerate(user_list):
    print(idx , value)


#(3) zip() 두 리스트나 튜플값들을 각각 요소에 맞춰서 합쳐서 출력시켜줌
days = ['MON','THU','WED']                        #[('MON', 'sleeping'), ('THU', 'studing'), ('WED', 'plaing')]
doit = ['Sleeping','Studing','Plaing','Eating']   #{'MON': 'sleeping', 'THU': 'studing', 'WED': 'plaing'}
print(list(zip(days, doit)))
print(dict(zip(days, doit)))
