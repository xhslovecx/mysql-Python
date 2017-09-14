drop table if exists mysqldb.woman;
create table woman(
id int(4) not null
,name char(30)
,sex char(2)
,age int(4)
,high int(6)
,salary int(12)
,vocation char(30)
,primary key(id)
);
insert into mysqldb.woman values(id=100,name='xhs')
;
select * from mysqldb.woman