# Write your MySQL query statement below
select 
    substr(trans_date,1,7) as month,
    country,
    count(id) as trans_count,
    sum(state='approved') as approved_count,
    sum(amount) as trans_total_amount,
    sum(if(state='approved',amount,0)) as approved_total_amount
from transactions
group by month, country
