with cte as 
(select 
e.*
from employees e 
join employees m
on e.employee_id = m.employee_id 
where e.salary < 30000 )

select employee_id 
from cte where manager_id not in (select distinct employee_id from employees)
