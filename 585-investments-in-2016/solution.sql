-- Investments in 2016
-- Difficulty: Medium
-- Runtime: 592 ms
-- Memory: 0B
-- https://leetcode.com/problems/investments-in-2016/

    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
