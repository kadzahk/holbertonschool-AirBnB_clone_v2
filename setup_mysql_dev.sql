-- Script that prepares a MySQL server for the project
-- Creates DB
CREATE DATABASE IF NOT EXISTS hbnb_dev_dv;
-- Creates user if not exists, identified with a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'
-- Grant all privileges to user on DB
GRANT ALL PRIVILEGES ON 'hbnb_dev_dv'.* TO 'hbnb_dev'@'localhost';
-- Grant Select privileges to user on performance_schema DB
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';
