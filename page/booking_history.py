import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import os
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.session import username, password, discount

current_page = "Booking History"

# === Helper to locate the correct booking history file ===
def get_user_file():
    user_dir = os.path.join(os.path.dirname(__file__), "..", "backend", "users")
    # Try plain username_password
    base_filename = f"{username}_{password}_None.txt"
    base_path = os.path.join(user_dir, base_filename)

    if os.path.exists(base_path):
        return base_path

    # Try discount suffix
    for discount in ["Student", "Senior", "PWD"]:
        alt_path = os.path.join(user_dir, f"{username}_{password}_{discount}.txt")
        if os.path.exists(alt_path):
            return alt_path

    return None  # Not found

# === Main Window Setup ===
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

# Welcome label
welcome_text = tk.StringVar(value=f"Welcome!, {username}")
username_label = tk.Label(menubar_frame, textvariable=welcome_text, bg="#F1DADA",
                          font=("Arial", 24), anchor="w", width=16)
username_label.place(x=7, y=0, height=41)

# Menu handling
def on_menu_select(option):
    global current_page

    if option == current_page:
        messagebox.showinfo("Info", f"You are already in the {option} page.")
        return
    if option == "Booking":
        subprocess.Popen(["python", "page/main_window.py"])
    elif option == "Discounts":
        subprocess.Popen(["python", "page/discounts.py"])
    elif option == "Booking History":
        subprocess.Popen(["python", "page/booking_history.py"])
    elif option == "Settings":
        subprocess.Popen(["python", "page/settings.py"])
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
# Booking History Display
# ============================
canvas.create_rectangle(124, 100, 124 + 667, 100 + 407, fill="#E1DEDE", outline="")
canvas.create_text(140, 105, anchor="nw", text="Booking History",
                   font=("Arial", 28, "bold"), fill="#000")

history_box = tk.Text(root, font=("Arial", 10), bg="white", fg="black")
history_box.place(x=140, y=160, width=630, height=320)

file_path = get_user_file()
if file_path:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                history_box.insert("1.0", "".join(lines))
            else:
                history_box.insert("1.0", "No booking history found.")
    except Exception as e:
        history_box.insert("1.0", f"Error reading file:\n{e}")
else:
    history_box.insert("1.0", "No user file found. Please check your account.")

history_box.config(state="disabled")  # make it read-only

# ============================
# Start Mainloop
# ============================
root.mainloop()
