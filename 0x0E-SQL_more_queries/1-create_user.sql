--creates the MySQL server user user_0d_1
-- Set a variable with the hashed password
SET @user_pwd = PASSWORD('user_0d_1_pwd');

-- Create the user with the hashed password
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY PASSWORD @user_pwd;
