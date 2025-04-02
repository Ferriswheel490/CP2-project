import tkinter as tk
from tkinter import messagebox
import subprocess

# Dictionary of projects
projects = {
    "To-Do List App": "todo.py",
    "Expense Tracker": "expenses.py"
}

# Function to show project details
def show_project_details(project_name):
    details = {
        "To-Do List App": "A simple task manager with local storage.",
        "Chatbot": "A simple chatbot using AI and NLP."
    }
    
    project_info = details.get(project_name, "No details available.")
    response = messagebox.askyesno("Project Details", f"{project_info}\n\nDo you want to run {project_name}?")
    if response:
        run_project(project_name)

# Function to run the selected project
def run_project(project_name):
    script = projects.get(project_name)
    if script:
        try:
            subprocess.run(["python", script], check=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run {project_name}: {e}")
    else:
        messagebox.showerror("Error", "Project script not found.")

# GUI Setup
root = tk.Tk()
root.title("My Programming Portfolio")
root.geometry("400x500")

tk.Label(root, text="Welcome to My Portfolio", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Click on a project to learn more and run it.").pack(pady=5)

for project in projects.keys():
    tk.Button(root, text=project, command=lambda p=project: show_project_details(p), width=40).pack(pady=5)

root.mainloop()
