-- Employees Earning More Than Their Managers
-- Difficulty: Easy
-- Runtime: 344 ms
-- Memory: 0B
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2
on e1.managerId = e2.id
where e1.salary>e2.salary
