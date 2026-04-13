-- Consecutive Numbers
-- Difficulty: Medium
-- Runtime: 1169 ms
-- Memory: 0B
-- https://leetcode.com/problems/consecutive-numbers/

# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1 AND num = prev2;
