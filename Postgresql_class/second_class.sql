create table sales(
sale_id  serial primary key,
customer_name varchar(100),
product_name varchar(100),
category varchar(50),
quantity int,
price numeric(10,2),
sale_date date,
city varchar(50),
is_online boolean
)

select * from sales

INSERT INTO sales(customer_name, product_name, category, quantity, price, sale_date, city, is_online)
VALUES
('Aman', 'Mouse', 'Electronics', 2, 800, '2026-08-02', 'Delhi', TRUE),
('Priya', 'Keyboard', 'Electronics', 1, 1500, '2026-08-03', 'Bhopal', FALSE),
('Neha', 'Chair', 'Furniture', 2, 5000, '2026-08-04', 'Indore', TRUE);

select customer_name,product_name, price from sales
-- as means alias 
select customer_name as customer from sales

select s.customer_name,s.product_name from sales  as s
-- it shows only unique value
select distinct city,category from sales

select distinct city from sales

select distinct category from sales

select product_name , quantity, price, 
quantity*price as total_sales from sales 

update sales set city='delhi',is_online=True where sale_id=1

delete from sales where sale_id=1


INSERT INTO sales(customer_name, product_name, category, quantity, price, sale_date, city, is_online)
VALUES
('pavan', 'Mouse', 'Electronics', 1, 700, '2026-08-02', 'Delhi', TRUE),
('riya', 'Keyboard', 'Electronics', 2, 500, '2026-08-03', 'Nagpur', FALSE),
('nia', 'Chair', 'Furniture', 5, 2000, '2026-08-04', 'Noida', TRUE);

truncate table sales  
-- delete table
-- drop table sales
-- delete database
-- drop database pnsales
-- used to change the structure of the table 
alter table sales add column discount numeric(5,2) 

alter table sales drop column discount

alter table sales rename column city to address

alter table sales rename to sales_data

select * from sales_data








