"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""

import shutil
from pathlib import Path

# shutil.copy('Ex01_Path.py',Path('temp2/test2/abc/test.py'))   #파일복사
#
# shutil.copytree('temp2','../copytemp')                        #폴더 통쨰로 복사


shutil.rmtree('temp2')                                          #파일이 안에 들어있어도 통쨰로 폴더 삭제

