# Write your MySQL query statement below
select customer_id
from customer 
group by customer_id
having count(distinct product_key) = (SELECT count(distinct product_key) 
    FROM product)
