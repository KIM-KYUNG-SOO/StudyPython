# 연산자 - 사칙연산
a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 정수형
print(a % b) # 나머지

# 문자열 연산(+, * 만 있음)
stat1 = 'Hello'
stat2 = 'World'
print(stat1,stat2) # 같이 출력하는 개념
print(stat1 + stat2) # 두문자열을 더한 개념
print(stat1 + stat2)
# print(stat1 - stat2) , 문자열 빼기는 안됨
print(stat1 * 5)
# print(stat1 * stat2), 문자열끼리 곱하기는 안됨
# print(stat1 / 5), 문자열 나누기 안됨

# 문자열 길이
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스(순번), 리스트와 동일한 작업
# print(stat3[0])
# print(stat3[1])
# print(stat3[2])
# print(stat3[3])
# print(stat3[4]) # 순번은 0번 부터 시작한다(중요!!!!)
# print(stat3[5]), string index out of range

#stat3[0] = '저'
#stat3[1] = '리'
#print(stat3)

print(stat3[-1]) #역순으로 돌아옴(-1부터 시작)
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

#문자열 자르기
일시 = '2022-01-17 14:39:25'
print(일시[:4],'년') # 0~3까지 출력
print(일시[5:7],'월') # [start_index:last_index-1]
print(일시[8:10],'일')
print(일시[11:13],'시')
print(일시[14:16],'분')
print(일시[17:],'초') # 처음과 마지막은 생략가능!

print(일시[-5:-3],'분')
print(일시[-5:],'분')

list_a = [1,2,3,4,5]
list_a[1] = 19
print(list_a) # 문자열은 불가

print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)

# 문자열 포맷팅(중요!!)
str1 = "I'm so happy {0} U".format('to')
print(str1)

첫번째 = '투'
두번째 = '유'
str2 = "I'm so happy {0} U. are {1}?".format(첫번째,두번째)
print(str2)

str3 = f"I'm so happy {첫번째} U. are {두번째}?"
print(str3)

# 숫자 천단위 콤마
money = 10000000000000
print(format(money, ',d'))

from datetime import datetime

now = datetime.now() #현재일시 생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math
mypi = math.pi
print(mypi)

print('{0}'.format(mypi))
print('{0:0.3f}'.format(mypi)) # f -> floating:실수형
print(f'{mypi:0.6f}')

full_name = 'Hugo MG Sung'
age = 47
greeting = f'''안녕하세요. 저는 {full_name}입니다. 
나이는 {age:0.1f}살 이구요.'''
print(greeting)

part_name = full_name.split() # 기본값은 스페이스바
print(part_name)
print(type(part_name)) # 자료형은 리스트

test = 'Hey, guys'
print(test.split(','))

# |
code = 'Test|2022|01|17|F45678'
split_codes = code.split('|')
print(split_codes)

# 단어교체 replace
print(full_name.replace('Hugo MG', 'Ashley'))

# strip == Oracle TRIM과 동일
aaa = '    Hello, world      '
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())

# index
print(full_name.index('H')) # 0
print(full_name.index('u')) # 1 먼저나오는 걸 읽는다.
print(full_name.index('g')) # 2
print(full_name.index('G')) # 6
#print(full_name.index('x')) # substring not found

# find
print(full_name.find('G')) # 6
print(full_name.find('MG')) # 5, 단어찾기도 가능 5는 M의 index
print(full_name.find('x')) # -1은 해당문장에 찾는 문자가 없는경우