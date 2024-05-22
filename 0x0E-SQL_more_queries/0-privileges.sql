-- Define user variables for flexibility
SET @user1 = 'user_0d_1';
SET @user2 = 'user_0d_2';
-- Display the grants for the first user
SHOW GRANTS FOR @user1 @localhost;

-- Display the grants for the second user
SHOW GRANTS FOR @user2 @localhost;
