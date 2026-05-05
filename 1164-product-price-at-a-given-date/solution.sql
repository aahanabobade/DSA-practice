-- Product Price at a Given Date
-- Difficulty: Medium
-- Runtime: 493 ms
-- Memory: 0B
-- https://leetcode.com/problems/product-price-at-a-given-date/

        SELECT product_id, new_price
        FROM Products
        WHERE (product_id, change_date) IN (
            SELECT product_id, MAX(change_date)
            FROM Products
            WHERE change_date <= '2019-08-16'
            GROUP BY product_id
        )
    ) t
ON p.product_id = t.product_id;
