-- Classes With at Least 5 Students
-- Difficulty: Easy
-- Runtime: 304 ms
-- Memory: 0B
-- https://leetcode.com/problems/classes-with-at-least-5-students/

# Write your MySQL query statement below
select class
from Courses
group by class
having count(class)>=5
