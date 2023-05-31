--+----------------+---------+
--| Column Name    | Type    |
--+----------------+---------+
--| tweet_id       | int     |
--| content        | varchar |
--+----------------+---------+
--tweet_id is the primary key for this table.
--This table contains all the tweets in a social media app.


SELECT tweet_id from Tweets
where length(content) > 15
