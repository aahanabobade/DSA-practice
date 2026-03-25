-- Not Boring Movies
-- Difficulty: Easy
-- Runtime: 246 ms
-- Memory: 0B
-- https://leetcode.com/problems/not-boring-movies/

# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;
