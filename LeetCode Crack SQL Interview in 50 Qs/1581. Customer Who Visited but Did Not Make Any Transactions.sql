--Table: Visits
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| visit_id    | int     |
--| customer_id | int     |
--+-------------+---------+
--visit_id is the primary key for this table.
--This table contains information about the customers who visited the mall.
--
--
--Table: Transactions
--
--+----------------+---------+
--| Column Name    | Type    |
--+----------------+---------+
--| transaction_id | int     |
--| visit_id       | int     |
--| amount         | int     |
--+----------------+---------+
--transaction_id is the primary key for this table.
--This table contains information about the transactions made during the visit_id.
--


Select customer_id, count(visit_id) as count_no_trans from Visits
where visit_id not in (select visit_id from Transactions) group by customer_id
order by customer_id