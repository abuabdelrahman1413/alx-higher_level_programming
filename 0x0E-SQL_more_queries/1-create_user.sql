-- Creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges to user_0d_1
GRANT ALL  ON *.* TO `user_0d_1`@`localhost`;

-- Apply the changes
FLUSH PRIVILEGES;
