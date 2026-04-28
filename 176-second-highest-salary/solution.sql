-- Second Highest Salary
-- Difficulty: Medium
-- Runtime: 311 ms
-- Memory: 0B
-- https://leetcode.com/problems/second-highest-salary/

# Write your MySQL query statement below
select  MAX(salary) as SecondHighestSalary 
from Employee 
where salary < (select MAX(salary) from Employee)
