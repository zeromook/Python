# myfile.py

#1. 전체 모듈을 임포트했을때
from mypackage import mymodule

print(mymodule.get_date())   #mymodule.으로 함수선언가능
print(mymodule.get_weather())
print()


#2. 별칭 부여시
print(my.get_date())   #my.으로 함수선언가능
print(my.get_weather())
print()


#3. 모듈에서 필요한 부분만 임포트할때
from mypackage.mymodule import get_weather#,get_date  #mymodule중에서 get_weather()만 임포트 여러개할때는 ,로 구분해서 적음
#print(get_date()) get_weather()만 임포트했으므로 사용불가능
print(get_weather())
print()


#4. 모듈에서 필요한 부분만 임포트하고 별칭부여
from mypackage.mymodule import  get_weather as gw
#print(get_date())
print(gw()) #별칭으로 사용하기
print()