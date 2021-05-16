#자료구조_사전

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) #에러 발생
# print(cabinet.get(5)) #none이라고 쓰임 / 기본값 원할시 , 사용가능 이라고 추가하면 됨
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) #값이 있으면 True / 없으면 False
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#손님 퇴장
del cabinet["A-3"]
print(cabinet)

#사용중만 출력
print(cabinet.keys())

#사용 인원 출력
print(cabinet.values())

#사용 정보 전체 출력
print(cabinet.items())

#모든 키  반납
cabinet.clear()
print(cabinet)