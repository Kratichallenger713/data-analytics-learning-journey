-- date and time function 
select current_date

-- Current Date & Time
SELECT CURRENT_TIMESTAMP;

-- To Extract year from the date 
SELECT
    sale_date,
    EXTRACT(YEAR FROM sale_date) AS year
FROM sales_data;

-- To Extract month from date 
SELECT  
     sale_date,
	 EXTRACT(MONTH FROM sale_date) AS MONTH
FROM sales_data;		

-- To Extract day from date 
SELECT 
     sale_date,
	 EXTRACT(DAY FROM sale_date) AS DAY
FROM sales_data;

-- Year-Month Analysis 
SELECT
    DATE_TRUNC('month', sale_date) AS month,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month;

-- Year-wise Revenue
SELECT
    EXTRACT(YEAR FROM sale_date) AS year,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY EXTRACT(YEAR FROM sale_date)
ORDER BY year;

-- Month-wise Revenue
SELECT
    EXTRACT(MONTH FROM sale_date) AS month,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY EXTRACT(MONTH FROM sale_date)
ORDER BY month;

-- Date Range
SELECT *
FROM sales_data
WHERE sale_date BETWEEN '2026-08-01' AND '2026-08-15'

-- Specific Year ki Sales
SELECT *
FROM sales_data
WHERE EXTRACT(YEAR FROM sale_date) = 2026;

-- Last 7 Days
SELECT *
FROM sales_data
WHERE sale_date >= CURRENT_DATE - INTERVAL '7 days';

-- Date mein Days Add Karna
SELECT
    sale_date,
    sale_date + INTERVAL '7 days' AS next_week
FROM sales_data

-- Date Difference
SELECT
    CURRENT_DATE - sale_date AS days_ago
FROM sales_data;

-- Day of Week

SELECT
    sale_date,
    TO_CHAR(sale_date, 'Day') AS day_name
FROM sales_data;

-- Month-wise total revenue:
SELECT
    DATE_TRUNC('month', sale_date) AS month,
    SUM(quantity * price) AS total_revenue
FROM sales_data
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month


-- Last 30 Days Sales:
SELECT *
FROM sales_data
WHERE sale_date >= CURRENT_DATE - INTERVAL '30 days';

-- 2026 ki Sales:
SELECT *
FROM sales_data
WHERE EXTRACT(YEAR FROM sale_date) = 2026;















