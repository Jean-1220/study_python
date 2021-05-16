#문자열 처리 _ 문자열 처리 함수
python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) #[]안에 있는 글자가 대문자인지 확인
print(len(python)) #문자 길이
print(python.replace("Python", "Java")) #앞 글자를 뒷 글자로 대체

index = python.index("n") #n이 어디 위치에 있는지
print(index)
index = python.index("n", index + 1) #두번째 n의 위치
print(index)

print(python.find("n"))
print(python.find("Java")) #해당 글자 없을시 -1을 반환
#print(python.index("Java")) #해당 글자 없을시 에러 남
print("hi")

print(python.count("n")) #n이 총 몇 번 등장하는지