-- Group Sold Products By The Date
-- Difficulty: Easy
-- Runtime: 641 ms
-- Memory: 0B
-- https://leetcode.com/problems/group-sold-products-by-the-date/

# Write your MySQL query statement below
SELECT 
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
