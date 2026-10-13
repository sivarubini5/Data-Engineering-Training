CREATE DATABASE expense_monitoring;
use expense_monitoring;

CREATE TABLE users(
    user_id int primary key AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    monthly_income DECIMAL(10,2) NOT NULL DEFAULT 0,
    monthly_budget DECIMAL(10,2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories(
    category_id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) not NULL UNIQUE
);

CREATE TABLE expenses(
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(10,2) not null CHECK(amount>0),
    expense_date DATE NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
    CONSTRAINT fk_exp_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT fk_exp_cat  FOREIGN KEY (category_id) REFERENCES categories(category_id),
    INDEX idx_user_date (user_id, expense_date),
    INDEX idx_category (category_id) 
);
drop TABLE expenses;
INSERT INTO users (name, email, monthly_income, monthly_budget) VALUES
 ('Asha Raman', 'asha@example.com', 60000, 40000),
 ('Vikram Das', 'vikram@example.com', 80000, 55000);

INSERT INTO categories (name) VALUES
 ('Food'), ('Rent'), ('Transport'), ('Utilities'), ('Entertainment'), ('Health'), ('Shopping');

-- CREATE
INSERT INTO expenses (user_id, category_id, amount, expense_date, description) VALUES
 (1, 1, 1250.50, '2026-09-03', 'Groceries'),
 (1, 2, 15000.00, '2026-09-01', 'September rent'),
 (1, 3, 600.00, '2026-09-05', 'Fuel'),
 (1, 5, 899.00, '2026-09-12', 'Streaming + movie'),
 (2, 1, 2100.00, '2026-09-04', 'Restaurant & groceries'),
 (2, 7, 7800.00, '2026-09-15', 'Headphones');

SELECT e.expense_id, u.name, c.name AS category, e.amount, e.expense_date, e.description
FROM expenses e
JOIN users u ON u.user_id = e.user_id
JOIN categories c ON c.category_id = e.category_id
WHERE e.user_id = 1
ORDER BY e.expense_date DESC;

UPDATE expenses
SET amount = 1300.00, description = 'Groceries (corrected)'
WHERE expense_id = 1;

DELETE FROM expenses WHERE expense_id = 4;

delimiter //
CREATE PROCEDURE monthly_total_per_category(in p_user_id int,in p_year int,in p_month int)
BEGIN
    SELECT c.name as category,
    count(*) as num_of_transactions,
    SUM(e.amount) as total 
    from expenses e
    inner join categories c on c.category_id=e.category_id
    where e.user_id=p_user_id and YEAR(e.expense_date)=p_year and MONTH(e.expense_date)=p_month
    GROUP by c.name
    ORDER BY total desc;
END//
delimiter ;
call monthly_total_per_category(1,2026,9);
