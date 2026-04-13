-- Nth Highest Salary
-- Difficulty: Medium
-- Runtime: 464 ms
-- Memory: 0B
-- https://leetcode.com/problems/nth-highest-salary/

BEGIN
  DECLARE offset_val INT;
  SET offset_val = N - 1;

  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET offset_val
  );
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
