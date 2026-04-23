-- Article Views I
-- Difficulty: Easy
-- Runtime: 425 ms
-- Memory: 0B
-- https://leetcode.com/problems/article-views-i/

# Write your MySQL query statement below
select DISTINCT  author_id as id
from Views 
where author_id = viewer_id
ORDER BY id;
