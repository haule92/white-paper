###### LINUX TERMINAL
To run dashboard on background. In this example the script is called 'filename'.
First make python path available to be able to run the script through terminal. The path after the equal will be the absolute path where is stored the project or repo. Basically the root from where all the dependencies are inside.
```sh
export PYTHONPATH=/home/path/is/name_of_the_repo
```
or
```sh
export PYTHONPATH=$PYTHONPATH:/home/ubuntuc/src/
```
I am not sure about the difference between the two.

Move inside the directory where the script is located to create the sh files to run/kill it.
Create a sh file through nano to run the python script
```sh
nano run_name.sh
```
Inside the editor (nano), write:
```nano
nohup python3 filename.py &
```
Press 'ctrl+x' to exit, 'y' to save and enter key.
&nbsp;
Create a sh file through nano to kill the python script
```sh
nano kill_name.sh
```
Inside the editor (nano), write:
```nano
pkill -f 'python3 filename.py'
```
Press 'ctrl+x' to exit, 'y' to save and enter key.
&nbsp;
To make the files executables using ./ in the terminal:
```sh
chmod +x run_name.sh
chmod +x kill_name.sh
```
Being in the same directory where the script is located, it can be run and stop using:
```sh
./run_name.sh
./kill_name.sh
```
