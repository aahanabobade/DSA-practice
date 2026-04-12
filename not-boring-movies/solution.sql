-- Q3. Not Boring Movies
-- Difficulty: Easy
-- Runtime: 282 ms
-- Memory: 0B
-- https://leetcode.com/problems/not-boring-movies/

# Write your MySQL query statement below
select * 
from Cinema
where id % 2 =1 and description != 'boring'
order by rating desc
