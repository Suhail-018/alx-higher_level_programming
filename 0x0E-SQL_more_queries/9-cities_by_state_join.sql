-- 9-cities_by_state_join.sql
-- Use the hbtn_0d_usa database

-- Select required columns and join cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
