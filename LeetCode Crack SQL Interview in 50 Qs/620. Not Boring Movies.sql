--Table: Cinema
--
--+----------------+----------+
--| Column Name    | Type     |
--+----------------+----------+
--| id             | int      |
--| movie          | varchar  |
--| description    | varchar  |
--| rating         | float    |
--+----------------+----------+
--id is the primary key for this table.
--Each row contains information about the name of a movie, its genre, and its rating.
--rating is a 2 decimal places float in the range [0, 10]



Select * from Cinema
where id%2 != 0
and description != 'boring'
order by rating desc
