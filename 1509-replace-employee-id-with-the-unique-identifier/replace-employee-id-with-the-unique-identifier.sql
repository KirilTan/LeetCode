-- Write your PostgreSQL query statement below
SELECT
    u.unique_id AS unique_id
    ,e.name AS name
FROM
    Employees AS e
LEFT JOIN
    EmployeeUNI AS u
ON e.id = u.id
