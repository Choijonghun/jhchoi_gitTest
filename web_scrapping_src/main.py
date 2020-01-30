'''
본 프로젝트는 매일 아침마다 
구직 사이트의 페이지 개수와 정보를 추출하여 엑셀 문서로
정리하는 프로그램을 제작하기 위함

Module
기능들을 집합해둔 것

import 명령어를 사용해 모듈을 가져옴
ex)
import math #math 모듈을 import(수입해온다)
print(math.ceil(1.2))

그러나 사용하지 않는 기능들 또한 import 해오기 때문에 비효율적

효율적으로 사용하는 예제문
from math import ceil,fsum
print(ceil(1.2))
print(fsum([1,2,3]))

함수 이름을 바꿔 줄 수도 있음
from math import ceil,fsum as sexy_sum
print(ceil(1.2))
print(sexy_sum([1,2,3]))

from math import ceil,fsum as sexy_sum
print(ceil(1.2))
print(sexy_sum([1,2,3]))
'''
from indeed import get_jobs as indeed_get_jobs
from so import get_jobs as so_get_jobs
from save import save_in_file, save_so_file

in_jobs = indeed_get_jobs()
so_jobs = so_get_jobs()

save_in_file(in_jobs)
save_so_file(so_jobs)