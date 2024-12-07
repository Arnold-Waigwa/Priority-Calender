import tkinter as tk
from tkinter import ttk
from PrioritySchedule import calculatePriority
from task import Task

# List to hold tasks
tasks = []

def add_task():
    """Add a task to the list based on user input."""
    name = name_var.get()
    duration = int(duration_var.get())
    difficulty = int(difficulty_var.get())
    deadline = deadline_var.get()
    
    if name and duration and difficulty and deadline:
        # Create a Task object
        task = Task(name, deadline, difficulty, duration)
        tasks.append(task)
        update_task_table()
        clear_inputs()

def update_task_table():
    """Update the table to display current tasks."""
    for row in task_table.get_children():
        task_table.delete(row)
    for task in tasks:
        task_table.insert("", "end", values=(task.name, task.priority_score, task.days_remaining, task.hardness_level))

def clear_inputs():
    """Clear input fields."""
    name_var.set("")
    duration_var.set("")
    difficulty_var.set("")
    deadline_var.set("")

def generate_schedule():
    """Generate and display the optimized schedule."""
    if tasks:
        sorted_tasks = calculatePriority(tasks)
        for row in schedule_table.get_children():
            schedule_table.delete(row)
        for task in sorted_tasks:
            schedule_table.insert("", "end", values=(task.name, task.priority_score))

# Initialize Tkinter
root = tk.Tk()
root.title("Task Scheduler")

# Input section
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

name_var = tk.StringVar()
duration_var = tk.StringVar()
difficulty_var = tk.StringVar()
deadline_var = tk.StringVar()

tk.Label(input_frame, text="Task Name:").grid(row=0, column=0, padx=5, pady=2)
tk.Entry(input_frame, textvariable=name_var).grid(row=0, column=1, padx=5, pady=2)
tk.Label(input_frame, text="Duration (hours):").grid(row=1, column=0, padx=5, pady=2)
tk.Entry(input_frame, textvariable=duration_var).grid(row=1, column=1, padx=5, pady=2)
tk.Label(input_frame, text="Difficulty Level:").grid(row=2, column=0, padx=5, pady=2)
tk.Entry(input_frame, textvariable=difficulty_var).grid(row=2, column=1, padx=5, pady=2)
tk.Label(input_frame, text="Deadline:").grid(row=3, column=0, padx=5, pady=2)
tk.Entry(input_frame, textvariable=deadline_var).grid(row=3, column=1, padx=5, pady=2)

tk.Button(input_frame, text="Add Task", command=add_task).grid(row=4, column=0, columnspan=2, pady=10)

# Task table
task_table_frame = tk.Frame(root)
task_table_frame.pack(pady=10)

task_table = ttk.Treeview(task_table_frame, columns=("Name", "Priority", "Days Remaining", "Hardness"), show="headings")
task_table.heading("Name", text="Name")
task_table.heading("Priority", text="Priority")
task_table.heading("Days Remaining", text="Days Remaining")
task_table.heading("Hardness", text="Hardness Level")
task_table.pack()

# Generate schedule button
tk.Button(root, text="Generate Schedule", command=generate_schedule).pack(pady=10)

# Schedule table
schedule_frame = tk.Frame(root)
schedule_frame.pack(pady=10)

schedule_table = ttk.Treeview(schedule_frame, columns=("Name", "Priority"), show="headings")
schedule_table.heading("Name", text="Task Name")
schedule_table.heading("Priority", text="Priority")
schedule_table.pack()

# Run the app
root.mainloop()
