# todo_list.py
# Fairus – To-Do List Program

import os

# Entry point for your portfolio
def list():
    print("""
Welcome to the To-Do List!

This is a simple task manager where you can:
- View your tasks
- Add new ones
- Remove completed tasks
This was another things I learned in class
I learned how to list things and remove things on a list
    """)
    ans = input("Do you want to use it? (y/n): ").strip().lower()
    if ans in ("yes", "y"):
        run_program()
    elif ans in ("no", "n"):
        return
    else:
        print("Not a valid option. Returning to portfolio.")

# Load tasks from file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def display_tasks(tasks):
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Add a task
def add_task(tasks, new_task, filename):
    tasks.append(new_task)
    save_tasks(filename, tasks)
    print(f"Task '{new_task}' added.")

# Remove a task
def remove_task(tasks, task_index, filename):
    try:
        removed_task = tasks.pop(task_index - 1)
        save_tasks(filename, tasks)
        print(f"Task '{removed_task}' removed.")
    except IndexError:
        print("Invalid task number.")

# Main to-do program
def run_program():
    filename = "Todo List/tasks.txt"
    os.makedirs("Todo List", exist_ok=True)  # Ensure folder exists
    tasks = load_tasks(filename)

    while True:
        print("""
=======================
To-Do List Menu
1. Display tasks
2. Add a task
3. Remove a task
4. Exit
=======================
""")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                add_task(tasks, new_task, filename)
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_index = int(input("Enter task number to remove: "))
                remove_task(tasks, task_index, filename)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting To-Do List. Tasks saved.")
            break
        else:
            print("Invalid choice. Please try again.")

# Only runs when file is executed directly
if __name__ == "__main__":
    list()
