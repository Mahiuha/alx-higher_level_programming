-- Create a database, table with constraints, and populate the table
-- Creating a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the database
USE hbtn_0d_usa;
-- Creating a table with constraints
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
