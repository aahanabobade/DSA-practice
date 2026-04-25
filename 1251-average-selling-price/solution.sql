-- Average Selling Price
-- Difficulty: Easy
-- Runtime: 797 ms
-- Memory: 0B
-- https://leetcode.com/problems/average-selling-price/

# Write your MySQL query statement below
SELECT 
    p.product_id,
    IFNULL(ROUND(SUM(u.units * p.price) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
