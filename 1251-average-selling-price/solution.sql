-- Average Selling Price
-- Difficulty: Easy
-- Runtime: 831 ms
-- Memory: 0B
-- https://leetcode.com/problems/average-selling-price/

SELECT 
    p.product_id,
    ROUND(
        COALESCE(SUM(u.units * p.price) / SUM(u.units), 0),
        2
    ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
# Write your MySQL query statement below
