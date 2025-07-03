import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import os
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.session import username, password

current_page = "Settings"

# Main Window Setup
root = tk.Tk()
root.title("Ride Booking System")
root.geometry("916x571")
root.resizable(False, False)

# Background Image
bg_image = Image.open("pictures/v-de-leon-pureza-av.jpg")
bg_image = bg_image.resize((916, 571))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=916, height=571)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Top Menubar
menubar_frame = tk.Frame(root, width=916, height=41, bg="#F1DADA")
menubar_frame.place(x=0, y=0)

username_text = tk.StringVar(value=username)
username_label = tk.Label(menubar_frame, textvariable=username_text, bg="#F1DADA",
                          font=("Arial", 24), anchor="w", width=16)
username_label.place(x=7, y=0, height=41)

def on_menu_select(option):
    global current_page

    if option == current_page:
        messagebox.showinfo("Info", f"You are already in the {option} page.")
        return
    if option == "Booking":
        subprocess.Popen(["python", "page/main_window.py"])
        root.destroy()
    elif option == "Discounts":
        subprocess.Popen(["python", "page/discounts.py"])
        root.destroy()
    elif option == "Booking History":
        subprocess.Popen(["python", "page/booking_history.py"])
        root.destroy()
    elif option == "Settings":
        subprocess.Popen(["python", "page/settings.py"])
        root.destroy()
    elif option == "Log-out":
        try:
            os.remove(os.path.join(os.path.dirname(__file__), "..", "backend", "session.py"))
        except FileNotFoundError:
            pass
        root.destroy()

menu_button = tk.Menubutton(menubar_frame, text="MENU", font=("Arial", 24),
                            bg="#F1DADA", relief="flat")
menu = tk.Menu(menu_button, tearoff=0, font=("Arial", 14))
menu.add_command(label="Booking", command=lambda: on_menu_select("Booking"))
menu.add_command(label="Discounts", command=lambda: on_menu_select("Discounts"))
menu.add_command(label="Booking History", command=lambda: on_menu_select("Booking History"))
menu.add_command(label="Settings", command=lambda: on_menu_select("Settings"))
menu.add_separator()
menu.add_command(label="Log-out", command=lambda: on_menu_select("Log-out"))
menu_button.config(menu=menu)

def update_menu_position():
    menu_width = menu_button.winfo_reqwidth()
    menu_button.place(x=916 - menu_width - 7, y=0, height=41)

root.after(10, update_menu_position)

# ============================
# Settings Content
# ============================
canvas.create_rectangle(124, 132, 124 + 667, 132 + 407, fill="#E1DEDE", outline="")

canvas.create_text(140, 131, anchor="nw", text="Settings", font=("Arial", 32, "bold"), width=200)
canvas.create_text(140, 187, anchor="nw", text="Change your username or password:",
                   font=("Arial", 14), width=500)

canvas.create_text(147, 232, anchor="nw", text=f"Current username: {username}",
                   font=("Arial", 14), width=500)

canvas.create_text(147, 310, anchor="nw", text=f"Current password: {password}",
                   font=("Arial", 14), width=500)

# ============================
# Entry Fields
# ============================
new_username_entry = tk.Entry(root, font=("Arial", 14), bg="#FFFFFF", fg="#000000")
new_username_entry.place(x=147, y=260, width=325, height=43)

new_password_entry = tk.Entry(root, font=("Arial", 14), bg="#FFFFFF", fg="#000000")
new_password_entry.place(x=147, y=338, width=325, height=43)

# ============================
# Helper: update session file and rename user file
# ============================
def update_credentials(new_user=None, new_pass=None):
    global username, password

    user_dir = os.path.join(os.path.dirname(__file__), "..", "backend", "users")
    old_file = os.path.join(user_dir, f"{username}_{password}.txt")
    new_username = new_user if new_user else username
    new_password = new_pass if new_pass else password
    new_file = os.path.join(user_dir, f"{new_username}_{new_password}.txt")

    try:
        if os.path.exists(old_file):
            os.rename(old_file, new_file)
        else:
            messagebox.showerror("Error", "Original user file not found.")
            return

        # Update session.py
        session_path = os.path.join(os.path.dirname(__file__), "..", "backend", "session.py")
        with open(session_path, "w") as f:
            f.write(f'username = "{new_username}"\n')
            f.write(f'password = "{new_password}"\n')

        # Update global values
        username_text.set(new_username)
        username = new_username
        password = new_password
        messagebox.showinfo("Success", "Credentials updated successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to update: {e}")

# ============================
# Buttons
# ============================
def on_change_username():
    new_user = new_username_entry.get().strip()
    if new_user:
        update_credentials(new_user=new_user)
    else:
        messagebox.showwarning("Input Required", "Please enter a new username.")

def on_change_password():
    new_pass = new_password_entry.get().strip()
    if new_pass:
        update_credentials(new_pass=new_pass)
    else:
        messagebox.showwarning("Input Required", "Please enter a new password.")

change_user_btn = tk.Button(root, text="Change", bg="#A24141", fg="white",
                            font=("Arial", 14), borderwidth=1, relief="solid",
                            command=on_change_username)
change_user_btn.place(x=495, y=258, width=170, height=45)

change_pass_btn = tk.Button(root, text="Change", bg="#A24141", fg="white",
                            font=("Arial", 14), borderwidth=1, relief="solid",
                            command=on_change_password)
change_pass_btn.place(x=495, y=338, width=170, height=45)

# ============================
# Start Mainloop
# ============================
root.mainloop()
