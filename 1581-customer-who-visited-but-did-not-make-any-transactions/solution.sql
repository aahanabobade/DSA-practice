-- Customer Who Visited but Did Not Make Any Transactions
-- Difficulty: Easy
-- Runtime: 1937 ms
-- Memory: 0B
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

select v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
