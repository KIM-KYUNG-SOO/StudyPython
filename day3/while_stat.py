# while 문
# while은 사용자가 직접 증감시켜줘야함, for는 자동으로 증감시켜줌
hit = 0

while hit < 100: # 이값이 참인 동안
    hit += 1 # hit = hit + 1
    if hit > 10:
        break
    print(f'나무를 {hit}번 찍습니다.')

for hit in range(1,100):
    if hit > 10:
        break
    print(f'나무를 {hit}번 찍습니다.')