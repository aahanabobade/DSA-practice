-- Fix Names in a Table
-- Difficulty: Easy
-- Runtime: 671 ms
-- Memory: 0B
-- https://leetcode.com/problems/fix-names-in-a-table/

# Write your MySQL query statement below
SELECT 
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM Users
ORDER BY user_id;
