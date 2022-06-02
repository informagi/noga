CREATE DATABASE matomo;

CREATE USER 'matomo'@'%' IDENTIFIED WITH mysql_native_password BY '${mysql_user_password}';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, DROP, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON matomo.* TO 'matomo'@'%';
GRANT FILE ON *.* TO 'matomo'@'%';
