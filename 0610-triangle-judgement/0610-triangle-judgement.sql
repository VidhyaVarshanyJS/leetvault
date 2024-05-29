# Write your MySQL query statement below
select *,
case when abs(x)+abs(y) > abs(z) then 'Yes' else 'No' end as triangle
from triangle