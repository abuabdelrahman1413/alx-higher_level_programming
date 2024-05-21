-- This SQL statement creates a table named 'first_table' if it doesn't already exist.
-- The table will have two columns: 'id' and 'name'.
CREATE TABLE first_table IF NOT EXISTS ( 
    id INT,
    name VARCHAR(256)
);
