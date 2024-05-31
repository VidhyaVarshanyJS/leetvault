# Write your MySQL query statement below
select person_name 
from (
select *, 
        sum(weight) over(order by turn) as cum_sum,
        row_number() over(order by turn) as rn
from queue
) as t
where cum_sum<=1000 
order by t.rn desc
limit 1


