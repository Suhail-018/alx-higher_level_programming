-- 6-states.sql

-- Create database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Create table states if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
