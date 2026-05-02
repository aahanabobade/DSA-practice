-- Department Top Three Salaries
-- Difficulty: Hard
-- Runtime: 892 ms
-- Memory: 0B
-- https://leetcode.com/problems/department-top-three-salaries/

        salary,
        departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
        ) AS rnk
    FROM Employee
) e
JOIN Department d
ON d.id = e.departmentId
WHERE rnk <= 3;
