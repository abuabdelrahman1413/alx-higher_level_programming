-- This SQL statement creates a table named 'first_table' if it doesn't already exist.
-- The table will have two columns: 'id' and 'name'.

CREATE TABLE first_table IF NOT EXISTS ( 
    id INT,                  -- Creates an integer column named 'id'
    name VARCHAR(256)       -- Creates a string column named 'name' with a maximum length of 256 characters
);