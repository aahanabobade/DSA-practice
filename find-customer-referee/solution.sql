-- Q4. Find Customer Referee
-- Difficulty: Easy
-- Runtime: 460 ms
-- Memory: 0B
-- https://leetcode.com/problems/find-customer-referee/

# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
