# Write your MySQL query statement below

SELECT (SELECT name FROM Department d WHERE d.id = e.departmentId) AS Department,e.name AS Employee,e.salary AS Salary FROM Employee e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);


