--Q1 S로 끝나는 사원 데이터
-- SELECT EMP WHERE ENAME LIKE 'S%';
SELECT * FROM EMP WHERE ENAME LIKE '%S'; --S로 끝나는 모든 이름

--Q2 30번 부서에서 근무하는 사람 중에 직책 'SALESMAN'
-- SELECT0 * FROM EMP WHERE DEPTNO = 30 AND JOB = 'SALESMAN';;
SELECT EMPNO, ENAME, JOB, SAL, DEPTNO 
    FROM EMP 
   WHERE  DEPTNO = 30 AND JOB = 'SALESMAN';
--Q3
-- SELECT * FROM EMP WHERE SAL > 2000;
-- SELECT * FROM EMP IS SAL > 2000;
-- 집합연산자 사용하지 않는 방식
SELECT EMPNO, ENAME, JOB, SAL, DEPTNO
    FROM EMP WHERE DEPTNO IN (20,30) AND SAL > 2000;

--집합연산자 사용하는 방식
SELECT EMPNO, ENAME, JOB, SAL, DEPTNO
    FROM EMP WHERE DEPTNO = 20 AND SAL > 2000
UNION
SELECT EMPNO, ENAME, JOB, SAL, DEPTNO
    FROM EMP WHERE DEPTNO = 30 AND SAL > 2000;

--Q4
SELECT * FROM EMP WHERE SAL IN (2000, 3000);

--Q5
SELECT ENAME, EMPNO, SAL, DEPTINO 
    WHERE ENAME LIKE '%S$'AND SAL NOT IN (1000, 2000);

--Q6
SELECT * FROM EMP
    WHERE COMM IS NULL
   AND MGR IS NOT NULL
   AND JOB IN ('MANAGER', 'CLERK')
   AND ENAME NOT LIKE '_L%';