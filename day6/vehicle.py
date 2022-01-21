# vehicle.py

class Car:

    __fuel = 'DISEL'
    deldate = 2018

    def __init__(self, number, manufacture, color) -> None:
        self.number = number
        self.manufacture = manufacture
        self.color = color

    def __str__(self) -> str:
        return f'제 차는 {self.deldate}년도에 만들어진 차량입니다.'

    def 연료확인(self):
        print(f'연료 {self.__fuel}')
    
    # private
    def 연료입력(self, fuel):
        self.__fuel = fuel

    def go(self):
        print(f'{self.color}가 앞으로 달린다')
    def back(self):
        print(f'{self.number} 뒤로 달린다')
    def left(self):
        print('왼쪽으로 달린다')
    def right(self):
        print('오른쪽으로 달린다')
    def stop(self):
        print('멈춘다')