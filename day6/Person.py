# Person.py
# Person Class
from codecs import getencoder
from os import name

class Person: # 사람이라는 클래스 생성
    # pass # 뭘 넣어야할지 모를때 쓴다.
    # 사람의 특성을 나타내는 건 명사, 행위는 동사 -> 변수와, 함수로 작성됨

    # 생성자, 매직메소드
    def __init__(self, name, age, gender) -> None: 
        # __init__메서드에선 속성을 self.변수로 할당한다.
        self.name = name # 결국은 Person().name이라고 할 수 있다.
        self.age = age
        self.gender = gender
        print('Person이 생성되었습니다.')

    def eating(self, food) -> None: # 리턴 값이 None, 이렇게도 표현이 가능하다.
        print(f'{self.name}가 {food}을(를) 먹는다.')
    def working(self, drink):
        print(f'{self.name}가 {drink}을(를) 마시면서 일한다.')
    def introduce(self):
        greeting = f'''안녕하세요. 저는 {self.name}입니다.
        {self.age}살이고요, {self.gender}입니다.'''
        print(greeting)

if __name__ == '__main__':
    kks = Person('김경수', 33, '남자') # __init__(self,name,age) == Person()

    kks.introduce()
    kks.eating('bonjook')
    kks.working('hotsix')

    str

