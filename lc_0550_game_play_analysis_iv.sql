SELECT 
    ROUND((
        SELECT COUNT(DISTINCT a.player_id)
        FROM Activity a
        JOIN (
            SELECT
                player_id,
                MIN(event_date) AS first_date
            FROM Activity
            GROUP BY player_id
        ) first_login
            ON a.player_id = first_login.player_id AND a.event_date = first_login.first_date + 1
    )::decimal
    /
    (
        SELECT COUNT(DISTINCT player_id)
        FROM Activity
    ), 2) AS fraction;
