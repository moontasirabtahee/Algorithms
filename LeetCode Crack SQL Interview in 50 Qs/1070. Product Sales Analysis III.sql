--Table: Sales
--
--+-------------+-------+
--| Column Name | Type  |
--+-------------+-------+
--| sale_id     | int   |
--| product_id  | int   |
--| year        | int   |
--| quantity    | int   |
--| price       | int   |
--+-------------+-------+
--(sale_id, year) is the primary key of this table.
--product_id is a foreign key to Product table.
--Each row of this table shows a sale on the product product_id in a certain year.
--Note that the price is per unit.


Select product_id, year,quantity, price from Sales
where (product_id, year) in (select product_id, min(year) from Sales group by product_id)
order by product_id, year