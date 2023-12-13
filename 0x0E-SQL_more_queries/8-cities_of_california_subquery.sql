-- 8-cities_of_california_subquery.sql

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select all cities of California sorted by cities.id
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
