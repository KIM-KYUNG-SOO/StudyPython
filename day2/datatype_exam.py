# 자료형
print(None)
print(type(None))

print(0 == None)
a = None
print(a)
print(type(a))

# 숫자형
금액 = 12_345_666 # 1000단위 구분 기호 , 대신 _로 대체 가능함
print(금액)

# 문자열형
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)

bruce_eckel = 'Life is short. \nYou need Python' #\n 줄바꿈 
print(bruce_eckel)

bruce_eckel = '''Life is short. 
You need Python'
난 필요없는데... 파이썬''' #'''로도 줄바꿈이 가능함
print(bruce_eckel)

#불형
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 999)
#print(val_sum = 10)

# 불 타입도 할당이 가능하다 단 T, F로 가능
bl_true = True
print(bl_true)
print(type(bl_true))
print(bl_true == True) # True
print(bl_true is True) # True

print(a is None) # True
print(val_sum is 1000) # True

# 의미가 있는 bool
print(bool(1)) # True
print(bool(0)) # False

# list
b = [1,2,3,4,5,6,7,8,9,10]
print(b)

b = [ i for i in range(50)]
print(b)

arr2 = ['Life','is','short', 'U','need','Python'] #(), {} []
print(arr2)

arr3 = [[1,2,3],[4,5,6]]
print(arr3) # 2x3 matrix

# 빈 리스트 새성
arr4 = list()
print(arr4) # None과 다르다

# 튜플
tuple1 = (1,2,3,4,5)
print(tuple1)

# 딕셔너리
spiderman = {'name' : '피터파커', 'age' : 18, 
             'weapon' : '웹슈터'}
print(spiderman)

# 집합. # 중복을 허용하지 않음
set_int = set([1,2,3,4,5,4,6,7,1,2,2])
print(set_int)

