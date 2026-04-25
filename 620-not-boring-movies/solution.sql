-- Not Boring Movies
-- Difficulty: Easy
-- Runtime: 258 ms
-- Memory: 0B
-- https://leetcode.com/problems/not-boring-movies/

# Write your MySQL query statement below
select * from Cinema
where id%2!=0 and description != 'boring'
order by rating desc
