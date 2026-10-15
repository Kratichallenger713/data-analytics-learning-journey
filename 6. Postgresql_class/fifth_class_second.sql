CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary NUMERIC(10,2),
    department_id INT
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO employees
    (emp_id, emp_name, salary, department_id)
VALUES
    (1, 'Rahul', 50000, 101),
    (2, 'Amit', 40000, 102),
    (3, 'Priya', 60000, 101),
    (4, 'Neha', 35000, 103),
    (5, 'Mohan', 30000, NULL);

INSERT INTO departments
    (department_id, department_name)
VALUES
    (101, 'IT'),
    (102, 'HR'),
    (104, 'Sales');
	
select * from employees,departments

select * from departments

SELECT
    e.emp_name,
    e.salary,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id;


SELECT
    e.emp_name,
    e.salary,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id;

SELECT
    e.emp_name,
    e.salary,
    d.department_name
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.department_id;

SELECT
    e.emp_name,
    e.salary,
    d.department_name
FROM employees e
FULL OUTER JOIN departments d
    ON e.department_id = d.department_id;

SELECT
    e.emp_name,
    d.department_name
FROM employees e
CROSS JOIN departments d;










	