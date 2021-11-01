"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인
#p = Path('c:\windows')
p = Path('c:\Windows')  #해당경로가 존재하지 않으면 에러발생
print(p)
print(p.resolve())  #절대경로로 바꿔줘서 출력
print('-'*50)

#child = []
#for x in p.iterdir():  #하위경로 출력하기
#    if x in p.is_dir():
#       child.append(x)

child = [a for a in p.iterdir() if a.is_dir()]  #디렉토리파일들만 가져오기

print(child)
