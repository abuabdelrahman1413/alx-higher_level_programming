--This SQL code modifies the 'first_table' to ensure that the 'name' column 
--can store a wider range of characters and that the entire table uses a 
--character set that supports a broader set of characters, including emojis.

-- Changes the 'name' column to VARCHAR(255) with utf8mb4 character set for broader character support.
ALTER TABLE first_table CHANGE name name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Converts the entire 'first_table' to the utf8mb4 character set and utf8mb4_unicode_ci collation.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- It appears this line is redundant, as the 'name' column was already altered in the first statement.
ALTER TABLE first_table CHANGE name name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;