# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False
print(type(hungry),type(sleepy))
print(not sleepy)

print(hungry and sleepy) #둘다 참일때만 True
print(hungry or sleepy) #둘중 하나만 참이여도 True


"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리      {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False
"""

if('아'):
    print('True') #답
else:
    print('False')

if([]):
    print('True2')
else:
    print('False2') #답

if(0):
    print('True3')
else:
    print('False3') #답

if(-1):
    print('True4') # 답
else:
    print('False4')

msg = "행복합시다."
if(msg.find("행복")): # 값이 0이여서 no로 떨어짐
    print("Okay")
else:
    print("No")

if(msg.find("가자") != -1): # 값이 -1이여서 Okay로 떨어짐 그래서 -1이 아닐때 참을 반환하게끔
    print("Okay")
else:
    print("No")