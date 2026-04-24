-- Replace Employee ID With The Unique Identifier
-- Difficulty: Easy
-- Runtime: 1181 ms
-- Memory: 0B
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

SELECT 
    eu.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;
