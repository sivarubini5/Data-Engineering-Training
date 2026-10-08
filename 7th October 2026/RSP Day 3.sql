-- https://drive.google.com/file/d/1BuD3Ewpo5NRZdujOLdZ4KPq4ultZ01Yg/view
-- Assessment 1 — Telecom Customer & Billing Analytics
CREATE DATABASE telecom_assessment;
USE telecom_assessment;
CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
mobile VARCHAR(30),
email VARCHAR(100)
);
INSERT INTO customers VALUES
(1, ' Arjun Rao ', 'Hyderabad', '98765-43210', ' ARJUN@GMAIL.COM '),
(2, 'SARA KHAN', 'Mumbai', '+91 99887 66554', 'sara@gmail.com'),
(3, 'Rohit Mehta ', 'Delhi', '9988 776 655', ''),
(4, 'Neha Singh', 'Hyderabad', '9876543210', 'neha@yahoo.com'),
(5, 'Imran Ali', 'Bangalore', '98765-AB210', NULL),
(6, 'Priya Nair', 'Pune', '9123456789', 'PRIYA@GMAIL.COM'),
(7, 'Kabir Shah', NULL, '9000011111', 'kabir@mail.com');

CREATE TABLE plans (
plan_id INT PRIMARY KEY,
plan_name VARCHAR(50),
monthly_charge DECIMAL(10,2)
);
INSERT INTO plans VALUES
(101, 'Basic', 399),
(102, 'Standard', 599),

(103, 'Premium', 999),
(104, 'Unlimited', 1499),
(105, 'Business', 1999);

CREATE TABLE subscriptions (
subscription_id INT PRIMARY KEY,
customer_id INT,
plan_id INT,
start_date DATE,
status VARCHAR(20)
);
INSERT INTO subscriptions VALUES
(1001, 1, 103, '2026-01-01', 'Active'),
(1002, 2, 102, '2026-01-15', 'Active'),
(1003, 3, 101, '2026-02-01', 'Inactive'),
(1004, 4, 104, '2026-02-10', 'Active'),
(1005, 5, 102, '2026-03-01', 'Active'),
(1006, 1, 105, '2026-04-01', 'Active'),
(1007, 6, NULL, '2026-04-15', 'Pending'),
(1008, 20, 103, '2026-05-01', 'Active');

CREATE TABLE payments (
payment_id INT PRIMARY KEY,
customer_id INT,
payment_date DATE,
amount DECIMAL(10,2)
);
INSERT INTO payments VALUES
(501, 1, '2026-01-05', 999),
(502, 2, '2026-01-18', 599),
(503, 1, '2026-02-05', 999),
(504, 3, '2026-02-10', 399),
(505, 4, '2026-02-15', 1499),
(506, 2, '2026-03-18', 599),
(507, 5, '2026-03-20', 599),
(508, 1, '2026-04-05', 1999),
(509, 4, '2026-04-15', 1499),
(510, 5, '2026-05-20', 599),
(511, 2, '2026-05-22', 599),
(512, 1, '2026-06-05', 1999);

/*Section A — Basics & CRUD

1. Display customer name, city and email for all customers.
2. Display customers belonging to Hyderabad or Mumbai.
3. Display customers whose names contain the letter a .
4. Insert one new customer of your choice.
5. Update the city of customer ID 6.
6. Delete the customer inserted in Question 4.
7. Display customers ordered alphabetically by customer name.*/

SELECT customer_name,city,email from customers;
SELECT * from customers WHERE city='Hyderabad'or city='Mumbai';
SELECT * FROM customers WHERE customer_name like '%a%';
INSERT into customers(customer_id, customer_name, city, mobile, email) VALUES(8,'Tara','Chennai','2579643815','tara@gmail.com');
UPDATE customers set city='Chennai' where customer_id=6;
DELETE FROM customers WHERE customer_id=8;
SELECT customer_name FROM customers ORDER BY customer_name asc;

/*Section B — Aggregation / GROUP BY / HAVING

8. Find the total number of payments and total amount collected.
9. Calculate total payment amount for each customer.
10. Display customers whose total payments exceed ₹2,000.
11. Find the average payment amount made by each customer.*/

SELECT count(payment_id) as no_of_payments,sum(amount) as total_amount from payments;
SELECT c.customer_name ,sum(p.amount) as total_amount FROM customers c INNER JOIN payments p on c.customer_id=p.customer_id GROUP by c.customer_id,c.customer_name;
SELECT c.customer_name ,sum(p.amount) as total_amount FROM customers c INNER JOIN payments p on c.customer_id=p.customer_id GROUP by c.customer_id,c.customer_name HAVING total_amount>2000;
SELECT c.customer_name ,avg(p.amount) as average_amount FROM customers c INNER JOIN payments p on c.customer_id=p.customer_id GROUP by c.customer_id,c.customer_name;



/*Section C — JOINs

12. Display customer name, plan name, monthly charge and subscription status.
13. Display all customers, including customers who have no subscription.
14. Identify subscriptions having no valid customer or plan.*/

SELECT c.customer_name, p.plan_name, p.monthly_charge,s.status from subscriptions s 
inner join customers c on s.customer_id=c.customer_id
inner join plans p on s.plan_id=p.plan_id;
SELECT * from customers c left JOIN subscriptions s on s.customer_id=c.customer_id;
SELECT s.subscription_id,s.customer_id,s.plan_id,s.start_date,s.status from subscriptions s 
left join customers c on s.customer_id=c.customer_id
left join plans p on s.plan_id=p.plan_id where p.plan_id is null or c.customer_id is NULL;

/*Section D — Data Cleansing / RegEx

15. Produce a cleaned customer output where:
names have leading/trailing spaces removed,
emails are lowercase,
blank emails become NULL ,
mobile numbers contain only numeric characters.
16. Using RegEx, identify mobile numbers containing alphabetic characters.*/

select TRIM(customer_name),
case
when TRIM(email)='' THEN null
ELSE lower(email)
end,
REGEXP_REPLACE(mobile,'[^0-9]',''),city from customers;

SELECT * From customers where REGEXP_LIKE(mobile,'[A-Za-z]');

-- ---------------------------------------------------------------------------------------------------------------------------------------------
-- Assessment 2 — Airline Booking & Employee Operations
CREATE DATABASE airline_assessment;
USE airline_assessment;

CREATE TABLE flights (
flight_id INT PRIMARY KEY,
airline VARCHAR(50),
source_city VARCHAR(50),
destination_city VARCHAR(50),
ticket_price DECIMAL(10,2)
);
INSERT INTO flights VALUES
(201, 'SkyJet', 'Hyderabad', 'Delhi', 6500),
(202, 'AirWorld', 'Mumbai', 'Bangalore', 7200),
(203, 'SkyJet', 'Delhi', 'Mumbai', 5800),
(204, 'FlyHigh', 'Hyderabad', 'Dubai', 18000),
(205, 'AirWorld', 'Bangalore', 'Delhi', 6900),
(206, 'FlyHigh', 'Mumbai', 'Singapore', 22000),
(207, 'SkyJet', 'Hyderabad', 'Mumbai', 5200);

CREATE TABLE passengers (
passenger_id INT PRIMARY KEY,
passenger_name VARCHAR(100),
city VARCHAR(50),
email VARCHAR(100)
);

INSERT INTO passengers VALUES
(1, 'Aman Verma', 'Hyderabad', ' AMAN@MAIL.COM '),
(2, 'Sara Ali', 'Mumbai', 'sara@gmail.com'),

(3, 'Rakesh Rao', 'Delhi', ''),
(4, 'Meena Shah', 'Bangalore', 'MEENA@YAHOO.COM'),
(5, 'Farah Khan', 'Hyderabad', NULL),
(6, 'John Mathew', 'Pune', 'john@gmail.com'),
(7, 'Priya Das', NULL, 'priya@mail.com');


CREATE TABLE bookings (
booking_id INT PRIMARY KEY,
passenger_id INT,
flight_id INT,
booking_date DATE,
seats INT,
status VARCHAR(20)
);
INSERT INTO bookings VALUES
(1001, 1, 201, '2026-06-01', 1, 'Confirmed'),
(1002, 2, 202, '2026-06-02', 2, 'Confirmed'),
(1003, 1, 204, '2026-06-03', 1, 'Confirmed'),
(1004, 3, 203, '2026-06-04', 1, 'Cancelled'),
(1005, 4, 205, '2026-06-05', 3, 'Confirmed'),
(1006, 5, 207, '2026-06-06', 2, 'Confirmed'),
(1007, 2, 206, '2026-06-07', 1, 'Confirmed'),
(1008, 20, 201, '2026-06-08', 1, 'Confirmed'),
(1009, 6, NULL, '2026-06-09', 2, 'Pending');

CREATE TABLE airline_staff (
employee_id INT PRIMARY KEY,
employee_name VARCHAR(100),
manager_id INT,
department VARCHAR(50),
salary DECIMAL(10,2)
);
INSERT INTO airline_staff VALUES
(1, 'Raj Kumar', NULL, 'Management', 200000),
(2, 'Meera Rao', 1, 'Operations', 140000),

(3, 'Imran Khan', 1, 'Sales', 135000),
(4, 'Aman Shah', 2, 'Operations', 90000),
(5, 'Priya Singh', 2, 'Operations', 85000),
(6, 'Rohit Das', 3, 'Sales', 75000),
(7, 'Farah Ali', 3, 'Sales', 78000),
(8, 'Vikas Rao', 4, 'Support', 60000);
/*
Section A — Filtering & Manipulation

1. Display flights originating from Hyderabad.
2. Display flights priced between ₹6,000 and ₹20,000.
3. Display international-looking routes where ticket price exceeds ₹15,000.
4. Increase the ticket price of all SkyJet flights by 5%.
5. Display the three most expensive flights.*/
SELECT * from flights where source_city='Hyderabad';
SELECT * from flights where ticket_price BETWEEN 6000 and 20000;
SELECT * from flights where ticket_price>15000 AND destination_city in ('Dubai','Singapore','London');
UPDATE flights set ticket_price=ticket_price*1.05 WHERE airline='SkyJet';
SELECT * FROM flights ORDER BY ticket_price desc limit 3;

/*Section B — Aggregate / GROUP BY / HAVING

6. Find average ticket price by airline.
7. Find total number of seats booked on each flight.
8. Find airlines whose average ticket price exceeds ₹8,000.
9. Find total booking value per airline using: seats × ticket_price
*/
SELECT AVG(ticket_price),airline from flights GROUP by airline;
SELECT flight_id,sum(seats) from bookings where booking_id is not null GROUP by flight_id;
SELECT AVG(ticket_price) as aver,airline from flights GROUP by airline HAVING aver>8000;
SELECT f.airline,sum(b.seats*f.ticket_price) as tot_booking_val from flights f inner join
bookings b on b.flight_id=f.flight_id GROUP by f.airline;

/*
Section C — JOINs

10. Display passenger name, airline, source, destination and booking status.
11. Display all passengers including passengers who have never booked a flight.
12. Find bookings having either:
no valid passenger, or
no valid flight.*/
select p.passenger_name,f.airline,f.source_city,f.destination_city,b.status from bookings b
inner join passengers p on p.passenger_id=b.passenger_id
INNER JOIN flights f on f.flight_id=b.flight_id;
select * from passengers p left join bookings b on b.passenger_id=p.passenger_id;
SELECT * from bookings b left join passengers p on b.passenger_id=p.passenger_id
LEFT join flights f on f.flight_id=b.flight_id WHERE f.flight_id is NULL or p.passenger_id is null;
/*
Section D — JOIN + Aggregate

13. Calculate total booking value generated by every passenger.

14. Display passengers whose confirmed booking value exceeds ₹10,000.*/
SELECT p.passenger_name,sum(b.seats*f.ticket_price) from  passengers p LEFT join bookings b on b.passenger_id=p.passenger_id
LEFT join flights f on f.flight_id=b.flight_id group by p.passenger_id,p.passenger_name ;
SELECT p.passenger_name,sum(b.seats*f.ticket_price) as tot from bookings b inner join passengers p on b.passenger_id=p.passenger_id
inner join flights f on f.flight_id=b.flight_id WHERE b.status='Confirmed' group by p.passenger_id,p.passenger_name having tot>10000;


