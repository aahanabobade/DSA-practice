-- Q1. Customer Placing the Largest Number of Orders
-- Difficulty: Easy
-- Runtime: 514 ms
-- Memory: 0B
-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

# Write your MySQL query statement below
select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1
