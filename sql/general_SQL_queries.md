#### SQL queries

- Change a value of a certain column and match certain id.
```sql
update table_name set column_name = 'something' where custom_id = 1; 
```

- Delete row matching custom_id. Or more than row second line.
```sql
delete from table_name where custom_id = 1;
delete from table_name where custom_id in (1,2,3);
```

- 

- Create a sql user and the connection to the database. The credentials are username, password and the ip of the machine which you want to connect to the database. The id could be 'localhost' if the user want to be created is in the same machine that the database.
```sql
create user 'username'@'127.0.0.0' identified by 'password';
```

- Grant all the privileges to the user in a database.
```sql
grant all on database_name.* to 'username'@'127.0.0.0' identified by 'password' with grant option;
flush privileges;
```

- Count numer of rows a table have.
```sql
select count (*) from table_name;
```

- Rename host(ip) and user(name) already existing.
```sql
rename user 'jeffrey'@'localhost' TO 'jeff'@'127.0.0.1';
```

- Create backup database mysql (using MariaDB)
```sql

```