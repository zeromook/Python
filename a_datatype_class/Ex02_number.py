"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25 숫자영 소문자오 2*8+5*1=16+5=21
            - 16진수  0x25 숫자영 소문자엑스2*16+5*1=32+5=37
"""

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : alt + shift + F10

""" [ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승 (n제곱)
    [참고]
        -자바 : 3/2 ==> 1
        -파이썬 : 3/2 ==> 1.5
        -파이썬 : 3//2 ==> 1
        
        
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        is      : 비교하는 객체의 주소가 같으면 true, 다르면 false
        is not  : 비교하는 객체의 주소가 다르면 true, 같으면 false 
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
      

    [참고] 증가(++), 감소(--) 연산자 없음         
"""

a = 5
b = 2

add = a + b
print("a + b = " + str(add))
#파이썬은 문자열 + 숫자가 안됨 그래서 스트링으로 형변환 해주어야함

#*************************************
#제발 변수명으로 str 사용하지 맙시다
print(a/b)# /한개는 실수
print(a//b)# //두개는 정수

""" [ 출력결과 ] 
        a + b = 7
        a - b = 3
        a * b = 10
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""

print(1j + 2j)
# ++증가 연산자 --감소연산자 파이썬에는 없음
print("Hello" is "Hello") #True
print("Hello" is not "Hello") #False

print("H" in "Hello") # True
print("H" not in "Hello") #False
