-- Select the database to work with

-- Select the 'name' column from the 'cities' table
SELECT id, name
-- Filter the cities based on their 'state_id'
FROM cities 
-- Where the 'state_id' matches the 'id' of the state named 'California'
WHERE state_id = (
    -- Subquery to find the 'id' of the state named 'California'
    SELECT id FROM states WHERE name = 'California'
)
-- Order the results in ascending order based on the 'id' column
ORDER BY id ASC;
