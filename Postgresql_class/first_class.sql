CREATE TABLE student(
id serial primary key,
name varchar(100),
city varchar(50)
)
SELECT *FROM student
insert into student(name,city)values('Ram','gwalior')
insert into student(name,city)
values
('Ram','gwalior'),
('Shyam','bhopal'),
('vish','indore'),
('karan','mumbai')

select name from student
select name,city from student
select * from student where id=1
select * from student  where  city='gwalior'

update student set city='delhi' where id=1
update student set city='delhi',name='kiran' where id=1
update student set name ='rahul' where city='gwalior'
delete from student where id=1
-- used to delete the records of the table 
truncate table student 
-- delete the table 
drop table student

CREATE TABLE teacher(
id serial primary key,
name varchar(50),
city varchar(50),
address varchar(50)
)

select * from teacher
insert into teacher(name,city,address)
values
('riya','gwalior','thatipur'),
('arpit','gwalior','gola ka mandir'),
('kratika','mumbai','jyoti Apartment'),
('Diya','kanpur','ritambar')

select name from teacher
select city from teacher

update teacher set name='komal' where id=1
delete from teacher where id=4
truncate table teacher
drop table teacher
