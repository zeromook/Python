"""
totalScore = 0

for i in range(5):
    score = int(input("점수를 입력하세요 : "))
    totalScore += score

sum = totalScore/5
print("평균 = %.1f" % (sum))
"""


"""
text = input("문자열 입력 : ")
print(text[::-1])
"""

"""
import math
import numpy

total = 0
su = list(map(int,input("정수리스트 입력 : ").split()))
sum = numpy.mean(su)
std = math.sqrt(sum)
print("평균 :",sum)
print("표준편차 :%.2f" % std)
"""

"""
input_str = input("문자열을 입력하시오: ")
count = 0
num = 2

#Dictionary 세팅
dictionary = {}
for i in range(65,91): # 아스키코드 65..91 은 (A..Z+1)
    if(count==3): #규칙이
        num = num + 1
        count = 0
    dictionary[chr(int(i))] = num
    count = count + 1


answer = "" #answer 값 출력
for i in input_str:
    answer += str(dictionary[str(i)])

print(answer)
"""
"""
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j

print(result)
"""
"""
def even_filter(args):      #리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수
    result = [ r for r in args if r%2==0]
    return result

print(even_filter([1, 2, 4, 5, 8, 9, 10]))


def is_prime_number(a):     #주어진 수가 소수인지 아닌지 판단하는 함수
    for i in range(2,a/2+1):
        if a % i == 0:
            return False
    return True

print(is_prime_number(60))
print(is_prime_number(61))


주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )


def count_vowel(s):
    count = 0
    vowel = ["a","e","i","o","u"]
    for i in s:
        if i in vowel:
            count += 1
    return count

print(count_vowel("pythonian"))
"""
