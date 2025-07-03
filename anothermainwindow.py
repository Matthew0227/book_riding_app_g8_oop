import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os

current_user_key = None

# File Handling for Users
USERS_FILE = "users.json"

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        json.dump({}, f)

def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

# Main WIndow
root = tk.Tk()
root.title("Ride Booking System")
root.geometry("916x571")
root.resizable(False, False)

# Background image
bg_image = Image.open("C:/CpE 1-7/SourceCodes/rolobox.png")
bg_image = bg_image.resize((916, 571))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=916, height=571)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Frames
login_frame = tk.Frame(root, bg="#E1DEDE", width=365, height=571)
register_frame = tk.Frame(root, bg="#E1DEDE", width=365, height=571)
dashboard_frame = tk.Frame(root, bg="#FFFFFF", width=916, height=571)

canvas.create_window(0, 0, anchor="nw", window=login_frame)
canvas.create_window(0, 0, anchor="nw", window=register_frame)
canvas.create_window(0, 0, anchor="nw", window=dashboard_frame)

def show_frame(frame):
    login_frame.lower()
    register_frame.lower()
    dashboard_frame.lower()
    frame.lift()

# Log In Screen
tk.Label(login_frame, text="BOOK RIDING", font=("Arial", 32), bg="#E1DEDE").place(x=13, y=40)
tk.Label(login_frame, text="LOGIN", font=("Arial", 14), bg="#E1DEDE").place(x=35, y=130)

username_login = tk.Entry(login_frame, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0)
username_login.place(x=20, y=165, width=325, height=43)

tk.Label(login_frame, text="PASSWORD", font=("Arial", 14), bg="#E1DEDE").place(x=35, y=220)
password_login = tk.Entry(login_frame, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0, show="*")
password_login.place(x=20, y=255, width=325, height=43)

def toggle_login_pw():
    if password_login.cget("show") == "":
        password_login.config(show="*")
        toggle_login_btn.config(text="Show")
    else:
        password_login.config(show="")
        toggle_login_btn.config(text="Hide")

toggle_login_btn = tk.Button(login_frame, text="Show", command=toggle_login_pw, font=("Arial", 10), bg="#CE3E3E", borderwidth=0)
toggle_login_btn.place(x=300, y=255, width=40, height=43)

create_account_label = tk.Label(login_frame, text="Create an Account", font=("Arial", 10), fg="#A90000", bg="#E1DEDE", cursor="hand2")
create_account_label.place(x=200, y=305, width=120, height=24)
create_account_label.bind("<Button-1>", lambda e: show_frame(register_frame))

def open_dashboard():
    username = username_login.get()
    password = password_login.get()
    users = load_users()

    if username in users and users[username] == password:
        show_frame(dashboard_frame)
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

tk.Button(login_frame, text="LOGIN", font=("Arial", 24), bg="#A24141", fg="white",
          activebackground="#922121", activeforeground="white", borderwidth=1,
          command=open_dashboard).place(x=95, y=350, width=170, height=45)

# Register Screen
tk.Label(register_frame, text="BOOK RIDING", font=("Arial", 32), bg="#E1DEDE").place(x=13, y=40)
tk.Label(register_frame, text="NEW USERNAME", font=("Arial", 14), bg="#E1DEDE").place(x=30, y=130)

username_register = tk.Entry(register_frame, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0)
username_register.place(x=20, y=165, width=325, height=43)

tk.Label(register_frame, text="PASSWORD", font=("Arial", 14), bg="#E1DEDE").place(x=30, y=220)
password_register = tk.Entry(register_frame, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0, show="*")
password_register.place(x=20, y=255, width=325, height=43)

tk.Label(register_frame, text="CONFIRM PASSWORD", font=("Arial", 14), bg="#E1DEDE").place(x=30, y=310)
confirm_entry = tk.Entry(register_frame, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0, show="*")
confirm_entry.place(x=20, y=345, width=325, height=43)

def toggle_register_pw():
    if password_register.cget("show") == "":
        password_register.config(show="*")
        toggle_register_btn.config(text="Show")
    else:
        password_register.config(show="")
        toggle_register_btn.config(text="Hide")

toggle_register_btn = tk.Button(register_frame, text="Show", command=toggle_register_pw, font=("Arial", 10), bg="#CE3E3E", borderwidth=0)
toggle_register_btn.place(x=300, y=255, width=40, height=43)

toggle_confirm_btn = tk.Button(register_frame, text="Show", command=lambda: confirm_entry.config(show="" if confirm_entry.cget("show") == "*" else "*"),
                               font=("Arial", 10), bg="#CE3E3E", borderwidth=0)
toggle_confirm_btn.place(x=300, y=345, width=40, height=43)

login_label = tk.Label(register_frame, text="Already have an account?", font=("Arial", 10), fg="#A90000", bg="#E1DEDE", cursor="hand2")
login_label.place(x=170, y=395, width=150, height=24)
login_label.bind("<Button-1>", lambda e: show_frame(login_frame))

#Error Handling
def register_user():
    username = username_register.get()
    password = password_register.get()
    confirm_pw = confirm_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    if password != confirm_pw:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    users = load_users()
    if username in users:
        messagebox.showwarning("Exists", "Username already taken.")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Success", "Registration complete.")
        show_frame(login_frame)

tk.Button(register_frame, text="REGISTER", font=("Arial", 24), bg="#A24141", fg="white",
          activebackground="#922121", activeforeground="white", borderwidth=1,
          command=register_user).place(x=95, y=440, width=170, height=45)

options_frame = tk.Frame(dashboard_frame, bg="#FFFFFF", width=916, height=571)
mototaxi_frame = tk.Frame(dashboard_frame, bg="#FFFFFF", width=916, height=571)
fourwheels_frame = tk.Frame(dashboard_frame, bg="#FFFFFF", width=916, height=571)
public_frame = tk.Frame(dashboard_frame, bg="#FFFFFF", width=916, height=571)

for f in (options_frame, mototaxi_frame, fourwheels_frame, public_frame):
    f.place(x=0, y=0)

def show_dashboard_page(page_frame):
    options_frame.lower()
    mototaxi_frame.lower()
    fourwheels_frame.lower()
    public_frame.lower()
    page_frame.lift()

tk.Label(options_frame, text="Choose Your Ride", font=("Arial", 24), bg="#FFFFFF").place(x=320, y=30)

# Vehicle Icons
mototaxi_img = Image.open("mototaxi.webp").resize((100, 100))
fourwheel_img = Image.open("car.webp").resize((100, 100))
public_img = Image.open("public.webp").resize((100, 100))

mototaxi_icon = ImageTk.PhotoImage(mototaxi_img)
fourwheel_icon = ImageTk.PhotoImage(fourwheel_img)
public_icon = ImageTk.PhotoImage(public_img)

tk.Button(options_frame, image=mototaxi_icon, command=lambda: show_dashboard_page(mototaxi_frame), borderwidth=0, bg="#FFFFFF").place(x=150, y=120)
tk.Label(options_frame, text="Mototaxi", font=("Arial", 12), bg="#FFFFFF").place(x=170, y=230)

tk.Button(options_frame, image=fourwheel_icon, command=lambda: show_dashboard_page(fourwheels_frame), borderwidth=0, bg="#FFFFFF").place(x=400, y=120)
tk.Label(options_frame, text="4-Wheels", font=("Arial", 12), bg="#FFFFFF").place(x=425, y=230)

tk.Button(options_frame, image=public_icon, command=lambda: show_dashboard_page(public_frame), borderwidth=0, bg="#FFFFFF").place(x=650, y=120)
tk.Label(options_frame, text="Public Transport", font=("Arial", 12), bg="#FFFFFF").place(x=645, y=230)

def go_back():
    show_dashboard_page(options_frame)

def make_booking(name):
    messagebox.showinfo("Booking Confirmed", f"You booked a {name}.")
    with open(f"{current_user_key}.txt", "a") as f:
        f.write(f"\nBooked: {name}\n")


def cancel_booking(name):
    messagebox.showinfo("Booking Canceled", f"Your {name} booking was canceled.")

def create_booking_page(frame, transport_name, booking_enabled=True, is_four_wheels=False):
    tk.Label(frame, text=transport_name, font=("Arial", 24), bg="#FFFFFF").place(x=350, y=50)

    if booking_enabled:
        selected_seater = tk.StringVar()

        if is_four_wheels:
            tk.Label(frame, text="Select Seating Option:", font=("Arial", 14), bg="#FFFFFF").place(x=340, y=110)
            options = [("4-Seater", "4-seater"), ("6-Seater", "6-seater"), ("9-Seater", "9-seater")]
            for i, (label, value) in enumerate(options):
                tk.Radiobutton(frame, text=label, variable=selected_seater, value=value,
                               font=("Arial", 12), bg="#FFFFFF").place(x=370, y=150 + i*30)

            def book_4wheels():
                if not selected_seater.get():
                    messagebox.showwarning("Missing Selection", "Please select a seating option.")
                else:
                    messagebox.showinfo("Booking Confirmed", f"You booked a {selected_seater.get()} 4-Wheels vehicle.")

            tk.Button(frame, text="BOOK", font=("Arial", 16), bg="green", fg="white",
                      command=book_4wheels).place(x=300, y=270, width=100, height=40)

            tk.Button(frame, text="CANCEL", font=("Arial", 16), bg="red", fg="white",
                      command=lambda: messagebox.showinfo("Booking Canceled", "Your 4-Wheels booking was canceled.")
                      ).place(x=450, y=270, width=100, height=40)

        else:
            tk.Button(frame, text="BOOK", font=("Arial", 16), bg="green", fg="white",
                      command=lambda: make_booking(transport_name)).place(x=300, y=150, width=100, height=40)
            tk.Button(frame, text="CANCEL", font=("Arial", 16), bg="red", fg="white",
                      command=lambda: cancel_booking(transport_name)).place(x=450, y=150, width=100, height=40)

    else:
        tk.Label(frame, text="Routes & Fare Info", font=("Arial", 18), bg="#FFFFFF").place(x=350, y=130)
        tk.Label(frame, text="• Route 1: Downtown - City Center - ₱15\n"
                             "• Route 2: City Center - University - ₱12\n"
                             "• Route 3: Terminal - Airport - ₱20",
                 font=("Arial", 12), bg="#FFFFFF", justify="left").place(x=250, y=180)

    tk.Button(frame, text="BACK", font=("Arial", 12), bg="#CCCCCC",
              command=go_back).place(x=20, y=20)

create_booking_page(mototaxi_frame, "Mototaxi")
create_booking_page(fourwheels_frame, "4-Wheels", is_four_wheels=True)
create_booking_page(public_frame, "Public Transport", booking_enabled=False)

root.mainloop()