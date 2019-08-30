-- create table
--Import each CSV file into the corresponding SQL table.

Drop Table if exists departements;
create Table departements (
	dept_no varchar,
	dept_name VARCHAR
);
-- Check data import
SELECT *
FROM departements;

Drop table if exists dept_emp;
create table dept_emp(
	emp_no int,
	dept_no varchar,
	from_date date,
	to_date date
);
-- Check data import
SELECT *
FROM dept_emp;

Drop table if exists dept_manager;
create table dept_manager(
	dept_no varchar,
	emp_no int,
	from_date date,
	to_date date
);
-- Check data import
SELECT *
FROM dept_manager;

Drop table if exists employees;
create table employees(
	emp_no int,
	birth_date date,
	first_name varchar,
    last_name varchar,
	gender varchar,
	hire_date date
);
--  check data import
SELECT *
FROM employees;

Drop table if exists salaries;
create table salaries(
	emp_no int,
	salary int,
	from_date date,
	to_date date
);
-- check data import
SELECT *
FROM salaries;

Drop table if exists titles;
create table titles(
	emp_no int,
	title varchar,
	from_date date,
	to_date date
);
-- check data import
SELECT *
FROM titles;
