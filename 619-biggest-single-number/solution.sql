-- Biggest Single Number
-- Difficulty: Easy
-- Runtime: 464 ms
-- Memory: 0B
-- https://leetcode.com/problems/biggest-single-number/

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
