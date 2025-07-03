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

    users_folder = "backend/users"
    matched_file = None
    discount = None

    # Look through user files
    for file in os.listdir(users_folder):
        if file.startswith(f"{username}_{password}"):
            matched_file = file
            parts = file.replace(".txt", "").split("_")
            if len(parts) == 3:
                discount = parts[2]  # Student, Senior, or PWD
            break

    if matched_file:
        messagebox.showinfo("Login Successful", f"Welcome back, {username}!")

        # Save session info including discount
        with open("backend/session.py", "w", encoding="utf-8") as session_file:
            session_file.write(f'username = "{username}"\n')
            session_file.write(f'password = "{password}"\n')
            session_file.write(f'discount = "{discount}"\n')  # Will be None if no discount

        subprocess.Popen(["python", "page/main_window.py"])
        root_window.destroy()
    else:
        messagebox.showerror("Login Failed", "Account does not exist. Please register first.")
