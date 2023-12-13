-- 2-create_read_user.sql
-- Create database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user_0d_2 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant usage on all databases and SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

