# Write your MySQL query statement below
select user_id, count(if(follower_id,1,0)) as followers_count
from followers
group by user_id