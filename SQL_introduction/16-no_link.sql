-- This script lists all the records of the table second_table where name is not NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;