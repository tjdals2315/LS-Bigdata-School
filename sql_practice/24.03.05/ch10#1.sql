--문제1
CREATE TABLE CHAP10HW_EMP AS SELECT * FROM EMP;
CREATE TABLE CHAP10HW_DEPT AS SELECT * FROM DEPT;
CREATE TABLE CHAP10HW_SALGRADE AS SELECT * FROM SALGRADE;
--열 지정 INSERT
SELECT * FROM CHAP10HW_DEPT;
INSERT INTO CHAP10HW_DEPT (DEPTNO, DNAME, LOC) VALUES (50, 'ORACLE', 'BUSAN');
INSERT INTO CHAP10HW_DEPT (DEPTNO, DNAME, LOC) VALUES (60, 'SQL', 'ILSAN');
INSERT INTO CHAP10HW_DEPT (DEPTNO, DNAME, LOC) VALUES (70, 'SELECT', 'INCHEON');
INSERT INTO CHAP10HW_DEPT (DEPTNO, DNAME, LOC) VALUES (80, 'DML', 'BUNDANG');
SELECT * FROM CHAP10HW_DEPT;
ROLLBACK;
--열 생략 INSERT = 모든 열에 INSERT 할 때는 생략 가능
--열 지정 생략 INSERT
SELECT * FROM CHAP10HW_DEPT;
INSERT INTO CHAP10HW_DEPT VALUES (50, 'ORACLE', 'BUSAN');
INSERT INTO CHAP10HW_DEPT VALUES (60, 'SQL', 'ILSAN');
INSERT INTO CHAP10HW_DEPT VALUES (70, 'SELECT', 'INCHEON');
INSERT INTO CHAP10HW_DEPT VALUES (80, 'DML', 'BUNDANG');
SELECT * FROM CHAP10HW_DEPT;
--다중 INSERT
ROLLBACK;
SELECT * FROM CHAP10HW_DEPT;
--열 지정 INSERT
INSERT ALL
 INTO CHAP10HW_DEPT(DEPTNO, DNAME, LOC) VALUES(50,'ORACLE','BUSAN')
 INTO CHAP10HW_DEPT(DEPTNO, DNAME, LOC) VALUES(60,'SQL','ILSAN')
 INTO CHAP10HW_DEPT(DEPTNO, DNAME, LOC) VALUES(70,'SELECT','INCHEON')
 INTO CHAP10HW_DEPT(DEPTNO, DNAME, LOC) VALUES(80,'DML','BUNDANG')
SELECT * FROM DUALSELECT * FROM CHAP10HW_DEPT;
ROLLBACK;
--열 지정 생략 INSERT
INSERT ALL
 INTO CHAP10HW_DEPT VALUES (50, 'ORACLE', 'BUSAN')
 INTO CHAP10HW_DEPT VALUES (60, 'SQL', 'ILSAN')
 INTO CHAP10HW_DEPT VALUES (70, 'SELECT', 'INCHEON')
 INTO CHAP10HW_DEPT VALUES (80, 'DML', 'BUNDANG')
 SELECT * FROM DUAL;
SELECT * FROM CHAP10HW_DEPT;