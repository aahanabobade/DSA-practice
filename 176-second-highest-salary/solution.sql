-- Second Highest Salary
-- Difficulty: Medium
-- Runtime: 257 ms
-- Memory: 0B
-- https://leetcode.com/problems/second-highest-salary/

# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
