--able: Activity
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| user_id       | int     |
--| session_id    | int     |
--| activity_date | date    |
--| activity_type | enum    |
--+---------------+---------+
--There is no primary key for this table, it may have duplicate rows.
--The activity_type column is an ENUM of type ('open_session', 'end_session', 'scroll_down', 'send_message').
--The table shows the user activities for a social media website.
--Note that each session belongs to exactly one user.

SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users from Activity
WHERE activity_date between '2019-06-28' and '2019-07-27' group by activity_date
