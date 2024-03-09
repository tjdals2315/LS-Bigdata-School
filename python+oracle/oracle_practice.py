# 한 줄 실행 = shift + enter
import cx_Oracle as oci
# db connection
con = oci.connect("scott/tiger@localhost:1521/orcl")
# cursor
cur = con.cursor()
#
# fetchone = 결과를 하나씩 가져옴
# SQL
sql = "SELECT * FROM EMP"
cur.execute(sql)
#
while True:
    row = cur.fetchone()
    if row is None:
        break
    print(row)
#
# SQL
sql = "SELECT * FROM EMP"
cur.execute(sql)
#
row = cur.fetchone()
while row is not None:
    print(", ".join([str(col) for col in row]))
    row = cur.fetchone()
#
# SQL
sql = "SELECT EMPNO, ENAME FROM EMP"
cur.execute(sql)
row = cur.fetchone()
#
while row is not None:
    empno, ename = row
    print(empno, ename)
    row = cur.fetchone()
#
# SQL
sql = "SELECT EMPNO, ENAME FROM EMP"
cur.execute(sql)
#
while True:
    row = cur.fetchone()
    if row is None:
        break
    data1 = row[0]
    data2 = row[1]
    # s = 문자열, 5자리 문자열, 10자리 문자열
    print("%5s %10s" % (data1, data2))
#
# fetchall = 결과를 전부 가져옴
# SQL
sql = "SELECT * FROM EMP"
cur.execute(sql)
#
rows = cur.fetchall()
if rows:
    for row in rows:
        print(row)
#
# SQL
sql = "SELECT EMPNO, ENAME FROM EMP"
cur.execute(sql)
#
rows = cur.fetchall()
if rows:
    for row in rows:
        empno, ename = row
        print(empno, ename)
#
# SQL
sql = "SELECT EMPNO, ENAME FROM EMP"
cur.execute(sql)
#
rows = cur.fetchall()
if rows:
    for row in rows:
        data1 = row[0]
        data2 = row[1]
        # s = 문자열, 5자리 문자열, 10자리 문자열
        print("%5s %10s" % (data1, data2))
#
# SQL
sql = "SELECT * FROM EMP A, SALGRADE B WHERE A.SAL BETWEEN B.LOSAL AND B.HISAL"
cur.execute(sql)
#
rows = cur.fetchall()
if rows:
    for row in rows:
        print(row)
#
# fetchmany = 결과를 정한 개수만큼 가져옴
# SQL
sql = "SELECT * FROM EMP"
cur.execute(sql)
#
rows = cur.fetchmany(5)
# display rows
for row in rows:
    print(row)
#
# pip install pandas
import pandas as pd
query = 'SELECT * FROM EMP'
df = pd.read_sql_query(query,con)
print(df)
#
# create
# SQL
sql = "CREATE TABLE EXAM_ID (ID INT)"
cur.execute(sql)
#
print(cur.execute("SELECT * FROM EXAM_ID").fetchall())
#
# insert
while True:
    data1 = input("사용자 ID를 입력하세요> ")
    if data1 == "":
        break
    sql = "INSERT INTO EXAM_ID VALUES ('" + data1 + "')"
    # sql = "INSERT INTO EXAM_ID (ID) VALUES ('" + data1 + "')"
    cur.execute(sql)
#
# drop
# SQL
sql = "DROP TABLE EXAM_ID"
cur.execute(sql)
#
print(cur.execute('SELECT * FROM EXAM_ID').fetchall())
#

# 커밋
con.commit()

# 롤백
con.rollback()

# 디비 연결 종료
con.close()