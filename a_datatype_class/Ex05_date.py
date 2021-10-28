
# import datetime
# today = datetime.date.today()
# print('today is ', today)

from datetime import date ,timedelta #년월일까지(date) , 날짜계산(timedelta)
today = date.today()
print('today is ',today)
print("연도 :",today.year)
print("월 :",today.month)
print("일 :",today.day)

#날짜 계산
print("어제 :",today+timedelta(days=-1))

#일주일 전 날짜
print("일주일 전 :",today+timedelta(weeks=-1))

#100일 후 날짜
print("100일 후 :",today+timedelta(days=+100))



#날짜형 <-> 문자형
# date -> str : strftime()
# str -> date : strptime()
from datetime import date,datetime #시분초까지(datetime)
today = datetime.today()
print(type(today))
print(today)

print(today.strftime("%Y년 %m월 %d일 %H:%M"))  #문자열 str타입

naljja = "1998-10-01 12:50:12"  #문자열
naljja2 = today.strptime(naljja,"%Y-%m-%d %H:%M:%S") #날짜형타입
print(type(naljja2))
print(naljja2)
print("연도",naljja2.year)
print("월",naljja2.month)
print("일",naljja2.day)