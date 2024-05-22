-- Retrieves the maximum temperature for each state, 
-- ordered alphabetically by state name.
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
