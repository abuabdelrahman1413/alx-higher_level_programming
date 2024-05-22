-- This SQL query retrieves the average temperature for each city 
-- from the 'temperatures' table and orders the results in descending order 
-- of average temperature.
SELECT city,                -- Selects the 'city' column.
       AVG(value) AS avg_temp -- Calculates the average temperature ('value' column) and aliases it as 'avg_temp'.
FROM temperatures           -- Specifies the table from which to retrieve data.
WHERE month = 7 OR month = 8 -- Filters the data to include only rows where the 'month' is July or August.
GROUP BY city                -- Groups the results by 'city', so the average temperature is calculated for each city.
ORDER BY avg_temp DESC LIMIT 3; -- Orders the results in descending order based on 'avg_temp' and limits the output to the top 3 cities.
