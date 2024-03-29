-- 8-1 문제
-- SQL-99 이전 방식
--WHERE절에
SELECT D.DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
  FROM EMP E, DEPT D
 WHERE E.DEPTNO = D.DEPTNO
   AND E.SAL > 2000;

--own.ver
SELECT D.DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
    FROM DEPT D, EMP E
   WHERE D.DEPTNO = E.DEPTNO
     AND E.SAL > 2000
ORDER BY D.DEPTNO, E.EMPNO;

-- SQL-99방식
--NATURAL JOIN
SELECT DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
  FROM EMP E NATURAL JOIN DEPT D
 WHERE E.SAL > 2000;

--own.ver
SELECT DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
    FROM DEPT D NATURAL JOIN EMP E
   WHERE E.SAL > 2000
ORDER BY DEPTNO, E.EMPNO;

--JOIN ~ USING
SELECT DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
  FROM EMP E JOIN DEPT D USING(DEPTNO)
 WHERE E.SAL > 2000
 ORDER BY DEPTNO;

--own.ver
SELECT DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
    FROM DEPT D JOIN EMP E USING (DEPTNO)
   WHERE E.SAL > 2000
ORDER BY DEPTNO, E.EMPNO;

--JOIN ~ ON
SELECT D.DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
    FROM DEPT D JOIN EMP E ON (D.DEPTNO = E.DEPTNO)
   WHERE E.SAL > 2000
   ORDER BY D.DEPTNO;
--own.ver
SELECT D.DEPTNO, D.DNAME, E.EMPNO, E.ENAME, E.SAL
    FROM DEPT D JOIN EMP E ON (D.DEPTNO = E.DEPTNO)
   WHERE E.SAL > 2000
ORDER BY D.DEPTNO, E.EMPNO;
