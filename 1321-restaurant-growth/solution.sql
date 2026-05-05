-- Restaurant Growth
-- Difficulty: Medium
-- Runtime: 374 ms
-- Memory: 0B
-- https://leetcode.com/problems/restaurant-growth/

    ) AS amount,
    ROUND(
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) / 7, 2
    ) AS average_amount
FROM daily
ORDER BY visited_on
LIMIT 1000000 OFFSET 6;
