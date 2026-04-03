-- Find Users With Valid E-Mails
-- Difficulty: Easy
-- Runtime: 1096 ms
-- Memory: 0B
-- https://leetcode.com/problems/find-users-with-valid-e-mails/

SELECT *
FROM Users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$', 'c');
