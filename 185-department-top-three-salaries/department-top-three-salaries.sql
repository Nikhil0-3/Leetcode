# Write your MySQL query statement below
select d.name as department,e.name as employee,e.salary as salary from employee e join 
department d on e.departmentid = d.id where (select count(distinct a.salary) from employee a
where a.departmentid = e.departmentid and a.salary >= e.salary ) <= 3 order by d.name,e.salary desc;






