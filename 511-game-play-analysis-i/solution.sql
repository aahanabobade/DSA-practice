-- Game Play Analysis I
-- Difficulty: Easy
-- Runtime: 479 ms
-- Memory: 0B
-- https://leetcode.com/problems/game-play-analysis-i/

SELECT 
    player_id, 
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
