-- This SQL code creates a new table called 'second_table' and then populates it with some initial data.
-- Create the 'second_table' with columns for id, name, and score.
CREATE TABLE second_table (
    id INT PRIMARY KEY,  -- 'id' is an integer and the primary key of the table, ensuring each row has a unique identifier.
    name VARCHAR(256),   -- 'name' is a string that can hold up to 256 characters.
    score INT            -- 'score' is an integer value.
);

-- Insert four rows of data into the 'second_table'.
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
