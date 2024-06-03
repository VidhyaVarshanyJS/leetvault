# Write your MySQL query statement below
select Department, Employee, Salary 
from (select d.name as Department,
       e.name as Employee,
       e.salary as Salary,
       dense_rank() over(partition by d.name order by salary desc) as rn
from employee e join department d on e.departmentid = d.id
) t 
where rn<=3
