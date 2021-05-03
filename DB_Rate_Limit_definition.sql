
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



-- Tbl Data maintenance (registers of type Resource, older than 10000 times of allowed in Settings will be Dropped once a week)
-- Example if rate_limit_time_period is 120s for resource A, events of this resource type older than 14 days aprox (1200000s) will be dropped form tbl data
-- SHOW PROCESSLIST;
-- SHOW EVENTS FROM rate_limit;
-- SELECT * FROM INFORMATION_SCHEMA.events;
-- DROP EVENT IF EXISTS tbl_data_maintenance;
delimiter |
CREATE EVENT IF NOT EXISTS tbl_data_maintenance
    ON SCHEDULE EVERY 7 DAY
    STARTS CURRENT_TIMESTAMP
    DO
        BEGIN
            CREATE TEMPORARY TABLE hist AS (
                SELECT d.id
                FROM data AS d INNER JOIN settings AS s
                    ON d.resource = s.resource
                WHERE d.date_unix_timestamp < (unix_timestamp(UTC_TIMESTAMP()) - s.rate_limit_time_period * 10000)
                );
            DELETE FROM data WHERE id IN ( SELECT id FROM hist );
            DROP TEMPORARY TABLE hist;
        END |
delimiter ;



