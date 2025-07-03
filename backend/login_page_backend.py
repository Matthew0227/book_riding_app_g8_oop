import os
from tkinter import messagebox
import subprocess

def letters_only(username):
    return all(char.isalpha() or char.isspace() for char in username)

def handle_login(username_entry, password_entry, root_window):
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    if not letters_only(username):
        messagebox.showerror("Input Error", "Username must contain letters only.")
        return

    key = f"{username}_{password}"
    file_path = f"./{key}.txt"

    # Check if user file exists (account exists)
    if os.path.exists(file_path):
        messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
        
        with open("backend/session.py", "w") as session_file:
            session_file.write(f'username = "{username}"\n')
            session_file.write(f'password = "{password}"\n')

        # Open dashboard and close login window
        subprocess.Popen(["python", "page/main_window.py"])
        root_window.destroy()
    else:
        messagebox.showerror("Login Failed", "Account does not exist. Please register first.")
