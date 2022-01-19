# 무한루프
val = 0

print('회원정보 프로그램')
while True:
    print('''작업할 번호를 입력하세요.
    1. 회원입력
    2. 회원검색
    3. 회원수정
    4. 회원삭제
    5. 종료
    숫자입력 : ''', end='')
    val = int(input()) # 입력

    if val == 1:
        print('회원정보 입력합니다.')
    elif val == 2:
        print('회원검색 화면으로 전환')
    elif val == 3:
        print('회원수정 화면으로 전환')
    elif val == 4:
        print('회원삭제 화면으로 전환')
    elif val == 5:
        break
    else:
        print('1~5사이의 수를 입력하세요.')
        continue
print('회원정보 프로그램 종료')

for b in list(range(1,6)):
    print(b*'*')

rows = 6
for b in range(1, rows + 1):
    print(''*(rows - b)+'*'*(2*b-1))
    
from errno import EILSEQ
from mailbox import ExternalClashError


hit = 0
while hit < 10:
    hit += 1
    print('*' * hit)
    if hit > 6:
        break

i = 0
while True:
    i += 1
    if i > 5:
         break
    print(" " * (5 - i), end="")
    print("*" * (2*i-1))

print()

i = 0
while True:
    i += 1
    if i > 5:
         break
    print(" " * (5 - i), end="")
    print("*" * i)
