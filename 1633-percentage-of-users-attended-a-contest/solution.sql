-- Percentage of Users Attended a Contest
-- Difficulty: Easy
-- Runtime: 1194 ms
-- Memory: 0B
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/

# Write your MySQL query statement below
SELECT 
    r.contest_id,
    ROUND(COUNT(r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;
