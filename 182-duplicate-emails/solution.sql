-- Duplicate Emails
-- Difficulty: Easy
-- Runtime: 393 ms
-- Memory: 0B
-- https://leetcode.com/problems/duplicate-emails/

# Write your MySQL query statement below
select email
from Person
group by email
having count(email)>1

