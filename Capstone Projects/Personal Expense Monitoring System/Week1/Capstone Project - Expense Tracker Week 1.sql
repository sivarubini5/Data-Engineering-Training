CREATE DATABASE IF NOT EXISTS expense_tracker;
USE expense_tracker;
CREATE TABLE users(
    user_id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE categories(
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE expenses(
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    expense_date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) 
);

INSERT INTO users (name,email) VALUES('Arun','arun@gmail.com'),('Priya','priya@gmail.com');
INSERT INTO categories (category_name) VALUES('Food'),('Transport'),('Rent'),('Utilities'),('Entertainment');
INSERT INTO expenses(user_id,category_id,amount,expense_date,description) VALUES
(1, 1, 450.00,   '2026-09-03', 'Groceries'),
(1, 2, 120.00,   '2026-09-05', 'Metro card recharge'),
(1, 3, 12000.00, '2026-09-01', 'Monthly rent'),
(1, 1, 300.50,   '2026-09-12', 'Restaurant dinner'),
(2, 4, 1800.00,  '2026-09-07', 'Electricity bill'),
(2, 5, 600.00,   '2026-09-15', 'Movie tickets');

SELECT e.expense_id,u.name,c.category_name,e.amount,e.expense_date,e.description from expenses e
inner join users u on e.user_id=u.user_id
inner join categories c on e.category_id=c.category_id where e.user_id =1 order by e.expense_date;

UPDATE expenses SET amount=480.00,description="Groceries(updated)" WHERE expense_id=1;

DELETE FROM expenses WHERE expense_id=2;

DELIMITER //
CREATE PROCEDURE sp_monthly_category_total(in p_user_id int, in p_year int,in p_month int)
BEGIN
    SELECT c.category_name,sum(e.amount) as total_expense from expenses e
    inner join categories c on e.category_id=c.category_id where e.user_id=p_user_id and 
    year(e.expense_date)=p_year and month(e.expense_date)=p_month group by c.category_name order by total_expense desc;
END //
DELIMITER ;

CALL sp_monthly_category_total(1,2026,9);

DROP PROCEDURE sp_monthly_category_total;
