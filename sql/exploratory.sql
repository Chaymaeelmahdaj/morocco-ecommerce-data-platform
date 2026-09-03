-- ============================================================
-- Morocco E-Commerce Data Platform
-- Exploratory SQL
-- ============================================================


-- 1. Number of customers

SELECT
    COUNT(*) AS total_customers
FROM customers;


-- 2. Number of orders

SELECT
    COUNT(*) AS total_orders
FROM orders;


-- 3. Orders by status

SELECT
    order_status,
    COUNT(*) AS order_count
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;


-- 4. Revenue from order items

SELECT
    ROUND(SUM(price), 2) AS total_product_revenue
FROM order_items;


-- 5. Freight revenue

SELECT
    ROUND(SUM(freight_value), 2) AS total_freight
FROM order_items;


-- 6. Revenue by order item

SELECT
    order_id,
    ROUND(
        SUM(price) + SUM(freight_value),
        2
    ) AS order_total
FROM order_items
GROUP BY order_id
ORDER BY order_total DESC
LIMIT 10;


-- 7. Average order value

SELECT
    ROUND(
        AVG(order_total),
        2
    ) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(price) + SUM(freight_value) AS order_total
    FROM order_items
    GROUP BY order_id
);


-- 8. Review score distribution

SELECT
    review_score,
    COUNT(*) AS review_count
FROM reviews
GROUP BY review_score
ORDER BY review_score;


-- 9. Top sellers by product revenue

SELECT
    seller_id,
    ROUND(SUM(price), 2) AS revenue
FROM order_items
GROUP BY seller_id
ORDER BY revenue DESC
LIMIT 10;


-- 10. Top products by revenue

SELECT
    product_id,
    ROUND(SUM(price), 2) AS revenue
FROM order_items
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;