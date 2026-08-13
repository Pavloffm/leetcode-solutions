SELECT ROUND(COUNT(*) FILTER (WHERE d.order_date = d.customer_pref_delivery_date)::decimal / COUNT(*) * 100, 2) AS immediate_percentage
From Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS order_date
    FROM Delivery
    GROUP BY customer_id
) first_orders
ON d.customer_id = first_orders.customer_id AND d.order_date = first_orders.order_date
