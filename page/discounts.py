import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess
import sys
import os

# Add parent path to access backend/session.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.session import username, password

current_page = "Discount"

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

welcome_text = tk.StringVar(value=f"Welcome!, {username}")
username_label = tk.Label(menubar_frame, textvariable=welcome_text, bg="#F1DADA",
                          font=("Arial", 24), anchor="w", width=16)
username_label.place(x=7, y=0, height=41)

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
            os.remove(os.path.join("backend", "session.py"))
        except FileNotFoundError:
            pass
        root.destroy()
        return
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
root.after(10, lambda: menu_button.place(x=916 - menu_button.winfo_reqwidth() - 7, y=0, height=41))

# Rectangle Background
canvas.create_rectangle(124, 132, 791, 539, fill="#E1DEDE", outline="")

# Discount Labels
canvas.create_text(140, 140, anchor="nw", text="Discount", font=("Arial", 32, "bold"))

users_dir = os.path.join("backend", "users")
base_file = os.path.join(users_dir, f"{username}_{password}.txt")
student_file = os.path.join(users_dir, f"{username}_{password}_student.txt")
senior_file = os.path.join(users_dir, f"{username}_{password}_senior.txt")
pwd_file = os.path.join(users_dir, f"{username}_{password}_pwd.txt")

# Detect current discount
if os.path.exists(student_file):
    current_discount = "Student"
elif os.path.exists(senior_file):
    current_discount = "Senior"
elif os.path.exists(pwd_file):
    current_discount = "PWD"
else:
    current_discount = "(none)"

current_discount_text = canvas.create_text(140, 190, anchor="nw",
                                           text=f"Current discount: {current_discount}",
                                           font=("Arial", 14))

canvas.create_text(248, 230, anchor="center", text="Student", font=("Arial", 24))
canvas.create_text(458, 230, anchor="center", text="Senior Citizen", font=("Arial", 24))
canvas.create_text(667, 230, anchor="center", text="PWD", font=("Arial", 24))
canvas.create_text(667, 260, anchor="center", text="(Persons with Disability)", font=("Arial", 12))

discount_var = tk.StringVar(value="")

style = ttk.Style()
style.configure("Custom.TRadiobutton",
                background="#A24141",
                foreground="white",
                font=("Arial", 20),
                indicatoron=False,
                anchor="center",
                padding=16,
                relief="flat")

ttk.Radiobutton(root, text="", variable=discount_var, value="Student", style="Custom.TRadiobutton").place(x=224, y=390, width=50, height=42)
ttk.Radiobutton(root, text="", variable=discount_var, value="Senior", style="Custom.TRadiobutton").place(x=432, y=390, width=50, height=42)
ttk.Radiobutton(root, text="", variable=discount_var, value="PWD", style="Custom.TRadiobutton").place(x=632, y=390, width=50, height=42)

def apply_discount():
    selected = discount_var.get()
    if not selected:
        messagebox.showwarning("No Discount Selected", "Please select a discount to apply.")
        return

    target_file = {
        "Student": student_file,
        "Senior": senior_file,
        "PWD": pwd_file
    }[selected]

    # If another discount is currently applied, rename it back to base
    for f in [student_file, senior_file, pwd_file]:
        if f != target_file and os.path.exists(f):
            os.rename(f, base_file)

    # Only rename if it's not already applied
    if os.path.exists(base_file):
        os.rename(base_file, target_file)

    canvas.itemconfig(current_discount_text, text=f"Current discount: {selected}")
    messagebox.showinfo("Success", f"{selected} discount applied.")

def remove_discount():
    restored = False
    for f in [student_file, senior_file, pwd_file]:
        if os.path.exists(f):
            os.rename(f, base_file)
            restored = True
    if restored:
        canvas.itemconfig(current_discount_text, text="Current discount: (none)")
        messagebox.showinfo("Removed", "Discount has been removed.")
    else:
        messagebox.showinfo("Info", "No discount is currently applied.")

# Apply Button
tk.Button(root, text="Apply", bg="#A24141", fg="white", font=("Arial", 14),
          command=apply_discount).place(x=375, y=447, width=170, height=45)

# Remove Discount Button
tk.Button(root, text="Remove Discount", bg="#A24141", fg="white", font=("Arial", 12),
          command=remove_discount).place(x=375, y=494, width=170, height=35)

# Load and place icons
student_img_raw = Image.open("pictures/student.png").resize((89, 89))
student_img = ImageTk.PhotoImage(student_img_raw)
canvas.create_image(204, 279, image=student_img, anchor="nw")

senior_img_raw = Image.open("pictures/senior.png").resize((89, 89))
senior_img = ImageTk.PhotoImage(senior_img_raw)
canvas.create_image(412, 279, image=senior_img, anchor="nw")

pwd_img_raw = Image.open("pictures/pwd.png").resize((89, 89))
pwd_img = ImageTk.PhotoImage(pwd_img_raw)
canvas.create_image(612, 279, image=pwd_img, anchor="nw")

root.mainloop()
