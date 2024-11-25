import json

# Data Structure Definition
tasks = [
    {"id": 1, "task": "Buy groceries", "status": "pending", "deadline": "2024-11-30"},
    {"id": 2, "task": "Read Python book", "status": "completed", "deadline": "2024-12-01"}
]

# Function to display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Task List:")
        for task in tasks:
            print(f"ID: {task['id']} - Task: {task['task']} - Status: {task['status']} - Deadline: {task['deadline']}")

# Function to add a new task
def add_task(tasks, task_desc, deadline):
    new_id = len(tasks) + 1
    task = {"id": new_id, "task": task_desc, "status": "pending", "deadline": deadline}
    tasks.append(task)
    print("Task added successfully.")

# Function to update a task
def update_task(tasks, task_id, new_status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            print(f"Task {task_id} updated to {new_status}.")
            return
    print("Task not found.")

# Function to delete a task
def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted.")
            return
    print("Task not found.")

def main():
    tasks = []  # Initialize an empty list of tasks
    
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task_desc = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            add_task(tasks, task_desc, deadline)
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status (pending/completed): ")
            update_task(tasks, task_id, new_status)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == "5":
            save_tasks_to_file(tasks)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

# Save tasks to file
def save_tasks_to_file(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)

# Load tasks from file
def load_tasks_from_file(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
