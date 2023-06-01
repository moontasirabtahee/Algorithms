--Table: Courses
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| student     | varchar |
--| class       | varchar |
--+-------------+---------+
--(student, class) is the primary key column for this table.
--Each row of this table indicates the name of a student and the class in which they are enrolled.

SELECT class from Courses
group by class
having count(distinct student) >= 5