#제어문_quiz
# cocoa 서비스 이용 택시 기사
# 50명 승객, 총 탑승 승객 수는?

# 조건1, 승객별 운행 소요 시간 5~50분 사이의 난수
# 조건2, 소요시간 5~15분 사이의 승객만 매칭

from random import *
cnt = 0
for i in range(1,51) :
    time = randrange(5, 51)
    if 5 <= time <= 15 : # 5분~15분 이내 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))
        cnt += 1
    else : 
        print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))
print("총 탑승 승객 : {0} 분" .format(cnt))