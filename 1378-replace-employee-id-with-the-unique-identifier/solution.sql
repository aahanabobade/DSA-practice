-- Replace Employee ID With The Unique Identifier
-- Difficulty: Easy
-- Runtime: 1403 ms
-- Memory: 0B
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/


select eu.unique_id , e.name
from Employees e
left join EmployeeUNI eu
on e.id = eu.id
