-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create table 'cities' if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    -- Auto-incrementing primary key
    id INT NOT NULL AUTO_INCREMENT,
    -- Foreign key referencing 'states' table
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    -- City name (not nullable)
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
