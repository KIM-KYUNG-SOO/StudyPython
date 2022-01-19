# 파일 입/출력

# 파일생성하기
# f = open('newfile.txt', 'w')
# f.close() # open 이후 close 반드시 하자.

# 특정경로에 파일생성하기
# f = open('C:/Sources/Sample/text2.txt', 'w') #/대신, \\로 사용도 가능함
# f.close()
# print('파일이 생성되었습니다.')

# newfile.txt 파일입력(읽어오기)
f = open('newfile.txt', 'r',encoding = 'utf-8')
# while True: # 무한루프
#     line = f.readline() # 한 줄씩 읽는다.
#     if not line:
#         break
#     print(line)

# f.close()

# for문으로 읽어오기
lines = f.readlines()
for line in lines:
    print(line)

f.close()