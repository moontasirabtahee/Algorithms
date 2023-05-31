--Table: Transactions
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| id            | int     |
--| country       | varchar |
--| state         | enum    |
--| amount        | int     |
--| trans_date    | date    |
--+---------------+---------+
--id is the primary key of this table.
--The table has information about incoming transactions.
--The state column is an enum of type ["approved", "declined"].

SELECT date_format(trans_date,"%Y-%m") as month,
country,

count(id) as trans_count
count(
if(state = 'approved',id,null)
)as approved_count
sum(
case when state = 'approved' then amount
else amount end
)
as trans_total_amount
sum(
case when state = 'approved' then amount
else 0 end
)
as approved_total_amount

from Transactions
group by month,country
order by month,country
