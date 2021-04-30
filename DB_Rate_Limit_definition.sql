
CREATE USER IF NOT EXISTS 'ratelimit'@'localhost' IDENTIFIED BY 'Password';
-- GRANT ALL PRIVILEGES ON Rate_limit.* TO 'ratelimit'@'localhost';
GRANT SELECT, INSERT, DELETE ON Rate_limit.* TO 'ratelimit'@'localhost';
FLUSH PRIVILEGES;


-- DROP DATABASE IF EXISTS Rate_limit;
CREATE DATABASE IF NOT EXISTS Rate_limit
CHARACTER SET utf8mb4;

USE Rate_limit;

DROP TABLE IF EXISTS `Rate_limit`.`Settings` ;
CREATE TABLE IF NOT EXISTS `Rate_limit`.`Settings` (
    -- `resource_id`                   INT AUTO_INCREMENT,
    `resource`                      VARCHAR(255) NOT NULL PRIMARY KEY,
    `filter`                        VARCHAR(255),
    `rate_limit_number_requests`    INT,
    `rate_limit_time_period`        INT,
    `description`                   TEXT,
    `enabled`                       TINYINT,
    `date_created`                  DATETIME
    );

DROP TABLE IF EXISTS `Rate_limit`.`Data` ;
CREATE TABLE IF NOT EXISTS `Rate_limit`.`Data` (
    `id`                 	INT AUTO_INCREMENT PRIMARY KEY,
    -- `resource_id`        INT,
    `resource`              VARCHAR(255) NOT NULL,
    `filter`                VARCHAR(255),
    `event_data`            TEXT,
    `date_unix_timestamp`   INT UNSIGNED
    );








