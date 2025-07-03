import os
from tkinter import messagebox
import subprocess

account_datas = {}

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
        # Optionally load their info into memory
        account_datas[key] = {
            "Username": username,
            "Password": password
        }
        # Open dashboard and close login window
        subprocess.Popen(["python", "empty.py"])
        root_window.destroy()
    else:
        messagebox.showerror("Login Failed", "Account does not exist. Please register first.")
