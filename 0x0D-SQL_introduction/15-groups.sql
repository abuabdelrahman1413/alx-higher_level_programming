-- This SQL query analyzes the distribution of scores in the 'second_table' by grouping scores and counting their occurrences.
SELECT score, COUNT(score) number FROM second_table GROUP BY score;
