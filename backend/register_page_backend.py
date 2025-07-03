import os
from tkinter import messagebox
import subprocess

Discount = "None"

def letters_only(username):
    return all(char.isalpha() or char.isspace() for char in username)

def handle_registration(username_entry, password_entry, confirm_entry, root_window):
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    confirm_password = confirm_entry.get().strip()

    if not username or not password or not confirm_password:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    if not letters_only(username):
        messagebox.showerror("Input Error", "Username must contain letters only.")
        return

    if password != confirm_password:
        messagebox.showerror("Input Error", "Passwords do not match.")
        return

    key = f"{username}_{password}_{Discount}"
    file_path = f"backend/users/{key}.txt"

    if os.path.exists(file_path):
        messagebox.showerror("Account Exists", "An account with this username and password already exists.")
        return

    # Create user file and write initial content
    with open(file_path, "w") as file_txt:
        file_txt.write("-------------------\n")
        file_txt.write("BOOKING HISTORY\n")
        file_txt.write("-------------------\n")

    messagebox.showinfo("Registration Successful", f"Account created for {username}!")

    with open("backend/session.py", "w") as session_file:
            session_file.write(f'username = "{username}"\n')
            session_file.write(f'password = "{password}"\n')
            session_file.write(f'discount = "none"\n')

        # Open dashboard and close login window
    subprocess.Popen(["python", "page/main_window.py"])
    root_window.destroy()
