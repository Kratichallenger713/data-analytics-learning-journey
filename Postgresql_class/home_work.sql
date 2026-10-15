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

INSERT INTO sales(customer_name, product_name, category, quantity, price, sale_date, city, is_online)
VALUES
('Aman', 'Mouse', 'Electronics', 2, 800, '2026-08-02', 'Delhi', TRUE),
('Priya', 'Keyboard', 'Electronics', 1, 1500, '2026-08-03', 'Bhopal', FALSE),
('Neha', 'Chair', 'Furniture', 2, 5000, '2026-08-04', 'Indore', TRUE),
('pavan', 'Mouse', 'Electronics', 1, 700, '2026-03-02', 'Delhi', TRUE),
('riya', 'Keyboard', 'Electronics', 2, 500, '2026-07-03', 'Nagpur', FALSE),
('nia', 'Chair', 'Furniture', 5, 2000, '2026-02-04', 'Noida', TRUE);

-- sales table ka saara data display karo.
select * from sales

-- Sirf customer name aur product name display karo.
select customer_name, product_name from sales

-- Product name aur price display karo
select product_name, price from sales

-- Unique cities display karo.
select distinct city from sales

-- Unique categories display karo.
select distinct category from sales

-- quantity * price se total sales calculate karo.
select quantity, price,quantity*price as total_sales from sales

--  Customer_Name column ka alias Customer rakho.
select customer_name as Customer from sales

-- Price column ka alias Product_Price rakho.
select price as product_price from sales

-- Ek new sale insert karo.
insert into sales(customer_name, product_name, category, quantity, price, sale_date, city, is_online)
values('dharshan', 'Mouse', 'Electronics', 2, 900, '2026-05-23', 'Mumbai', TRUE);

-- Ek saath 3 sales insert karo.
insert into sales(customer_name, product_name, category, quantity, price, sale_date, city, is_online)
values
('Arpit', 'Mouse', 'Electronics', 2, 900, '2026-05-24', 'Mumbai', TRUE),
('Prem', 'Chair', 'Furniture', 2, 750, '2026-05-23', 'Delhi', TRUE),
('Krish', 'Mouse', 'Electronics', 1, 800, '2026-05-23', 'Noida', TRUE);

-- Kisi ek sale ki price update karo.
update sales set price=300 where sale_id=4

-- Kisi ek customer ka city update karo.
update sales set city='Kanpur' where sale_id=2

-- Kisi ek record ko delete karo.
delete from sales where sale_id=3

-- Har sale ka total revenue calculate karo.
select quantity*price as total_revenue from sales

-- Customer, product aur total revenue ek saath display karo.
select customer_name, product_name , quantity*price as total_revenue from sales

-- Unique cities ki list nikalo.
select distinct city from sales

-- Unique product categories nikalo.
select distinct category from sales

-- Sabhi products ki quantity aur price ke saath total value calculate karo.
select quantity, price, quantity*price as total_value from sales