# Write your MySQL query statement below
with cte as
(select e.id, e.name, e.salary, d.name as dname
from employee e
left join department d 
on e.departmentid = d.id)

select Department , Employee, Salary
from (
select dname as Department, 
name as Employee , max(salary) over(partition by dname, name) as Salary,
dense_rank() over(partition by dname order by salary desc) as rn
from cte 
) as t
where rn<=3

