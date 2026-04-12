-- Q1. Combine Two Tables
-- Difficulty: Easy
-- Runtime: 413 ms
-- Memory: 0B
-- https://leetcode.com/problems/combine-two-tables/

# Write your MySQL query statement below
select p.firstName, p.lastName,a.city,a.state
from Person p
LEFT JOIN Address a
on p.personId = a.personId

