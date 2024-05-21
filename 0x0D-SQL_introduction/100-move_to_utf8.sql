--This SQL code modifies the character set and collation of the 'hbtn_0c_0' database 
--and its 'first_table'.  It aims to ensure that the database and the 'name' column 
--in the table can handle a wider range of characters, including emojis.


-- Sets the character set and collation for the entire 'hbtn_0c_0' database to utf8mb4.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Converts the 'first_table' to use the utf8 character set and utf8_unicode_ci collation.
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;

-- Modifies the 'name' column in 'first_table' to use VARCHAR(256), utf8 character set, and utf8_general_ci collation.
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci;
