CREATE DATABASE smart_home;
USE smart_home;
 
CREATE TABLE rooms (
    room_id     INT AUTO_INCREMENT PRIMARY KEY,
    room_name   VARCHAR(50)  NOT NULL UNIQUE,
    floor_no    TINYINT      NOT NULL DEFAULT 0,
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
); 
 drop table devices;

CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(80)  NOT NULL,
    device_type VARCHAR(40)  NOT NULL,          
    room_id INT NOT NULL,
    rated_power_watts INT NOT NULL CHECK (rated_power_watts > 0),
    status ENUM('ON','OFF','STANDBY','FAULT') NOT NULL DEFAULT 'OFF',
    installed_on DATE NOT NULL DEFAULT (CURRENT_DATE),
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_devices_room FOREIGN KEY (room_id)
        REFERENCES rooms(room_id) ON DELETE RESTRICT ON UPDATE CASCADE
);
 
CREATE TABLE energy_logs (
    log_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id INT NOT NULL,
    recorded_at DATETIME NOT NULL,
    energy_kwh DECIMAL(10,4) NOT NULL CHECK (energy_kwh >= 0),
    power_watts DECIMAL(10,2) NULL,
    voltage DECIMAL(6,2)  NULL,
    CONSTRAINT fk_logs_device FOREIGN KEY (device_id) REFERENCES devices(device_id) ON DELETE CASCADE ON UPDATE CASCADE
);
 
CREATE INDEX idx_logs_device_time ON energy_logs (device_id, recorded_at);
CREATE INDEX idx_logs_time        ON energy_logs (recorded_at);
CREATE INDEX idx_devices_room     ON devices (room_id);
CREATE INDEX idx_devices_status   ON devices (status);
 
INSERT INTO rooms (room_name, floor_no) VALUES
    ('Living Room', 0),
    ('Bedroom',1),
    ('Kitchen',0),
    ('Study',1);
 
INSERT INTO devices (device_name, device_type, room_id, rated_power_watts, status) VALUES
    ('Living Room AC','AC',1, 1500, 'ON'),
    ('Smart TV','TV',1,  120, 'STANDBY'),
    ('Bedroom AC','AC',2, 1200, 'ON'),
    ('Bedroom Lamp','Light',2,10, 'OFF'),
    ('Refrigerator','Fridge',3,200, 'ON'),
    ('Microwave Oven','Microwave',3,1000, 'OFF'),
    ('Study Desktop','Computer',4,300, 'ON'),
    ('Study Light','Light',4,15,'ON');
 
 
INSERT INTO energy_logs (device_id, recorded_at, energy_kwh, power_watts, voltage) VALUES
    (1, '2026-10-12 08:00:00', 1.2000, 1480.00, 230.5),
    (1, '2026-10-12 14:00:00', 1.4500, 1495.00, 229.8),
    (1, '2026-10-12 21:00:00', 1.3000, 1470.00, 231.0),
    (2, '2026-10-12 20:00:00', 0.3000,  110.00, 230.2),
    (3, '2026-10-12 22:00:00', 2.1000, 1190.00, 230.7),
    (4, '2026-10-12 19:00:00', 0.0300,   10.00, 230.1),
    (5, '2026-10-12 00:00:00', 0.1500,  190.00, 230.4),
    (5, '2026-10-12 12:00:00', 0.1800,  200.00, 230.0),
    (6, '2026-10-12 13:00:00', 0.2500,  980.00, 229.5),
    (7, '2026-10-12 10:00:00', 0.9000,  290.00, 230.3),
    (8, '2026-10-12 18:00:00', 0.0800,   15.00, 230.6),
    (1, '2026-10-13 08:00:00', 1.1000, 1460.00, 230.9),
    (3, '2026-10-13 01:00:00', 2.4000, 1210.00, 230.2),
    (5, '2026-10-13 06:00:00', 0.1600,  195.00, 230.5),
    (7, '2026-10-13 11:00:00', 1.0500,  300.00, 230.1);
 

INSERT INTO rooms (room_name, floor_no) VALUES ('Balcony', 0);
 
INSERT INTO devices (device_name, device_type, room_id, rated_power_watts, status)
VALUES ('Washing Machine', 'Washer',
        (SELECT room_id FROM rooms WHERE room_name = 'Balcony'), 500, 'OFF');
 
INSERT INTO energy_logs (device_id, recorded_at, energy_kwh, power_watts, voltage)
VALUES (1, NOW(), 0.8500, 1475.00, 230.0);
 
 
SELECT d.device_id, d.device_name, d.device_type, r.room_name, d.status
FROM devices d
JOIN rooms r ON r.room_id = d.room_id
ORDER BY r.room_name, d.device_name;
 
-- Logs for one device in a time window (uses idx_logs_device_time)
SELECT * FROM energy_logs
WHERE device_id = 1
  AND recorded_at >= '2026-10-12 00:00:00'
  AND recorded_at <  '2026-10-13 00:00:00';
 
-- Total energy per device
SELECT d.device_name, ROUND(SUM(l.energy_kwh), 3) AS total_kwh
FROM devices d
JOIN energy_logs l ON l.device_id = d.device_id
GROUP BY d.device_id, d.device_name
ORDER BY total_kwh DESC;
 
-- Change device status
UPDATE devices SET status = 'OFF' WHERE device_name = 'Living Room AC';
 
-- Switch every light in the house off
UPDATE devices SET status = 'OFF' WHERE device_type = 'Light';
 
-- Correct a usage record
UPDATE energy_logs
SET energy_kwh = 1.3500, power_watts = 1490.00
WHERE device_id = 1 AND recorded_at = '2026-10-12 14:00:00';
 
-- Move a device to another room
UPDATE devices
SET room_id = (SELECT room_id FROM rooms WHERE room_name = 'Study')
WHERE device_name = 'Smart TV';
 
-- Remove old logs (data retention)
DELETE FROM energy_logs WHERE recorded_at < '2026-01-01 00:00:00';

DELETE FROM devices WHERE device_name = 'Washing Machine';
 
DROP PROCEDURE IF EXISTS sp_room_daily_energy;
 
DELIMITER $$
 
CREATE PROCEDURE sp_room_daily_energy (
    IN p_start_date DATE,
    IN p_end_date   DATE,
    IN p_room_id    INT         
)
BEGIN
    IF p_end_date < p_start_date THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'p_end_date must be on or after p_start_date';
    END IF;
 
    SELECT
        r.room_id,
        r.room_name,
        DATE(l.recorded_at) AS usage_date,
        COUNT(DISTINCT d.device_id) AS active_devices,
        ROUND(SUM(l.energy_kwh), 3) AS total_kwh
    FROM energy_logs l
    JOIN devices d ON d.device_id = l.device_id
    JOIN rooms   r ON r.room_id   = d.room_id
    WHERE l.recorded_at >= p_start_date
      AND l.recorded_at <  DATE_ADD(p_end_date, INTERVAL 1 DAY)
      AND (p_room_id IS NULL OR r.room_id = p_room_id)
    GROUP BY r.room_id, r.room_name, DATE(l.recorded_at)
    ORDER BY usage_date, r.room_name;
END$$
 
DELIMITER ;
 
CALL sp_room_daily_energy('2026-10-12', '2026-10-12', NULL);  
CALL sp_room_daily_energy('2026-10-12', '2026-10-13', 1);      
 
