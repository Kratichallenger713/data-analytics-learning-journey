select * from sales_data
-- where & and 
select * from sales_data where address='Mumbai' 
and category='Electronics'

select * from sales_data where address='Mumbai' 
or category='Electronics'

select *from sales_data where price between 100 and 800
-- in used to check the multiple details
select product_name,price from sales_data where address in ('Mumbai','Noida')

-- like 
select * from sales_data where customer_name like 'r%'

select * from sales_data where customer_name ILIKE 'r%'

select *from sales_data where address is 'null'

select *from sales_data where address is not null

select * from sales_data

select * from sales_data order by price desc

select * from sales_data limit 3
-- offset means skip the offset no. of records
select * from saleS_data  limit 2 offset 3

select * from sales_data where price >1000

select * from sales_data where address='Mumbai' order by price desc limit 1

select * from sales_data where address='Mumbai' order by price desc limit 1 offset 1

select * from sales_data  order by price limit 3 

select * from saleS_data order by price asc

select * from sales_data order by sale_id desc


select * from sales_data order by sale_id desc limit 3

select * from sales_data order by sale_id desc limit 1

select address,price from sales_data order by address asc ,price desc

select * from sales_data order by email nulls first

select * from sales_data order by email nulls last

select price from sales_data order by price nulls last

select * from sales_data fetch first 5 rows only

select * from sales_data order by quantity*price desc limit 5

select product_name from sales_data order by price asc limit 4

select product_name, price from sales_data  order by price desc limit 5

select product_name, price from sales_data  order by price asc limit 5

select count(*) from sales_data

select count(customer_name) from sales_data

select count(distinct address) from sales_data

select sum(price) from sales_data

select sum(quantity*price) as total_revenue from sales_data

select avg(price) as average_price from sales_data

select min(price) as minimum_price from sales_data

select max(price) as maximum_price from sales_data