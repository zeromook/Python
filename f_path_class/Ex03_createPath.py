
from pathlib import Path


# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())  #현재경로
print(Path.home(),'\n') #home경로 Linux와 동일한 개념의 home

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
p1 = Path('Ex03_createPath.py')
tm = p1.stat().st_atime #파일생성시간 가져오는 명령어
print(tm)

from datetime import datetime
print(datetime.fromtimestamp(tm),'\n')  #파일생성시간 datetime으로 변환해서 가져오기
# ------------------------------------------------
# 3. 디렉토리 생성
# p1 = Path('imsi')           #폴더생성
# p1.mkdir(exist_ok=True)     #이미있는 폴더를 생성했을때 오류가 안나게 하려면 exist_ok=True
#
# p2 = Path('temp2/test2/abc')  #부모자식관계인 폴더를 생성할때는
# p2.mkdir(parents=True,exist_ok=True)        #parents=True
# ------------------------------------------------
# 4. 파일 생성
#write 만 해주면 됨


# ------------------------------------------------
#  5. 경로 제거
p3 = Path('temp2')
p3.rmdir()  #디렉토리가 비어있지 않으면 제거 불가능 자식부터 제거해야함