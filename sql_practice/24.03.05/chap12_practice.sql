-- 잊기 전에 한 번 더 정답

-- 12-1
CREATE TABLE EMP_HW(
    EMPNO   NUMBER(4),
    ENAME   VARCHAR2(10),
    JOB     VARCHAR2(9),
    MGR     NUMBER(4),
    HIREDATE DATE,
    SAL     NUMBER(7,2),
    COMM    NUMBER(7,2),
    DEPTNO  NUMBER(2)
);

DESC EMP_HW;

SELECT * FROM EMP_HW;

-- 12-2
ALTER TABLE EMP_HW
    ADD BIGO VARCHAR2(20);

DESC EMP_HW;

SELECT * FROM EMP_HW;

-- 12-3
ALTER TABLE EMP_HW
    MODIFY BIGO VARCHAR2(30);

DESC EMP_HW;

SELECT * FROM EMP_HW;

-- 12-4
ALTER TABLE EMP_HW
RENAME COLUMN BIGO TO REMARK; --COLUMN 작성해야함

DESC EMP_HW;
SELECT * FROM EMP_HW;

-- 12-5
INSERT INTO EMP_HW 
SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO, NULL 
  FROM EMP; 

-- 12-6
DROP TABLE EMP_HW;