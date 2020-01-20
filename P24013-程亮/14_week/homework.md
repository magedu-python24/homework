#### 写出以下操作的sql语句：

##### 1、创建一个叫users的表包含username、age、sex字段

```mysql
# 创建了一个数据库进行操作 CREATE DATABASE customers;
CREATE TABLE users (id INT AUTO_INCREMENT, username CHAR(10), age INT(3), sex enum('F','M'), PRIMARY KEY (id));
```

##### 2、查询username为“张三”的一条纪录

```mysql
select * from users where username='张三';
```

##### 3、查询age大于18且sex为“女“的所有纪录

```mysql
select * from users where age > 18 and sex = 'F';
```

##### 如何备份并还原上述表？

备份

```shell
mysqldump --single-transaction customers users > users.sql
```

还原

```shell
# 删除原来的表 drop table users; 还原时指定数据库，如果没有就需要create database 去创建
mysql customers < users.sql
```

