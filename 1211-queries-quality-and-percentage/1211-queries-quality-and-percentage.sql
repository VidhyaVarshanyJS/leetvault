# Write your MySQL query statement below
select 
query_name,
ifnull(round(sum(rating/ position)/count(*),2),0) as quality ,
round(avg(if(rating<3,1,0)) *100,2) as poor_query_percentage
from queries
group by query_name