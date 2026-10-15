select * from sales

alter table sales_data
add column salary int 

alter table sales_data
alter column salary type numeric(10,2)

alter table sales_data rename column city to address

alter table sales_data
add column employee varchar(50)

alter table sales_data
alter column employee type int
using employee::int

alter table sales_data
alter column address set default 'gwalior'

alter table sales_data 
alter column address drop default

alter table sales rename to sales_data

alter table sales_data 
alter column customer_name set not null

alter table sales_data
alter column customer_name drop not null

select * from sales_data

alter table sales_data 
add constraint salary_check
check(salary>0)

alter table sales_data 
drop constraint salary_check

-- alter table sales_data 
-- add primary key (sale_id)

-- alter table sales_data 
-- drop constraint sales_pkey

INSERT INTO sales_data(customer_name, product_name, category, quantity, price, sale_date, address, is_online)
VALUES
('parul', 'Mouse', 'Electronics', 2, 700, '2026-03-02','Noida' , TRUE)

alter table sales_data 
add column email varchar(50)

alter table sales_data
add constraint unique_customer_email
unique(email)

alter table sales_data
drop column salary

alter table sales_data
drop column employee

INSERT INTO sales_data(customer_name, product_name, category, quantity, price, sale_date, address, is_online, email)
VALUES
('parul', 'Mouse', 'Electronics', 2, 700, '2026-03-02','Noida' , TRUE, 'bkratika@gmail.com')

INSERT INTO sales_data(customer_name, product_name, category, quantity, price, sale_date, address, is_online)
VALUES
('parul', 'Mouse', 'Electronics', 2, 700, '2026-03-02','Noida' , TRUE)

alter table sales_data
add constraint fk_customer
foreign key (customer_id)
references customers(customer_id)


select * from sales_data 

