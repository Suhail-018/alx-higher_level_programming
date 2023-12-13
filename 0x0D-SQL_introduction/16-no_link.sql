-- 16-no_link.sql
-- List scores and names from second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
