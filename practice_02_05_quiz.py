#퀴즈
# 월 4회 스터디 中 3회는 온라인 / 1회는 오프라인

# 조건 1 : 랜덤 날짜 뽑기
# 조건 2 : 월별 날짜는 최소 일수인 28 이내로
# 조건 3 : 매월 1~3일은 스터디 준비일이므로 제외

from random import *

date = randint(4,28)

print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")