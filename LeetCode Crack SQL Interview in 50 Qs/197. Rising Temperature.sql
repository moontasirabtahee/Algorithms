--Table: Weather
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| id            | int     |
--| recordDate    | date    |
--| temperature   | int     |
--+---------------+---------+
--id is the primary key for this table.
--This table contains information about the temperature on a certain day.

SELECT w1.id from Weather w1 , Weather w2
where datediff(w1.recordDate , w2.recordDate) = 1 and w1.temperature > w2.temperature