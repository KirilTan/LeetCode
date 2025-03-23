/*SELECT e1.name        AS "Manager Name"
     , COUNT(e2.name) AS Subordinates
FROM employee e1
         JOIN
     employee e2
     ON e1.id = e2.managerid
GROUP BY DISTINCT (e1.name)
HAVING COUNT(e2.name) >= 5;*/

SELECT e1.name AS name
FROM employee e1
         JOIN employee e2 ON e1.id = e2.managerId
GROUP BY DISTINCT (e1.id, e1.name)
HAVING COUNT(*) >= 5;
