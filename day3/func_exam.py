# 함수 선언 및 사용
# 더하기 함수 선언
def add(a,b):
    res = a + b

    return res # 함수는 리턴이 중요!!

# 함수 사용
print(add(2455,895))

mid_val = add(3,4) # 선언한 쪽으로 점프
print(mid_val * 3)

# 함수종류
# 매개변수(입력값) 없는 형태
def say_hello(): # 매개변수 없이 함수 선언
    return 'Hello~'

print(say_hello())
print(say_hello(), 'my friend')

val = say_hello()
print(val.replace('o~',''))

# 결과값이 없는 형태
def say_hello(name):
    print(f'Hello~ {name}')  # 리턴없이 함수 선언
    #return None이 생략된 형태
say_hello('Kim')


# 둘다 없는 경우
def say_goodbye():
    print('by')

say_goodbye()

# 매개변수 지정
def multi(a,b):
    return a * b

print(multi(2,9))
print(multi(8,9))

# 매개변수 개수가 일정치 않은 경우
def plus(*args): # 개수가 일정치 않을때 *를 앞에 먼저 붙인다.
    res = 0
    for i in args:
        res += i

    return res

print(plus(1,2,3))
print(plus(1,2,3,4,5,6,7,8,9,10))


# 리턴값이 두개 이상
def mul_and_div(x,y):
    mul = x * y
    div = x / y

    return mul, div # 튜플

(res1, res2) = mul_and_div(7,8)
print(res1, res2)

def 사칙연산(x,y):
    return(x+y, x-y, x*y, x/y)

res1, res2, res3, res4 = 사칙연산(9,5)
print(res1,res2,res3,res4)
print(type(사칙연산(1,2))) # 함수형태가 turple임을 알 수 있다.