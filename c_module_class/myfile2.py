
 # 1. 전체 임포트
import mypackage.mymodule

print('Weather',mypackage.mymodule.get_weather())

# 2. 필요한것만 임포트
from mypackage import  mymodule

print('Weather',mymodule.get_weather())