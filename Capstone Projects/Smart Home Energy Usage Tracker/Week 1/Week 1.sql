CREATE DATABASE IF NOT EXISTS smart_home;
use smart_home;

CREATE TABLE rooms(
    room_id int AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(50) NOT NULL
);

CREATE TABLE devices(
    device_id int AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    device_type VARCHAR(50),
    room_id INT NOT NULL,
    status ENUM('ON','OFF') NOT NULL DEFAULT 'OFF',
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE energy_logs(
    log_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id INT NOT NULL,
    energy_kwh DECIMAL(10,2) NOT NULL,
    log_timestamp DATETIME NOT NULL,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

INSERT INTO rooms (room_name) VALUES ('Living Room'), ('Bedroom'), ('Kitchen');

INSERT INTO devices(device_name, device_type, room_id, status) VALUES
('Air Conditioner','Cooling',1,'ON'),
('LED TV','Appliance',1,'OFF'),
('Ceiling Fan','Cooling',2,'ON'),
('Refrigerator','Appliance',3,'ON');

INSERT INTO energy_logs (device_id, energy_kwh, log_timestamp) VALUES
(1, 1.250, '2025-01-01 10:00:00'),
(1, 1.400, '2025-01-01 14:00:00'),
(2, 0.150, '2025-01-01 20:00:00'),
(3, 0.080, '2025-01-01 22:00:00'),
(4, 0.300, '2025-01-01 12:00:00'),
(1, 1.100, '2025-01-02 11:00:00');

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

