--Table: Employee
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| id          | int     |
--| name        | varchar |
--| department  | varchar |
--| managerId   | int     |
--+-------------+---------+
--id is the primary key column for this table.
--Each row of this table indicates the name of an employee, their department, and the id of their manager.
--If managerId is null, then the employee does not have a manager.
--No employee will be the manager of themself.

Select Name from Employee where id in (
    Select managerId from Employee group by managerId having count(*) >= 5
)