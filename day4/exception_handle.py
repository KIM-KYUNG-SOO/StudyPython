# 예외처리(가장 중요!!!)
# 예외가 발생할 것 같은 코드에만 예외처리를 한다!
def add(a,b):
    return a + b
    
def minus(a,b):
    return a - b

def multi(a,b):
    return a * b

def divide(a,b):
    return a / b

print('사칙연산 시작')
a, b = 4, 1 # break point, 빨간점
numbers = [3, 6, 9] # 리스트 생성
try:
    print(f'나누기 결과 : {divide(a, b)}')
    res = int(numbers[2]) * 8
    num = int(input('수를 입력하세요'))
# 오류명 대신 Exceptional을 써도 됨
# Exceptional > ZeroDivisionError, 상/하위 개념?
# 변수에 0을 넣는 순간 프로그램이 실행되지 않음
# 예외는 실행이후에 나오는 오류

except ZeroDivisionError as e:
    print(f'나누기 예외. 추가처리1 {e}')
except IndexError as e: 
    print(f'인덱스 예외. 추가처리2 {e}')
except ValueError as e: 
    print(f'숫자만 넣으세요. 추가처리4 {e}')
except Exception as e: 
    print(f'알수없는 예외. 추가처리5 {e}')
finally:
    print(f'곱하기 결과 : {multi(a, b)}')
    print(f'빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')

print('사칙연산 종료')

# 예외처리는 최소화하는 것이 좋다.