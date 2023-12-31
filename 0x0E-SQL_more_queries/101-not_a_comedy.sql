-- 101-not_a_comedy.sql

-- Use the hbtn_0d_tvshows database

-- Get the genre_id for Comedy
SET @comedy_id = (SELECT id FROM tv_genres WHERE name = 'Comedy' LIMIT 1);

-- Select shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT show_id FROM tv_show_genres WHERE genre_id = @comedy_id)
ORDER BY tv_shows.title ASC;

