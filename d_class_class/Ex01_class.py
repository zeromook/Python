
"""
    자바인 경우 클래스 선언
    class Sample {
        //멤버변수
        String data = "hello";
        String name;
        //생성자 함수
        Sample(String name){
            this.name = name;
        }
    }
"""
"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

#파이썬 버젼
class Sample:
    data = 'Hello'
    def __init__(self,name):
        self.name = name
        print('__init__호출')
        print(name)

    def __del__(self):
        print('__del__호출')


s = Sample('홍길동')
print(s.name)
print(s.data)
del s
print('종료')


"""
    자바인 경우
    class Book{
        String bname;
        int count;
        Book(String bname){
            this.bname = bname;
            count++;
        }
    }
    
    Book b1 = new Book("자바란 무엇인가");
    Book b2 = new Book("파이썬이란 무엇인가");
    System.out.println("책의 갯수 : "+b1.count);   //1
    System.out.println("책의 갯수 : "+b2.count);   //1 b1과 b2는 다른 객체
"""

class Book:
    cnt = 0

    def __init__(self,title):
        self.title = title

    #일반함수
    def output(self):
        print('책 제목:',self.title)
        self.cnt += 1
        print('1. 총 갯수 :',self.cnt)

    #클래스함수
    @classmethod
    def output2(cls):
        cls.cnt += 1
        print('2. 총갯수',cls.cnt)

b1 = Book('행복이란')
b2 = Book('자바란')

Book.output2()
Book.output2()
Book.output2()


"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
"""







'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''


