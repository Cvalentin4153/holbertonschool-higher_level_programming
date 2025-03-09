-- This script creates the MYSLQ user user_0d_2 and database hbtn_0d_2 and grants SELECT privilege
CREATE USER IF NOT EXISTS 'user_0d_2'@'loclahost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';