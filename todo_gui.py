import tkinter as tk
from tkinter import messagebox
import json

# File where tasks will be saved
TASKS_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Function to update the tasks in the listbox
def update_task_list():
    task_listbox.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        task_listbox.insert(tk.END, f"ID: {task['id']} - {task['task']} - Status: {task['status']}")

# Add new task
def add_task():
    task_desc = task_entry.get()
    deadline = deadline_entry.get()

    if task_desc == "" or deadline == "":
        messagebox.showerror("Input Error", "Please enter both task description and deadline.")
        return

    # Create a new task dictionary
    new_task = {
        "id": len(tasks) + 1,
        "task": task_desc,
        "status": "Pending",
        "deadline": deadline
    }

    # Add the new task to the task list
    tasks.append(new_task)
    save_tasks(tasks)  # Save to file
    update_task_list()  # Refresh the listbox

    # Clear the input fields
    task_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)

# Update the status of the selected task
def update_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showerror("Selection Error", "Please select a task to update.")
        return

    # Get the selected task
    task_id = tasks[selected_task_index[0]]['id']
    new_status = status_entry.get().lower()

    if new_status not in ["pending", "completed"]:
        messagebox.showerror("Input Error", "Status must be 'pending' or 'completed'.")
        return

    # Update task status
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            break

    save_tasks(tasks)  # Save the updated list to file
    update_task_list()  # Refresh the listbox

    # Clear the status entry
    status_entry.delete(0, tk.END)

# Delete the selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showerror("Selection Error", "Please select a task to delete.")
        return

    # Get the task ID
    task_id = tasks[selected_task_index[0]]['id']

    # Remove task from the list
    tasks[:] = [task for task in tasks if task['id'] != task_id]

    save_tasks(tasks)  # Save the updated task list
    update_task_list()  # Refresh the listbox

# Initialize the Tkinter window
root = tk.Tk()
root.title("To-Do List Application")

# Load tasks from the file
tasks = load_tasks()

# Create widgets
task_label = tk.Label(root, text="Task Description:")
task_label.grid(row=0, column=0, padx=10, pady=10)

task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=10, pady=10)

deadline_label = tk.Label(root, text="Deadline (YYYY-MM-DD):")
deadline_label.grid(row=1, column=0, padx=10, pady=10)

deadline_entry = tk.Entry(root, width=30)
deadline_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

status_label = tk.Label(root, text="Update Status (pending/completed):")
status_label.grid(row=4, column=0, padx=10, pady=10)

status_entry = tk.Entry(root, width=30)
status_entry.grid(row=4, column=1, padx=10, pady=10)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.grid(row=5, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=5, column=1, padx=10, pady=10)

# Refresh the task list when the application starts
update_task_list()

# Start the Tkinter main loop
root.mainloop()