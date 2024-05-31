# Write your MySQL query statement below
SELECT product_id, COALESCE(last_price, 10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM products
) t
LEFT JOIN (
    SELECT product_id, new_price AS last_price
    FROM (
        SELECT product_id, new_price,
               ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
        FROM products
        WHERE change_date <= '2019-08-16'
    ) sub
    WHERE rn = 1
) p USING (product_id);