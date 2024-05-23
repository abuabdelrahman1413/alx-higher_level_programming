-- Select the database to work with
USE `hbtn_0d_usa`;

-- Select the desired columns from the 'cities' and 'states' tables
SELECT c.id, c.name AS city_name, s.name AS state_name
-- Join the 'cities' and 'states' tables based on the 'state_id' relationship
FROM cities c
JOIN states s ON c.state_id = s.id -- This JOIN clause combines rows from 'cities' and 'states' tables
                                  -- based on the matching 'state_id' in 'cities' and 'id' in 'states'
-- Order the results in ascending order based on the 'id' column of the 'cities' table
ORDER BY c.id ASC;
