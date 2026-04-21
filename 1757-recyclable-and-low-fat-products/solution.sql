-- Recyclable and Low Fat Products
-- Difficulty: Easy
-- Runtime: 527 ms
-- Memory: 0B
-- https://leetcode.com/problems/recyclable-and-low-fat-products/

# Write your MySQL query statement below
SELECT product_id  
from Products 
where low_fats ='Y' and recyclable ='Y'
