# Write your MySQL query statement below
# Write your MySQL query statement below

select *
from (values row('Low Salary', (select count(account_id) from Accounts where income < 20000)), 
             row('Average Salary', (select count(account_id) from Accounts where income >= 20000 and income <= 50000)), 
             row('High Salary', (select count(account_id) from Accounts where income > 50000))
     ) categories(category, accounts_count)
;