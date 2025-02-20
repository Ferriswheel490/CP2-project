#Fairus to do list

import os

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

# Function to add a task
def add_task(tasks, new_task, filename):
    tasks.append(new_task)
    save_tasks(filename, tasks)
    print(f"Task '{new_task}' added.")

# Function to remove a task
def remove_task(tasks, task_index, filename):
    try:
        removed_task = tasks.pop(task_index - 1)
        save_tasks(filename, tasks)
        print(f"Task '{removed_task}' removed.")
    except IndexError:
        print("Invalid task number.")

filename = "Todo List/tasks.txt"
tasks = load_tasks(filename)

# The main loop
while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks(tasks)
    elif choice == "2":
        new_task = input("Enter a new task: ")
        add_task(tasks, new_task, filename)
    elif choice == "3":
        display_tasks(tasks)
        try:
            task_index = int(input("Enter task number to remove: "))
            remove_task(tasks, task_index, filename)
        except ValueError:
            print("Invalid input, please enter a number.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
