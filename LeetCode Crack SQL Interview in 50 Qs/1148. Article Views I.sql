--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| article_id    | int     |
--| author_id     | int     |
--| viewer_id     | int     |
--| view_date     | date    |
--+---------------+---------+
--There is no primary key for this table, it may have duplicate rows.
--Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
--Note that equal author_id and viewer_id indicate the same person.

SELECT distinct author_id as id from Views
where author_id = viewer_id order by author_id