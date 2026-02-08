# 📝 To-Do List

A simple Python console application to manage daily tasks.

In this program, the user can view saved tasks, add new ones with deadlines, and complete tasks. All data is stored in a file so the tasks remain available even after the program is closed.



## Features

- View all saved tasks
- Add a new task with a deadline
- Complete (remove) a task
- Automatically generated unique task IDs (UUID)
- Data persistence using a text file
- Basic input and file error handling
- Built with Python (standard library only)


## Concepts Practiced

- functions
- loops and conditional statements
- user input handling
- string manipulation
- lists
- file handling (`read`, `write`, `append`)
- exception handling (`try/except`)
- using modules (`uuid`)



## Requirements

Python 3.x  


## Additional info

There is minor difference between assignment and solution, for the solution I've choose use counter of the tasks instead of UUID (the UUID solution is still commented in the code). And also the design of the table is slightly adjusted.


## How to Run Locally

1. Clone the repository:
```
git clone https://github.com/lucienadvornik/to_do_list
```
2. Navigate into the project folder:
```
cd to_do_list
```
3. Run the program:
```
python3 main.py
```
