-- Confirmation Rate
-- Difficulty: Medium
-- Runtime: 763 ms
-- Memory: 0B
-- https://leetcode.com/problems/confirmation-rate/

# Write your MySQL query statement below
SELECT 
    s.user_id,
    ROUND(
        IFNULL(SUM(c.action = 'confirmed') / COUNT(c.action), 0),
        2
    ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id;
