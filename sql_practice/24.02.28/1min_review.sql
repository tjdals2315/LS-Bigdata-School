--P102
SELECT *
    FROM EMP
  WHERE SAL >= 2500
   AND JOB = 'ANALYST';

--P135
SELECT SUBSTR(ENAME, 3)
    FROM EMP;