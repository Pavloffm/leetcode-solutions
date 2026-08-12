SELECT query_name, 
    ROUND(AVG(rating::numeric / position), 2) AS quality,
    ROUND(COUNT(rating) FILTER (WHERE rating < 3)::numeric / COUNT(rating) * 100, 2) AS poor_query_percentage
FROM Queries q
GROUP BY query_name
