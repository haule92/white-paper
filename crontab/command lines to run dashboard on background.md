###### CRONTAB

Example to execute a bash shell file through crontab. The >> /path/order_log.log 2>&1, serves the purpose of creating a log file to store what we can see in the python console.
```sh
* * * * * /home/ubuntu/bash_shell_files/update_db_with_executed_trades/./run_update_db.sh >> /home/ubuntu/order_log.log 2>&1
```

To execute a python script. One way of doing it is creating a sh file and run it with crontab.
First in the sh file we write the pythonpath and the location of the script we want to run.
```sh
export PYTHONPATH=$PYTHONPATH:/home/ubuntu/code_repository/flexnow_bbg
python3 /home/ubuntu/code_repository/flexnow_bbg/wherver/inside/path/filename.py
```