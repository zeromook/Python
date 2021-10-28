"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""
print("# (0) 인자도 없고 리턴값도 없는 함수")
def func():
    print("Inside Function")

func()
result = func() #호출된 시점이라 프린트됨
print(result) #Return 값이 없으니 None이 나옴


print("\n# (1) 리턴값이 여러개인 함수 ==> 사실 한개(튜플)로 리턴됨")
def func(args):
    return args+1, args-1, args*2

result = func(10)
print(result)
first , second , third = func(10)
print(first,second,third)
print(first + second - third)#+를 하거나 *를 하거나 다양한 응용가능 파이썬의 새로운 스타일



print("\n# (2)위치인자 (Positional argument)")
def func(greeting, name):
    print(greeting,"!!!!!",name+'님')

func('안녕','영묵') #안녕 !!!!! 영묵님
func('영묵','안녕') #순서대로 위치인자로 인해 영묵 !!!!! 안녕님 으로 출력됨

print("\n# (3)키워드인자 (Keyword argument)")
func(name='영묵2',greeting='안녕2') #데이터순서가 바뀌어도 키워드를 찾아서 출력됨 안녕2 !!!!! 영묵2님


print("\n# (4)")
def func(greeting, name="세뇨르"):#기본값(Default Value) 설정하기
    print(greeting,"!!!!!",name+'님')

# func('올라','세뇨리따','바이') - 에러남
# func('올라') - 에러남
func('올라')
func('올라','세뇨리따')

def method(a,b,c=100):
    return a+b+c
print(method(1,2,3)) #a=1  b=2  c=3
print(method(c=1,a=2,b=30))#a=2  b=30  c=1
print(method(10,20))#a=10  b=20  c=100




'''
#----------------------------------------------------------------
첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?
       # args에 7,8,9가 튜플로 들어간다
'''

print("\n#(5) 위치 인자 모으기 (*)")
def func(a,b,c=0,*args):     #뒤에 몇개의 매개변수가 추가될지 모를때 *args로 선언해준다 튜플형식으로 추가됨으로
    sum = a+b+c
    for i in args:           #튜플을 for문으로 돌려서 데이터를 빼오는 식을 추가해준다.
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))


print("\n#(6) 키워드 인자 모으기 (**)")

def func(a,b,c=0,*args,**kwargs):     #딕셔너리 타입으로 들어옴 키워드를 모른상태에서 알아서 추가하게 해주려면 **kwargs로 선언해준다.
    sum = a+b+c
    for i in args:
        sum += i
    for k in kwargs:                  #딕셔너리를 for문으로 돌려서 kwargs의 Value값들을 따오게끔 한다. 필요한건 value값뿐이기 때문 key는 kor,math....가 들어간다
        sum += kwargs[k]
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
print(func(1,2,3,kor=100,math=50))
print(func(1,2,kor=50,math=60,eng=40))
print(func(1,2,kor=50,java=40))

