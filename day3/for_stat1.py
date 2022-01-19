# 기본 for문

from operator import length_hint


arr = list(range(1,100))

for i in arr:
   print(f'{i:2.1f}')

# 튜플 for문
arr2 = ('me', 'my', 'friend', 'jane')
print(f'{arr2}')

for item in arr2:
   print(f'{item:>10}') # 우측정렬

합계 for 문
numbers = list(range(1,11)) # 1~10까지
numbers = list(range(1,21,2)) # 1~20까지 홀수만 출력
res = 0
for item in numbers:
    res += item

print(f'{numbers[-1]}까지의 총 합은 {res}입니다')

홀수, 짝수 구분
numbers = list(range(1,21)) # 1~20까지

for item in numbers:
    if item % 2 != 0: 
    # if item % 2 != 0: -> 짝수
        print(f'{item}은 홀수')

numbers = list(range(1,21)) # 1~20까지

# 13이상이면 탈출 또는 계속
numbers = list(range(1,21)) # 1~20까지
for item in numbers:
    if item > 12:
        break # break는 제일 앞에 써주는 것이 좋다.
    # 두 if문의 순서를 바꿨을때 결과값이 다름
    if item % 2 != 0: 
     # if item % 2 != 0: -> 짝수
        print(f'{item}은 홀수')
    
numbers = list(range(1,21)) # 1~20까지
for item in numbers:
    if item == 13:
        continue # 13은 제외하고  출력
    if item % 2 != 0: 
     # if item % 2 != 0: -> 짝수
        print(f'{item}은 홀수')

# 구구단(이중 for문을 사용)
print('구구단 프로그램')
for i in range(2,10):
    print(f'{i}단 시작', end="     ")
print('') # 줄바꿈
for i in range(1,10): # 2~9
    for j in range(2,10): # 1~9
        print(f'{j} x {i} = {j*i:2d}', end="   ")
    print('')

# inline for문과 기존 for문의 비교
a = [1,2,3,4]
result = [i*3 for i in a]
print(result)

t =[]
for i in a:
    t.append(i*3)
print(t)