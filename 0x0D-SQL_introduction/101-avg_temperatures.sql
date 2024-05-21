-- This SQL query retrieves the average temperature for each city 
-- from the 'temperatures' table and orders the results in descending order 
-- of average temperature.

SELECT city,        -- Select the 'city' column.
       AVG(value) AS avg_temp  -- Calculate the average temperature for each city and alias it as 'avg_temp'.
FROM temperatures   -- Specify the table from which to retrieve data.
GROUP BY city        -- Group the results by city, so the average temperature is calculated for each distinct city.
ORDER BY avg_temp DESC; -- Order the results in descending order based on the calculated average temperature.
