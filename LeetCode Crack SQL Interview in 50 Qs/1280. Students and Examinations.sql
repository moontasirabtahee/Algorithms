--Table: Students
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| student_id    | int     |
--| student_name  | varchar |
--+---------------+---------+
--student_id is the primary key for this table.
--Each row of this table contains the ID and the name of one student in the school.
--
--
--Table: Subjects
--
--+--------------+---------+
--| Column Name  | Type    |
--+--------------+---------+
--| subject_name | varchar |
--+--------------+---------+
--subject_name is the primary key for this table.
--Each row of this table contains the name of one subject in the school.
--
--
--Table: Examinations
--
--+--------------+---------+
--| Column Name  | Type    |
--+--------------+---------+
--| student_id   | int     |
--| subject_name | varchar |
--+--------------+---------+
--There is no primary key for this table. It may contain duplicates.
--Each student from the Students table takes every course from the Subjects table.
--Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

Select s.student_id,s.student_name , sb.subject_name, count(e.subject_name) as attended_exams

from Students s join Subjects sb
left join Examinations e
on s.student_id = e.student_id and sb.subject_name = e.subject_name

group by s.student_id,s.student_name , sb.subject_name
order by s.student_id,s.student_name , sb.subject_name