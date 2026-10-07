/* columns -> properties eg: properties which helps to identify a school going kid are uniforn,shoes,bag etc..
Domain Driven Design (DDD) -> similarly we can give different column names for different domain classes like Corporate(Employee),Retail(Products),etc..
*/
-- day 1 class notes crud operations
CREATE DATABASE training_db;
USE training_db;
CREATE TABLE employees(
 emp_id int primary key,
 emp_name VARCHAR(100),
 department VARCHAR(50),
 salary DECIMAL(10,2),
 city VARCHAR(50)
);

INSERT INTO employees VALUES (1,'Amit Sharma','IT',60000,'Hyderabad'),
(2, 'Sara Khan', 'HR', 50000, 'Bangalore'),
(3, 'Rahul Verma', 'Finance', 55000, 'Hyderabad'),
(4, 'Neha Singh', 'IT', 65000, 'Pune'),
(5, 'Arjun Mehta', 'Sales', 45000, 'Mumbai');

SELECT * from employees;

update employees set emp_name ='Neha Varma'where emp_id=3;

delete from employees where emp_id=5;

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- practice - Online store database
/* 1. Create a database named shop_db.
2. Create a table named products with:
    Product ID
    Product Name
    Category
    Price
    Stock Quantity
3. Make Product ID the primary key.
4. Insert at least 6 products from different categories.
5. Display all products.
6. Display only Product Name and Price.
7. Insert a new product named Wireless Mouse.
8. Change the price of one product using its Product ID.
9. Increase the price of all products in the Electronics category by 10%.
10. Reduce the stock quantity of one product after a sale.
11. Change the category of one product.
12. Display products costing more than ₹1,000.
13. Display products whose stock quantity is less than 10.
14. Display only Electronics products.
15. Sort products from highest price to lowest price.
16. Delete one product using its Product ID.
17. Delete products whose stock quantity is 0.
18. Display all remaining products.*/

CREATE DATABASE shop_db;
USE shop_db;
CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT
);
INSERT INTO products VALUES (1,'pen','stationery','10',100),
(2,'cheese','food','50',200),
(3,'Face wash','skincare','80',100),
(4,'Shampoo','haircare','15',0),
(5,'Sneakers','footwear','1000',80),
(6,'smartphone','Electronics','20000',1000);

SELECT * from products;

select product_name,price from products;

INSERT into products VALUE(7,'Wireless Mouse','gadgets','5000',500);

UPDATE products set stock_quantity=800 where product_id=6;

UPDATE products set price=(price*1.1) where category='Electronics';

UPDATE products set stock_quantity=(stock_quantity-10) where product_id=5;

UPDATE products set category='Electronics' where product_id=7;

select * from products where price>1000;

select * from products where stock_quantity<10;

select * from products where category='Electronics';

SELECT * FROM products ORDER BY price desc;

DELETE FROM products where product_id=2;

select * from products where stock_quantity=0;

select * from products;

TRUNCATE TABLE products;

-- ---------------------------------------------------------------------------------------------------------------------------------------------------------
/* Stored Procedure
used to increase efficiency as it stores cache in memory and reduces communication with db.
/Delimiter
Default end point is ; so the contents within each ; are considered as blocks and sent to db individually but SP may use multiple queries each ending
with ; so sql treats each as individual blocks resulting in error so we use delimiter to change default end point from ; to some other symbol 
So before starting a procedure use DELIMITER $$ or any symbol and after completing SP code change it back to ;
*/
                                                       -- exercise - Bank Accounts
-- question link   https://drive.google.com/file/d/1wcy-7zjKhtDDAStQEo-MDhfuKoIqjBWY/view      
-- create and insert are already given in question
/*
1. Create a stored procedure named GetAllAccounts that displays all account records.

2. Create a procedure named GetSavingsAccounts that displays only customers having a
Savings account.

3. Create a procedure named GetAccountsByCity that accepts a city as an input parameter
and displays customers from that city.

Example expected usage:

CALL GetAccountsByCity('Hyderabad') ;

4. Create a procedure named GetAccountsAboveBalance that accepts a balance amount and
displays accounts having a balance greater than that value.

Example:

CALL GetAccountsAboveBalance (50000);

5. Create a procedure named UpdateAccountBalance that accepts:

o Account ID
o New Balance

The procedure should update the balance of that account.

6. Create a procedure named DepositAmount that accepts:

o Account ID
o Deposit Amount

The amount should be added to the existing balance, not replace it.

7. Create a procedure named WithdrawAmount that accepts:

o Account ID
o Withdrawal Amount

It should subtract the amount from the existing balance.

8. Create a procedure named DeleteAccount that accepts an Account ID and deletes that
account.
*/
CREATE DATABASE banking_db;

use banking_db;

CREATE TABLE accounts(
    account_id int PRIMARY KEY,
    customer_name VARCHAR(100),
    account_type VARCHAR(30),
    balance DECIMAL(10,2),
    city VARCHAR(50)
);

INSERT INTO accounts VALUES
(101, 'Arun Kumar', 'Savings', 45000, 'Hyderabad'),
(102, 'Meera Shah', 'Current', 85000, 'Mumbai'),
(103, 'Ravi Reddy', 'Savings', 32000, 'Hyderabad'),
(104, 'Priya Nair', 'Savings', 67000, 'Bangalore'),
(105, 'Sameer Khan', 'Current', 120000, 'Pune'),
(106, 'Neha Gupta', 'Savings', 28000, 'Delhi'),
(107, 'Vikram Rao', 'Current', 95000, 'Hyderabad'),
(108, 'Anjali Singh', 'Savings', 54000, 'Mumbai');

SELECT * FROM accounts;
-- the following method can be used for procedures using single query
CREATE PROCEDURE GetAllAccounts()
    SELECT * FROM accounts;

call GetAllAccounts();


CREATE PROCEDURE GetSavingsAccounts()
    SELECT * FROM accounts where account_type='Savings';

call GetSavingsAccounts();


CREATE PROCEDURE GetAccountsByCity(IN p_city VARCHAR(50))
    SELECT * 
    FROM accounts
    WHERE city = p_city;

CALL GetAccountsByCity('Hyderabad');


CREATE PROCEDURE GetAccountsAboveBalance(IN p_bal DECIMAL(10,2))
    SELECT * 
    FROM accounts
    WHERE balance > p_bal;

CALL GetAccountsAboveBalance(5000);


CREATE PROCEDURE UpdateAccountBalance(IN p_id int,p_bal DECIMAL(10,2))
    UPDATE accounts set balance=p_bal
    WHERE account_id = p_id;

CALL UpdateAccountBalance(101,50000);


CREATE PROCEDURE DepositAmount(IN p_id int,p_amount DECIMAL(10,2))
    UPDATE accounts set balance=(balance+p_amount)
    WHERE account_id = p_id;

CALL DepositAmount(101,50000);


CREATE PROCEDURE WithdrawAmount(IN p_id int,p_amount DECIMAL(10,2))
    UPDATE accounts set balance=(balance-p_amount)
    WHERE account_id = p_id;

CALL WithdrawAmount(101,50000);


CREATE PROCEDURE DeleteAccount(IN p_id int)
    DELETE FROM accounts 
    WHERE account_id = p_id;

CALL DeleteAccount(101);

truncate TABLE accounts; -- Removes all data without deleting table 

drop PROCEDURE DepositAmount; -- to remove a SP

-- the following are same queries but uses delimeter
-- run individually in new file or else like if run each  by selecting throws error
DELIMITER //
CREATE PROCEDURE GetAllAccount()
BEGIN
SELECT * FROM accounts;
END //
DELIMITER ;

CALL GetAllAccounts();


DELIMITER //
CREATE PROCEDURE GetSavings()
BEGIN
    SELECT * FROM accounts WHERE account_type='Savings';
END//
DELIMITER ;

call GetSavings();


DELIMITER //
CREATE PROCEDURE GetAccountsByCit(IN city_name VARCHAR(50))
BEGIN
    SELECT * FROM accounts WHERE city = sity_name;
END //
DELIMITER ;

CALL GetAccountsByCity('Hyderabad');


DELIMITER //
CREATE PROCEDURE GetAccountsAboveBalance(IN p_bal DECIMAL(10,2))
BEGIN
    SELECT * 
    FROM accounts
    WHERE balance > p_bal;
END//
DELIMITER ;

CALL GetAccountsAboveBalance(5000);


DELIMITER //
CREATE PROCEDURE UpdateAccountBalance(IN p_id int,p_bal DECIMAL(10,2))
BEGIN
    UPDATE accounts set balance=p_bal
    WHERE account_id = p_id;
END//
DELIMITER ;

CALL UpdateAccountBalance(101,5000);


DELIMITER //
CREATE PROCEDURE DepositAmount(IN p_id int,p_amount DECIMAL(10,2))
BEGIN
    UPDATE accounts set balance=(balance+p_amount)
    WHERE account_id = p_id;
END//
DELIMITER ;

CALL DepositAmount(101,5000);


DELIMITER //
CREATE PROCEDURE WithdrawAmount(IN p_id int,p_amount DECIMAL(10,2))
BEGIN
    UPDATE accounts set balance=(balance-p_amount)
    WHERE account_id = p_id;
END//
DELIMITER ;

CALL WithdrawAmount(101,5000);


DELIMITER //
CREATE PROCEDURE DeleteAccount(IN p_id int)
BEGIN
    DELETE FROM accounts 
    WHERE account_id = p_id;
END//
DELIMITER ;

CALL DeleteAccount(101);


-- ----------------------------------------------------------------------------------------------------------------------------------------------
-- class notes 
CREATE TABLE sales_orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    product_category VARCHAR(50),
    product_name VARCHAR(100),
    quantity INT,
    unit_price DECIMAL(10,2),
    salesperson VARCHAR(100),
    order_date DATE
);

INSERT INTO sales_orders VALUES
(1001, 'Amit Sharma', 'Hyderabad', 'Electronics', 'Laptop', 1, 55000, 'Rahul', '2026-01-05'),
(1002, 'Sara Khan', 'Mumbai', 'Electronics', 'Mobile', 2, 25000, 'Neha', '2026-01-06'),
(1003, 'Vikram Rao', 'Hyderabad', 'Furniture', 'Office Chair', 4, 7000, 'Rahul', '2026-01-07'),
(1004, 'Meera Nair', 'Bangalore', 'Electronics', 'Tablet', 3, 18000, 'Arjun', '2026-01-08'),
(1005, 'Ravi Kumar', 'Delhi', 'Furniture', 'Desk', 2, 15000, 'Neha', '2026-01-10'),
(1006, 'Fatima Ali', 'Hyderabad', 'Accessories', 'Keyboard', 5, 2500, 'Rahul', '2026-01-11'),
(1007, 'Arjun Mehta', 'Mumbai', 'Accessories', 'Mouse', 10, 1200, 'Arjun', '2026-01-12'),
(1008, 'Priya Singh', 'Bangalore', 'Electronics', 'Laptop', 2, 60000, 'Neha', '2026-01-15'),
(1009, 'Sameer Khan', 'Hyderabad', 'Furniture', 'Bookshelf', 3, 9000, 'Rahul', '2026-01-16'),
(1100, 'Anjali Verma', 'Delhi', 'Electronics', 'Mobile', 4, 22000, 'Arjun', '2026-01-18'),
(1101, 'Kiran Reddy', 'Hyderabad', 'Accessories', 'Headphones', 6, 3000, 'Neha', '2026-01-20'),
(1102, 'Sneha Patel', 'Mumbai', 'Furniture', 'Office Chair', 5, 7500, 'Rahul', '2026-01-21'),
(1103, 'Raj Malhotra', 'Delhi', 'Accessories', 'Keyboard', 8, 2800, 'Arjun', '2026-01-23'),
(1104, 'Nisha Gupta', 'Bangalore', 'Electronics', 'Monitor', 3, 16000, 'Neha', '2026-01-24'),
(1105, 'Imran Sheikh', 'Hyderabad', 'Electronics', 'Mobile', 3, 24000, 'Rahul', '2026-01-25'),
(1106, 'Pooja Rao', 'Mumbai', 'Furniture', 'Desk', 2, 14000, 'Arjun', '2026-01-26'),
(1107, 'Adil Khan', 'Delhi', 'Electronics', 'Laptop', 1, 58000, 'Neha', '2026-01-28'),
(1108, 'Kavya Reddy', 'Hyderabad', 'Accessories', 'Mouse', 7, 1500, 'Rahul', '2026-01-29'),
(1109, 'Mohit Jain', 'Bangalore', 'Furniture', 'Desk', 3, 15500, 'Arjun', '2026-01-30'),
(1200, 'Zoya Ahmed', 'Mumbai', 'Electronics', 'Monitor', 2, 17000, 'Neha', '2026-02-01');

SELECT * FROM sales_orders WHERE city='Hyderabad' AND unit_price>10000;  -- AND

SELECT * from sales_orders WHERE city IN ('Mumbai','Bangalore');  -- IN

SELECT sum(quantity*unit_price) as total_sales from sales_orders; -- SUM

SELECT COUNT(*) AS total_orders FROM sales_orders; -- COUNT

SELECT AVG(unit_price) AS average_price FROM sales_orders; -- AVG 

SELECT MAX(unit_price) as max_price FROM sales_orders;  -- MAX

SELECT MIN(unit_price) as min_price from sales_orders; -- MIN

SELECT city,sum(quantity*unit_price) as total_sales from sales_orders GROUP by city; -- sales in each city

SELECT salesperson,count(*) as total_sales from sales_orders group by salesperson; -- no of sales by each person

SELECT
city,
SUM(quantity * unit_price) AS total_sales       -- cities which sold Electronics greater than Rs.50K highest to lowest
FROM sales_orders
WHERE product_category = 'Electronics'
GROUP BY city
HAVING SUM(quantity * unit_price) > 50000  -- HAVING
ORDER BY total_sales DESC;

-- order of execution
-- 1. FROM --table
--  2. WHERE -- Electronics
-- 3. GROUP BY -- City
-- 4. HAVING -- another layer of filtering
-- 5. SELECT -- get the data
-- 6. ORDER BY -- Sorting

-- -----------------------------------------------------------------------------------------------------------------------------------------------------
-- joins -> To use related datas scattered across different tables and also to clean (left and right)
-- types -> left,right,inner,full(using union with left and right join) 
-- class notes
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(100),
    amount DECIMAL(10,2)
);

INSERT INTO customers VALUES
(1, 'Amit Sharma', 'Hyderabad'),
(2, 'Sara Khan', 'Mumbai'),
(3, 'Rahul Verma', 'Delhi'),
(4, 'Neha Singh', 'Bangalore'),
(5, 'Imran Ali', 'Hyderabad'),
(6, 'Priya Rao', 'Pune'),
(7, 'Arjun Mehta', NULL);

INSERT INTO orders VALUES
(1001, 1, 'Laptop', 55000),
(1002, 2, 'Mobile', 25000),
(1003, 1, 'Keyboard', 3000),
(1004, 3, 'Monitor', 18000),
(1005, 4, 'Laptop', 62000),
(1006, 2, 'Headphones', 5000),
(1007, 5, 'Tablet', 30000),

(1008, 10, 'Printer', 22000),
(1009, NULL, 'Mouse', 1500);
-- inner join
select c.customer_id,c.customer_name,o.order_id,o.product_name,o.amount from customers c inner join orders o on c.customer_id=o.customer_id;
-- left join
select c.customer_id,c.customer_name,c.city,o.order_id,o.product_name,o.amount from customers c left join orders o on c.customer_id=o.customer_id;
-- right join
select c.customer_id,c.customer_name,c.city,o.order_id,o.product_name,o.amount from customers c RIGHT join orders o on c.customer_id=o.customer_id;
-- customers who didnt placed any orders so that we can send offer mails to attract customers
select c.customer_id,c.customer_name from customers c left join orders o on c.customer_id=o.customer_id WHERE o.order_id is NULL;
-- products without customer which is bad data or noise
select o.customer_id,o.order_id,o.product_name,o.amount from customers c right join orders o on c.customer_id=o.customer_id where c.customer_id IS NULL;

-- -----------------------------------------------------------------------------------------------------------------------------------------------------------
-- Exercise Hospital Appointment Database
/* given all create and insert datas
This deliberately gives you:

. patients with no appointments,
. doctors with no appointments,
. an appointment with no patient,
. an appointment with an invalid patient ID,
. an appointment with no doctor,
· actual NULL data.

Exercises

1. Display appointment ID, patient name, doctor name and appointment date.

2. Show the doctor and specialization for every completed appointment.

3. Find all appointments made by patients from Hyderabad.

4. Display every patient and their appointment details. Patients who have never booked an
appointment must also appear.

5. Find patients who have never booked an appointment.

6. Display every doctor and appointments handled by them, including doctors who have never
handled an appointment.

7. Find doctors who currently have no appointments.

8. Identify appointment records for which a valid patient cannot be found.

9. Identify appointment records for which a doctor has not been assigned.

10. Display:

Patient Name
Doctor Name
Specialization
Consultation Fee
Appointment Status

for all valid appointments.
11. Find the number of appointments handled by each doctor.

12. Find the total consultation value generated by each doctor based on completed appointments
only

13. Find doctors who have handled more than one appointment.

14. Find the specialization generating the highest total consultation value.

15. Display each patient and the number of appointments they have booked, including patients with
zero appointments.

16. Find patients who have consulted more than one doctor.

17. Find patients who have visited a Cardiology doctor.

18. Display appointments where the consultation fee is greater than ₹900.

19. Find the average consultation fee of doctors involved in completed appointments.

20. Display the doctor who has handled the highest number of completed appointments.
*/
CREATE DATABASE hospital_lab;
USE hospital_lab;

CREATE TABLE patients (
patient_id INT PRIMARY KEY,
patient_name VARCHAR(100),
age INT,
city VARCHAR(50)
);
INSERT INTO patients VALUES
(1, 'Rohan Das', 34, 'Hyderabad'),
(2, 'Meena Iyer', 46, 'Chennai'),
(3, 'Kabir Khan', 29, 'Hyderabad'),
(4, 'Lakshmi Rao', 61, 'Bangalore'),
(5, 'John Mathew', 38, 'Mumbai'),
(6, 'Ayesha Ali', 25, NULL),
(7, 'Naveen Reddy', 52, 'Pune');

CREATE TABLE doctors (
doctor_id INT PRIMARY KEY,
doctor_name VARCHAR(100),
specialization VARCHAR(50),
consultation_fee DECIMAL(10,2)
);
INSERT INTO doctors VALUES
(101, 'Dr. Sharma', 'Cardiology', 1200),
(102, 'Dr. Farah', 'Dermatology', 800),
(103, 'Dr. Joseph', 'Orthopedics', 1000),
(104, 'Dr. Mehta', 'General Medicine', 600),

(105, 'Dr. Sana', 'Neurology', 1500),
(106, 'Dr. Rao', 'Pediatrics', 700);

CREATE TABLE appointments (
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
status VARCHAR(30)
);
INSERT INTO appointments VALUES
(1001, 1, 101, '2026-10-01', 'Completed'),
(1002, 2, 104, '2026-10-01', 'Completed'),
(1003, 3, 102, '2026-10-02', 'Cancelled'),
(1004, 1, 105, '2026-10-03', 'Completed'),
(1005, 4, 101, '2026-10-03', 'Scheduled'),
(1006, 5, 103, '2026-10-04', 'Completed'),
(1007, 3, 104, '2026-10-04', 'Completed'),
(1008, NULL, 102, '2026-10-05', 'Scheduled'),
(1009, 20, 103, '2026-10-05', 'Completed'),
(1010, 2, NULL, '2026-10-06', 'Scheduled');

select a.appointment_id,d.doctor_name,p.patient_name,a.appointment_date
from appointments a 
INNER JOIN doctors d ON a.doctor_id=d.doctor_id 
INNER JOIN patients p ON a.patient_id= p.patient_id;

select d.doctor_name,d.specialization from appointments a inner join doctors d on a.doctor_id=d.doctor_id where a.status='Completed';

SELECT p.patient_id,p.patient_name,p.city,p.age from appointments a INNER join patients p on a.patient_id=p.patient_id where p.city='Hyderabad';

SELECT * from appointments a Right join patients p on a.patient_id=p.patient_id;

SELECT p.patient_id,p.patient_name from appointments a Right join patients p on a.patient_id=p.patient_id where a.appointment_id is NULL;

SELECT * from appointments a Right join doctors d on a.doctor_id=d.doctor_id;

SELECT * from appointments a Right join doctors d on a.doctor_id=d.doctor_id where a.appointment_id is NULL ;

SELECT a.patient_id,a.appointment_id,a.doctor_id,a.appointment_date,a.status from appointments a LEFT join patients p on a.patient_id=p.patient_id WHERE p.patient_id is NULL;

SELECT a.patient_id,a.appointment_id,a.doctor_id,a.appointment_date,a.status from appointments a LEFT join doctors d on a.doctor_id=d.doctor_id WHERE d.doctor_id is NULL;

SELECT p.patient_name,d.doctor_name,d.specialization,d.consultation_fee,a.status from appointments a
INNER JOIN patients p on p.patient_id=a.patient_id
INNER JOIN doctors d on d.doctor_id = a.doctor_id ;

SELECT d.doctor_name,count(a.appointment_id) from appointments a RIGHT join doctors d on a.doctor_id = d.doctor_id group by a.doctor_id;

SELECT d.doctor_name,sum(d.consultation_fee) from doctors d INNER JOIN appointments a on a.doctor_id = d.doctor_id where a.status='Completed' GROUP by d.doctor_id,d.doctor_name;

SELECT d.doctor_name from doctors d INNER JOIN appointments a on a.doctor_id = d.doctor_id GROUP by d.doctor_id,d.doctor_name HAVING COUNT(a.appointment_id)>1;

SELECT d.specialization,sum(d.consultation_fee) as total from doctors d INNER JOIN appointments a on a.doctor_id = d.doctor_id where a.status='Completed' GROUP by d.specialization ORDER BY total desc limit 1;

select p.patient_name,count(a.appointment_id) from patients p left join appointments a on p.patient_id=a.patient_id group by p.patient_id,p.patient_name;

select p.patient_name from patients p INNER join appointments a on p.patient_id=a.patient_id group by p.patient_id,p.patient_name having COUNT(distinct a.doctor_id)>1;

SELECT distinct p.patient_name from appointments a
INNER JOIN patients p on p.patient_id=a.patient_id
INNER JOIN doctors d on d.doctor_id = a.doctor_id where d.specialization ='Cardiology';

SELECT a.patient_id,a.appointment_id,a.doctor_id,a.appointment_date,a.status from appointments a INNER join doctors d on a.doctor_id=d.doctor_id where (d.consultation_fee)>900;

SELECT AVG(d.consultation_fee) as avg_fee from appointments a inner join doctors d on a.doctor_id=d.doctor_id where a.status='Completed';

select d.doctor_name,COUNT(a.appointment_id) AS completed_appointments from appointments a inner join doctors d on a.doctor_id=d.doctor_id where a.status='Completed' GROUP BY a.doctor_id,d.doctor_name ORDER BY completed_appointments DESC
LIMIT 1;
