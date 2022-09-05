-- Script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a database if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Creates a user if doesn't exist with given credentials.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant created users all privilege on database hbnb_test_db.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Grant created users all privilege on database performance_schema.