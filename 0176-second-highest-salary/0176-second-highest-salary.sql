# Write your MySQL query statement below
select max(salary) as SecondHighestSalary 
from (
    select *, dense_rank() over(order by salary desc) as rn
    from employee
) as t
where rn =2
       