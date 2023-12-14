-- 100-not_my_genres.sql

-- Use the hbtn_0d_tvshows database

-- Get the genre_id for the show Dexter
SET @dexter_id = (SELECT id FROM tv_shows WHERE title = 'Dexter' LIMIT 1);

-- Select genres not linked to Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT genre_id FROM tv_show_genres WHERE show_id = @dexter_id)
ORDER BY tv_genres.name ASC;
