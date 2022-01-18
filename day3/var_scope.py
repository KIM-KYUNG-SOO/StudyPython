# 변수 라이프스코프
a = 10 # 전역변수

def vartest(a):
    a = a + 1
    return a
    # 함수안에있는 a는 매개변수이면서, 지역변수
    # a를 x로 바꾸면 이해하기 쉽다.

a = vartest(a)
print(a)

# 객체지향, 클래스
# person
class person:
    pass
p = person()
print(type(p))