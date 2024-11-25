# CodSoft_TO.DO.LIST_01
To-Do List Application (GUI)

This is a simple To-Do List Application built using Python and Tkinter. The application allows users to create, update, delete, and track their tasks in a friendly graphical user interface (GUI). Tasks are saved in a JSON file, ensuring persistence between application sessions.

# Features
Add Tasks: Users can add tasks with descriptions and deadlines.
Update Tasks: Users can change the status of tasks (e.g., "Pending" or "Completed").
Delete Tasks: Users can delete tasks from their to-do list.
View Tasks: Users can view all tasks with their description, deadline, and status.

# Persistence: 
All tasks are saved to a tasks.json file, ensuring the data persists between sessions.

# Requirements
Python: Version 3.x or higher
Tkinter: Tkinter comes pre-installed with Python. If it's missing, it can be installed separately.

# Installation
Install Python:

Make sure Python 3.x is installed on your system. You can download Python from the official website: https://www.python.org/downloads/.
Ensure Tkinter is Installed: Tkinter is the standard Python library for creating GUIs, and it usually comes pre-installed with Python. If it’s missing, you can install it using:

bash
Copy code
'''pip install tk'''
Download the Application:

Download or clone this repository to your local machine.

# Usage
1. Running the Application:
Navigate to the directory where todo_gui.py is located and run the script using:
bash
Copy code
python todo_gui.py
This will open the application window.

2. Interacting with the Application:
Add Task: Enter the task description and deadline, then click "Add Task" to add a new task.
Update Task Status: Select a task from the list, enter the new status (either "Pending" or "Completed") in the status entry field, and click "Update Task."
Delete Task: Select a task from the list and click "Delete Task" to remove it.
View Tasks: All tasks are displayed in a list format in the main window, showing the task description, deadline, and status.

# Task Data Persistence
The tasks are saved to a file called tasks.json. This file is used to store all tasks and their details (ID, description, status, and deadline). The application will automatically load the tasks from this file when it starts and save any changes when tasks are added, updated, or deleted.

The tasks.json file will be created in the same directory as the Python script when the application is first run.

#File Structure
bash
Copy code
todo_gui.py              # The main Python application script
tasks.json               # JSON file storing the tasks
README.md                # This README file

# Troubleshooting
Tkinter Not Found:

If Tkinter is not found, it may need to be installed manually. Use the following command to install it:
bash
Copy code
pip install tk
File Not Found (tasks.json):

If tasks.json is not found when the app starts, the app will create a new empty list. The file will be automatically created when tasks are added.

# License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

# Contributing
Feel free to fork this project and create pull requests for bug fixes or new features. If you have suggestions for improvement, please open an issue in the repository.

# Acknowledgments
Tkinter: For the simple and powerful GUI toolkit.
Python: For providing the platform to develop this app.
