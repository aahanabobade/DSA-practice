-- Q1. Students and Examinations
-- Difficulty: Easy
-- Runtime: 925 ms
-- Memory: 0B
-- https://leetcode.com/problems/students-and-examinations/

FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
    ON s.student_id = e.student_id 
    AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
