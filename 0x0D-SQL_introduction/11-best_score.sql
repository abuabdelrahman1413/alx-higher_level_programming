-- Select the score and name of each entry in the 'second_table' where the score is greater than or equal to 10.
-- The results are sorted in descending order based on the score.
SELECT score, name 
FROM second_table 
where score >= 10  -- Filter results to include only scores greater than or equal to 10.
ORDER BY score DESC; -- Sort the results in descending order based on the score.
