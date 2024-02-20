import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def show_password():
    password_length = 12  # You can adjust the length as per your requirement
    generated_password = generate_password(password_length)
    messagebox.showinfo("Generated Password", generated_password)

# Create a tkinter window
window = tk.Tk()
window.title("Password Generator")

# Create a button to generate and show the password
button = tk.Button(window, text="Generate Password", command=show_password)
button.pack(pady=10)

# Run the tkinter event loop
window.mainloop()
