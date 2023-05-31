--1934. Confirmation Rate
--Table: Signups
--
--+----------------+----------+
--| Column Name    | Type     |
--+----------------+----------+
--| user_id        | int      |
--| time_stamp     | datetime |
--+----------------+----------+
--user_id is the primary key for this table.
--Each row contains information about the signup time for the user with
--ID user_id.
--
--
--Table: Confirmations
--
--+----------------+----------+
--| Column Name    | Type     |
--+----------------+----------+
--| user_id        | int      |
--| time_stamp     | datetime |
--| action         | ENUM     |
--+----------------+----------+
--(user_id, time_stamp) is the primary key for this table.
--user_id is a foreign key with a reference to the Signups table.
--action is an ENUM of the type ('confirmed', 'timeout')
--Each row of this table indicates that the user with ID user_id
-- requested a confirmation message at time_stamp and that confirmation
-- message was either confirmed ('confirmed')
--or expired without confirming ('timeout').


Select s.user_id , round(
avg(
case when c.action = 'confirmed' then 1 else 0 end
)
,2) as confirmation_rate from
Signups s left join Confirmations c
on s.user_id = c.user_id
group by s.user_id
order by s.user_id

