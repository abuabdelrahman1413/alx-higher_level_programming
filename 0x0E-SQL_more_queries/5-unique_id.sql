-- Creates a table named 'unique_id' if it doesn't already exist.
CREATE TABLE IF NOT EXISTS unique_id (
    -- 'id' column: An integer with a unique constraint, defaulting to 1.
    -- Note: This default value might cause issues if you insert rows without specifying 'id'.
    id INT UNIQUE DEFAULT 1, 
    -- 'name' column: A string (VARCHAR) that can store up to 255 characters.
    name VARCHAR(255)
);
