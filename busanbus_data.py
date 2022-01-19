# 부산버스 노선별 이용 건수
import csv

file_name = '부산버스정보.csv'

f = open('부산버스정보.csv', mode = 'r', encoding='utf-8')
reader = csv.reader(f, delimiter=',') # delimiter -> 구분자
next(reader) # 헤더를 없애는 역할-> csv파일 첫째줄은 읽지 않는다.

for line in reader:
    print(line) # 한줄이 리스트로 변환되어 나옴

f.close()