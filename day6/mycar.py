# mycar.py
from vehicle import Car # vehicle의 car만 쓰겠다.

if __name__ == '__main__':
    mycar = Car('8899','HYUNDAI','black')
    mycar.__fuel = 'gasolin'
    mycar.deldate = 2017

    mycar.go()
    mycar.back()
    print(mycar)
    mycar.연료입력('등유')
    mycar.연료확인()
   