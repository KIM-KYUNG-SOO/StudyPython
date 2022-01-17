# 변수 - 파이썬의 변수에는 제약이 거의 없다.
a = '헬로우'
print(a)

a = 3.141592
print(a)

a = 10
print(a) 

a = 999999999999999999
print(a)

a = 1/10
print(a)

# 변수값을 지정(할당) - assign 방법
a = 3 # left value(숫자는 절대 안됨) = right value
b = 3.141592
c = 'python'
d = (1, 2, 3) # 튜플
e = [1, 2, 3, 4] # 리스트
f = [7 , '8', '$', a] # 파이썬의 장점!

# 변수명(숫자, 특수문자 안됨, 공백없이 지정)
# 변수명 지정 불가는 주석처리 함, 길이제약은 크게 없음
# 변수명은 지정할때 의미를 알수있게 지정하는 것이 좋음
val = 10
val2 = 20
val4 = 30
#4val = 40 # 안됨
#-val = 50 # 안됨
#*val = 60 # 안됨
val_of_change = 99
chain_reaction = 108
#chain reaction = 109 # 안됨
#val$ = 99 # 안됨
val_ = 999
Val_ = 9080
print(val_)
print(Val_)
은행계좌금액 = 1
myaccountofbank = 1

#내장함수 id(), type()
print(id(val_))
print(id(Val_))
print(type(val_))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


