-- Invalid Tweets
-- Difficulty: Easy
-- Runtime: 574 ms
-- Memory: 0B
-- https://leetcode.com/problems/invalid-tweets/

# Write your MySQL query statement below
select tweet_id       
from Tweets
where length(content)>15
