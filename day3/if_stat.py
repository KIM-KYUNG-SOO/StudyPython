# if 구문 - 흐름제어
# name = '경수'
name = ['경수', '태경', '기영', '광조', '다원']
# name을 list, turple로도 구성이 가능하다.

#if name == '경수' or '태경':  # :if 구문의 범위를 나타냄
if '태경' in name:
    print('의사를 만나러 갑니다.')
    print('인사를 합니다.')
elif name == '다원': # 다윈은 절대 주사실로 갈 수 없다.
    print('주사실로 갑니다.')
else:
    print('호출할때까지 대기합니다.')
