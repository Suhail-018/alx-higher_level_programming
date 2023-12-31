-- 12-no_genre.sql

-- Use the hbtn_0d_tvshows data

-- Select required columns from tv_shows and tv_show_genres tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
