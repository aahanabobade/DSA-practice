-- Q2. Customers Who Bought All Products
-- Difficulty: Medium
-- Runtime: 581 ms
-- Memory: 0B
-- https://leetcode.com/problems/customers-who-bought-all-products/

# Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*) FROM Product
);
