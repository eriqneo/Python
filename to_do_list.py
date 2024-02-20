import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.config(bg='white')

# Create and configure the task entry
entry_task = tk.Entry(window, font=("Arial", 12), bg='white', bd=2, relief=tk.GROOVE)
entry_task.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Create the task list
listbox_tasks = tk.Listbox(window, font=("Arial", 12), bg='white', bd=2, relief=tk.GROOVE, selectbackground='maroon')
listbox_tasks.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create scrollbar
scrollbar_tasks = tk.Scrollbar(window, bg='white', orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar_tasks.grid(row=1, column=1, sticky='ns')

# Link scrollbar to task list
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

# Create buttons for adding and deleting tasks
button_add_task = tk.Button(window, text="Add Task", font=("Arial", 12), bg='maroon', fg='white', relief=tk.GROOVE, command=add_task)
button_add_task.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

button_delete_task = tk.Button(window, text="Delete Task", font=("Arial", 12), bg='maroon', fg='white', relief=tk.GROOVE, command=delete_task)
button_delete_task.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# Configure grid rows and columns
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

# Start the tkinter event loop
window.mainloop()
