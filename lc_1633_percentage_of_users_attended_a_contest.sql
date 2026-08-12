
SELECT contest_id, ROUND(COUNT(user_id)::numeric / (SELECT COUNT(DISTINCT user_id) FROM users) * 100, 2) AS percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC
