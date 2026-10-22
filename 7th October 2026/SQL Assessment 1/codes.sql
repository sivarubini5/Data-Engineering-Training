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

