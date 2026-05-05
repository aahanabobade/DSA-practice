-- Friend Requests II: Who Has the Most Friends
-- Difficulty: Medium
-- Runtime: 353 ms
-- Memory: 0B
-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

# Write your MySQL query statement below
SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) AS all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;
