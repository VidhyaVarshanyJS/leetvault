# Write your MySQL query statement below
select teacher_id, sum(rn) as cnt
from(
select teacher_id, subject_id,
row_number() over(partition by teacher_id, subject_id order by teacher_id) as rn
from teacher) as t
where t.rn = 1
group by teacher_id
