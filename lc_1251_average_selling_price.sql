SELECT p.product_id, ROUND(COALESCE(
        ROUND(SUM(p.price * us.units)::numeric / NULLIF(SUM(us.units), 0), 2),
        0
    ), 2) AS average_price
FROM Prices p
LEFT JOIN UnitsSold us
ON us.product_id = p.product_id AND us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
