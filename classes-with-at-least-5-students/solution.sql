-- Q2. Classes With at Least 5 Students
-- Difficulty: Easy
-- Runtime: 368 ms
-- Memory: 0B
-- https://leetcode.com/problems/classes-with-at-least-5-students/

# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
