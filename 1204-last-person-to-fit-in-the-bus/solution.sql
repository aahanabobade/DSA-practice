-- Last Person to Fit in the Bus
-- Difficulty: Medium
-- Runtime: 1768 ms
-- Memory: 0B
-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/

# Write your MySQL query statement below
SELECT person_name
FROM Queue q1
WHERE (
    SELECT SUM(weight)
    FROM Queue q2
    WHERE q2.turn <= q1.turn
) <= 1000
ORDER BY q1.turn DESC
LIMIT 1;
