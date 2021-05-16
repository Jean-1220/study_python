# #자료구조_퀴즈
# 파이썬 코딩대회 이벤트
# 추첨, 1명 치킨, 3명 커피쿠폰

# 조건1, 댓글 20명 작성, 아이디는 1~20
# 조건2, 무작위 추첨, 중복 불가
# 조건3, random 모듈의 shuffle과 sample 활용

# from random import *
# lst = [1,2,3,4,5,]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
users = range(1,21) #1부터 20까지 숫자 생성
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) 

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print(" -- 축하합니다 -- ")