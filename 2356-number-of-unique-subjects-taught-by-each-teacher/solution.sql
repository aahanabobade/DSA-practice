-- Number of Unique Subjects Taught by Each Teacher
-- Difficulty: Easy
-- Runtime: 501 ms
-- Memory: 0B
-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

SELECT 
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
