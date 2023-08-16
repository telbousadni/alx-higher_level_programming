-- Check if the user already exists
SELECT COUNT(*) INTO @user_count FROM mysql.user WHERE user = 'user_0d_1';

-- If the user doesn't exist, create it
IF @user_count = 0 THEN
  CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
  GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
  FLUSH PRIVILEGES;
END IF;

