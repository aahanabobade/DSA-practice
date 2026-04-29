-- Product Sales Analysis I
-- Difficulty: Easy
-- Runtime: 1439 ms
-- Memory: 0B
-- https://leetcode.com/problems/product-sales-analysis-i/

# Write your MySQL query statement below
select p.product_name , s.year , s.price 
from Sales s
left join Product p
on p.product_id = s.product_id 
