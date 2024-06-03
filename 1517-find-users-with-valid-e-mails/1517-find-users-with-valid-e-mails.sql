# Write your MySQL query statement below
select * from users
where mail regexp '^[A-Za-z][a-z0-9A-Z_.-]*@leetcode[.]com$' 