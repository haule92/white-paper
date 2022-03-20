
- create backup database mysql using MariaDB

```sh
sudo mysqldump --single-transaction --quick --lock-tables=false [name_of_database] > /path/where/save/full-backup-$(date +\%F).sql
mysqldump --single-transaction --quick --lock-tables=false [name_of_database] > /path/where/save/full-backup-$(date +\%F).sql
```

```sh
sudo mysql -u [user] -p [database_name] < [filename].sql
mysql -u [user] -p [database_name] < [filename].sql
```
