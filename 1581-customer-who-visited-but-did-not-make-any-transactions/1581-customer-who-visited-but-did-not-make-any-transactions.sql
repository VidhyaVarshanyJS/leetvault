# Write your MySQL query statement below
select customer_id , count(customer_id) as count_no_trans
from visits 
where visit_id not in (
select t.visit_id 
from visits v 
join transactions as t
on v.visit_id = t.visit_id
)
group by customer_id

