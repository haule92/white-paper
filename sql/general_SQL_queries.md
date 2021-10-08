#### SQL queries

- Change a value of a certain column and match certain id.
```sql
update table_name set column_name = 'something' where custom_id = 1; 
```

- Delete row matching custom_id.
```sql
delete from table_name where custom_id = 1; 
```

- Create a sql user and the connection to the database. The credentials are username, password and the ip of the machine which you want to connect to the database. The id could be 'localhost' if the user want to be created is in the same machine that the database.
```sql
create user 'username'@'127.0.0.0' identified by 'password';
```

- Grant all the privileges to the user in a database.
```sql
grant all on database_name.* to 'username'@'127.0.0.0' identified by 'password' with grant option;
```
```sql
flush privileges;
```

- Count numer of rows a table have.
```sql
select count (*) from table_name;
```
