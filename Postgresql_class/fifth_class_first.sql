select * from sales_data
-- where & and 
select * from sales_data where address='Mumbai' 
and category='Electronics'

select * from sales_data where address='Mumbai' 
or category='Electronics'

select *from sales_data where price between 100 and 800
-- in used to check the
select product_name,price from sales_data where address in ('Mumbai','Noida')

select * from sales_data

select sum(quantity*price) as total_sales from sales_data where address='Mumbai'

select avg(price) as average_price from sales_data where category ='Electronics'

select count(*) as total_sales from sales_data where address='Mumbai'

-- Multiple aggregation

SELECT
    COUNT(*) AS total_orders,
    SUM(quantity * price) AS total_revenue,
    AVG(price) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM sales_data;

select sum(quantity*price) as total_revenue from sales_data 

select avg(price) as average_price from sales_data

select max(price) as highest_price from sales_data

select min(price) as minimum_price from sales_data

-- Groupby and having 
select address, count(*) as total_sales from sales_data group by address

select category ,sum(quantity*price) as total_revenue from sales_data group by category

select address ,sum(quantity*price) as total_revenue from sales_data group by address

select product_name ,sum(quantity) as total_quantity from sales_data group by product_name

select address,category ,sum(quantity*price) as total_quantity from sales_data group by 
address, category

-- having is used to filter the group result
-- it's work like where but we use where to filter rows and having to filter group by results

select address,sum(quantity*price) as total_quantity from sales_data group by 
address
having sum(quantity*price)>3000
-- where v/s having 
-- where gorping se pehle rows filter karta hai 
select address,sum(quantity*price) as total_quantity from sales_data 
where price >1000
group by 
address
SELECT address,
	SUM(quantity * price) AS total_revenue
FROM sales_data
WHERE price > 1000
GROUP BY address
HAVING SUM(quantity * price) > 500
ORDER BY total_revenue DESC;



































