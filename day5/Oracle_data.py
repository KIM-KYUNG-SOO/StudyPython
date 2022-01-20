# Oracle_data
# cx_oracle 설치 : pip install cx_oracle
import cx_Oracle as ora

# 내 컴퓨터에 있는 DB에 접속시 localhost로 씀
# 회사에서는 DB컴퓨터나, 다른 공용컴퓨터... 주소 필요
# makedsn('호스트명 혹은 IP주소', 포트번호, service_name)
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 오라클 주소
# connect(user, password, dsn, encoding)
conn = ora.connect(user ='scott', password = 'tiger', dsn = dsn, encoding = 'utf-8') # 오라클 접속
cur = conn.cursor() # 실행결과를 담을 메모리 객체, 커서
try:
    # for row in cur.execute('SELECt * FROM emp'):
    #     print(row)
    # 데이터 한행만 가져올때
    cur.execute('SELECT COUNT(*) FROM emp')
    result = cur.fetchone()
    print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 13번라인 확인요 : {e}')
finally:
    cur.close() # 커서 닫고
    conn.close() # 접속 닫음