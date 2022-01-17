# 리스트 연산
arr = list(range(5))
print(arr)

arr = list(range(1,6))
print(arr)

arr = list(range(2,101,2)) # (시작숫자,원하는끝숫자+1. 증감량)
print(arr)
print(arr[0]+arr[5]) # 연산도 가능하다.

# 2차원 배열(리스트)
arr2 = [1,2,['Hi','My','Friend']]
print(arr2[0])
print(arr2[2])
print(arr2[2][1])
print(arr2[2][1][0]) # MY에서 인덱스0-> M

arr3 = list(range(1,4))
print(arr3)
print(arr3 * 3)
print(arr3 + arr)
print(len(arr3))

# 리스트 함수
print('--리스트 내장함수')
del(arr3[1]) # del은 index값으로 지움
print(arr3)

arr3.remove(1)
print(arr3) # remove는 데이터 값으로 지움

# 리스트 삭제
arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3) # 중복된값이 있으면 하나만 지움
print(arr4)
del(arr4[8])
print(arr4)

arr4.sort()
print(arr4) # 오름차순

arr4.reverse()
print(arr4) # 내림차순

arr4.insert(2,10) # index 2번 자리에서 10을 추가
print(arr4)

# 튜플
tup1 = tuple(range(1,6))
print(tup1)
print(tup1[0])

#tup1[0] = 99
#print(tup1) # tuple은 처음 값이 정해지면 이후 수정안됨

# 딕셔너리 {key:value}
dic1 = {1:'a'}
dic1[2] = 'b'
print(dic1)

dic1['name'] = 'Hugo'
print(dic1) # 문자열, 숫자 상관없이 추가가능

del dic1['name']
print(dic1)

print(dic1.keys())
print(dic1.values())
print(dic1.items())

# 리스트를 위한 튜플 변환
print('-- 리스트/튜플 변환')
print(arr4) # 리스트
tup2 = tuple(arr4) # 튜플로 변환, 이렇게 하면 튜플도 변환이 가능하다.
print(tup2) # 튜플

print(tup1)
arr5 = list(tup1)
arr5.append(6) #append 열 마지막에 추가
print(arr5)
tup1 = tuple(arr5)
print(tup1)