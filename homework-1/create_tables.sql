-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(32) NOT NULL,
	last_name varchar(32)NOT NULL,
	title varchar(64),
	birth_date date,
	note text
);

CREATE TABLE customers
(
	customer_id varchar(32) PRIMARY KEY,
	company_name varchar(64),
	contact_name varchar(64)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(64)
);
