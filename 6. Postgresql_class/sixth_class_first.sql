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

alter table employees add column manager_id int 

select * from employees

UPDATE employees
SET manager_id = CASE emp_id
    WHEN 2 THEN 1
    WHEN 3 THEN 1
    WHEN 4 THEN 2
    WHEN 5 THEN 2
    ELSE NULL
END;

SELECT
    e.emp_name AS employee_name,
    m.emp_name AS manager_name
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.emp_id;

-- used where , order clause with join

SELECT
    e.emp_name,
    e.salary,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id
WHERE d.department_name = 'IT';


SELECT
    e.emp_name,
    e.salary,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id
ORDER BY e.salary DESC;

-- department wise total salary 
SELECT
    d.department_name,
    SUM(e.salary) AS total_salary
FROM departments d
INNER JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC;

SELECT
    e.emp_id,
    e.emp_name,
    e.department_id
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
-- jis department employees nahi hai 
SELECT
    d.department_id,
    d.department_name
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
WHERE e.emp_id IS NULL;

-- department wise employee salary and average count
SELECT
    d.department_name,
    COUNT(e.emp_id) AS employee_count,
    AVG(e.salary) AS avg_salary,
    SUM(e.salary) AS total_salary
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY total_salary DESC NULLS LAST;

-- self join 
SELECT
    e.emp_name AS employee,
    m.emp_name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.emp_id;























	