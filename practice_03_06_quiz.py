#사이트별 비밀번호 작성 프로그램

#http://naver.com
#1.http://부분은 제외할 것 -> naver.com
#2. .이후를 제외할 것 -> naver
#3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성할 것

url = "http://youtube.com"

my_str = url.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))