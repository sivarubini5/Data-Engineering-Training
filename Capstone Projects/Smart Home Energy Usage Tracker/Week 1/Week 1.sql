CREATE DATABASE IF NOT EXISTS smart_home;
use smart_home;

CREATE TABLE IF NOT EXISTS rooms(
    room_id int AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS devices(
    device_id int AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    device_type VARCHAR(50),
    room_id INT NOT NULL,
    status ENUM('ON','OFF') NOT NULL DEFAULT 'OFF',
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE IF NOT EXISTS energy_logs(
    log_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id INT NOT NULL,
    energy_kwh DECIMAL(10,2) NOT NULL,
    log_timestamp DATETIME NOT NULL,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

INSERT INTO rooms (room_name) VALUES
('Living Room'), ('Bedroom'), ('Kitchen'), ('Utility Area'), ('Bathroom');
 
INSERT INTO devices (device_name, device_type, room_id, status) VALUES
('Air Conditioner',  'Cooling',   1, 'ON'),
('LED TV',           'Appliance', 1, 'OFF'),
('Ceiling Fan',      'Cooling',   2, 'ON'),
('Laptop Charger',   'Charger',   2, 'ON'),
('Refrigerator',     'Appliance', 3, 'ON'),
('Microwave',        'Appliance', 3, 'OFF'),
('Washing Machine',  'Appliance', 4, 'OFF'),
('Geyser',           'Heating',   5, 'ON'),
('Wi-Fi Router',     'Network',   1, 'ON'),
('LED Lights',       'Lighting',  2, 'ON');
 
INSERT INTO energy_logs (device_id, energy_kwh, log_timestamp) VALUES
(1, 0.650, '2025-01-01 10:00:00'),
(1, 0.720, '2025-01-01 14:00:00'),
(2, 0.080, '2025-01-01 20:00:00'),
(3, 0.040, '2025-01-01 22:00:00'),
(5, 0.050, '2025-01-01 12:00:00'),
(1, 0.580, '2025-01-02 11:00:00'),
(8, 0.800, '2025-01-02 06:00:00'),
(7, 0.350, '2025-01-02 09:00:00');

SELECT * FROM rooms;
SELECT * FROM devices;
SELECT * FROM energy_logs WHERE device_id = 1;
SELECT * FROM energy_logs
WHERE log_timestamp BETWEEN '2025-01-01 00:00:00' AND '2025-01-01 23:59:59';

UPDATE energy_logs SET energy_kwh=1.300 WHERE log_id=1;

DELETE FROM energy_logs where log_id=6;

DELIMITER //
CREATE PROCEDURE CalculateRoomDailyEnergy()
BEGIN
    SELECT r.room_id,r.room_name,date(e.log_timestamp) as usage_date,sum(e.energy_kwh) as total_energy_kwh
    from energy_logs e INNER JOIN devices d on d.device_id=e.device_id
    INNER JOIN rooms r on r.room_id=d.room_id
    GROUP BY r.room_id,r.room_name,date(e.log_timestamp)
    ORDER BY usage_date,r.room_name;
END//

DELIMITER ;

CALL CalculateRoomDailyEnergy();

