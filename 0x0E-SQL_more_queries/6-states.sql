-- Creates a database named 'hbtn_0d_usa' if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switches to the 'hbtn_0d_usa' database.
USE hbtn_0d_usa;
-- Creates a table named 'states' if it doesn't already exist.
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
