-- This query retrieves scores and names from 'second_table', ordered by score (highest first).
SELECT score, name -- Selects the score and name columns
FROM second_table  -- From the 'second_table'
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC; -- Orders results by score in descending order
