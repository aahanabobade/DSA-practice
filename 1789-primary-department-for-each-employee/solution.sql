-- Primary Department for Each Employee
-- Difficulty: Easy
-- Runtime: 621 ms
-- Memory: 0B
-- https://leetcode.com/problems/primary-department-for-each-employee/

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'

UNION

SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(*) = 1;
