-- Find Followers Count
-- Difficulty: Easy
-- Runtime: 533 ms
-- Memory: 0B
-- https://leetcode.com/problems/find-followers-count/

# Write your MySQL query statement below
select user_id , count(* )as followers_count
from Followers 
group by user_id 
ORDER BY user_id;
