-- This SQL statement creates a database if it doesn't already exist.
-- The database name is 'hbtn_0d_2'.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the MySQL server user user_0d_2
CREATE USER IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY 'user_0d_2_pwd';
-- Grants all privileges to user_0d_1
GRANT SELECT  ON hbtn_0d_2.* TO `user_0d_2`@`localhost`;
