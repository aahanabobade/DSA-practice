-- Count Salary Categories
-- Difficulty: Medium
-- Runtime: 1481 ms
-- Memory: 0B
-- https://leetcode.com/problems/count-salary-categories/

       COUNT(*)
FROM Accounts
WHERE income BETWEEN 20000 AND 50000

UNION ALL

SELECT 'High Salary',
       COUNT(*)
FROM Accounts
WHERE income > 50000;
