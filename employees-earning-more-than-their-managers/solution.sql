-- Q2. Employees Earning More Than Their Managers
-- Difficulty: Easy
-- Runtime: 358 ms
-- Memory: 0B
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below
select e.name as Employee 
from Employee e
join Employee m
on e.managerId = m.id
where e.salary>m.salary
