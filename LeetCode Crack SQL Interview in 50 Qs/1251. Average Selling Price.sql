--Table: Prices
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| product_id    | int     |
--| start_date    | date    |
--| end_date      | date    |
--| price         | int     |
--+---------------+---------+
--(product_id, start_date, end_date) is the primary key for
-- this table.
--Each row of this table indicates the price of the product_id
--in the period from start_date to end_date.
--For each product_id there will be no two overlapping
--periods. That means there will be no two intersecting
-- periods for the same product_id.
--
--
--Table: UnitsSold
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| product_id    | int     |
--| purchase_date | date    |
--| units         | int     |
--+---------------+---------+
--There is no primary key for this table, it may contain
--duplicates.
--Each row of this table indicates the date, units, and
--product_id of each product sold.

Select p.product_id , (round(sum(p.price*u.units)/sum(u.units),2)) as average_price from Prices p
join UnitsSold u
on p.product_id = u.product_id
where u.purchase_date between p.start_date and p.end_date
group by p.product_id
order by p.product_id
