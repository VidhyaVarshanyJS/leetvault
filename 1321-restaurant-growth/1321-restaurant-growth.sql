# Write your MySQL query statement below
with cte as
(select visited_on ,
        sum(amount) as amount
from customer
group by visited_on
)
select a.visited_on,
        sum(b.amount) as amount,
        round(avg(b.amount),2) as average_amount
from cte a, cte b
where datediff(a.visited_on, b.visited_on) between 0 and 6
group by a.visited_on
having count(*)>6