# 커세이 접근하는 코드를 함수로 작성
from sqlite3 import connect
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 오라클 주소
    conn = ora.connect(user = 'scott', password='tiger', dsn=dsn, encoding='utf-8') # 오라클 접속
    return conn

def getAllData(conn): # conn객체를 매개변수 받아서 쿼리를 실행할 함수
    cur = conn.cursor()
    query = 'SELECT * FROM emp' # emp 테이블에서 데이터를 모두 가져와라
    for row in cur.execute(query): # emp 테이블의 최상단에 커서가 위치하면서 모든데이터를
        print(row) # 한줄씩 출력
    return

def getNameAndJobData(conn):
    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp' # emp 테이블 ename, job만 가져와라
    cur.execute(query) # 실행
    while True:
        row = cur.fetchone() # 한 row(레코드) 읽기
        if row is None:
            break
        else:
            print(row)

# def getDeptName(conn, no, loc):
def getDeptName(conn, tup):

    cur = conn.cursor()
    # query = f'SELECT * FROM dept WHERE deptno = {tup[0]} AND loc = \'{tup[1]}\''
    # loc는 var2 타입이니 홑따움표를 넣어야함!
    query = 'SELECT * FROM dept WHERE deptno = :1 AND loc = :2' 
    # :는 문법... 여기서 1은 oracle db index 1에서 가져옴
    cur.execute(query, tup)
    row = cur.fetchone()
    print(row)

if __name__ == '__main__': # 언더바 2개씩, 프로그램의 시작위치
    print('프로그램 시작')
    # 함수호출
    scott_conn = myconn() # dsn, connect() 후 접속객체 conn 리턴
    
    # print('emp 테이블 전체 조회(select *)')
    # getAllData(scott_conn)
    # print('emp 2개 컬럼 조회')
    # getNameAndJobData(scott_conn)

    no = input('1. 부서번호를 입력하세요:')
    loc = input('2. 지역명을 입력하세요:').upper()
    tup = (no,loc)
    print(f'부서번호: {no}, 지역: {loc}')
    getDeptName(scott_conn, tup)
    print('프로그램 종료')