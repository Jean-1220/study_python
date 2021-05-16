#제어문_한줄for

#출석번호 1~4, 앞에 100을 붙이기로 변경
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

#학생들 이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [len(i) for i in student]
print(student)

#학생 이름을 대문자로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student]
print(student)