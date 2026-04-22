-- Find Customer Referee
-- Difficulty: Easy
-- Runtime: 591 ms
-- Memory: 0B
-- https://leetcode.com/problems/find-customer-referee/

# Write your MySQL query statement below
select name
from Customer
where referee_id !=2 or referee_id is null
