# 입출력_quiz

# 매주 1회 작성 보고서
# 1주차부터 50주차까지의 보고서 파일 만드는 프로그램

for i in range(1, 51) :
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 :")