-- Managers with at Least 5 Direct Reports
-- Difficulty: Medium
-- Runtime: 466 ms
-- Memory: 0B
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

SELECT 
    e.name
FROM 
    Employee e
JOIN 
    Employee e2 ON e.id = e2.managerId
GROUP BY 
    e.id, e.name
HAVING 
    COUNT(e2.id) >= 5;
