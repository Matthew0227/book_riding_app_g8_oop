import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import login_page_backend

# Main Window Setup
root = tk.Tk()
root.title("Ride Booking System")
root.geometry("916x571")
root.resizable(False, False)

# Background Image
bg_image = Image.open("v-de-leon-pureza-av.jpg")
bg_image = bg_image.resize((916, 571))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=916, height=571)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Left Side Panel
canvas.create_rectangle(0, 0, 365, 571, fill="#E1DEDE", outline="")

# Header Text
book_label = tk.Label(root, text="BOOK RIDING", font=("Arial", 32), bg="#E1DEDE", fg="#000000")
canvas.create_window(182, 40, window=book_label, width=339, height=56)

# Login Section
login_label = tk.Label(root, text="LOGIN", font=("Arial", 14), bg="#E1DEDE", fg="#000000")
canvas.create_window(35, 150, window=login_label, width=100, height=28)

username_entry = tk.Entry(root, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0)
canvas.create_window(175, 185, window=username_entry, width=325, height=43)

password_label = tk.Label(root, text="PASSWORD", font=("Arial", 14), bg="#E1DEDE", fg="#000000")
canvas.create_window(65, 240, window=password_label, width=140, height=28)

password_entry = tk.Entry(root, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0, show="*")
canvas.create_window(175, 275, window=password_entry, width=325, height=43)

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show="")
        toggle_btn.config(text="Hide")

toggle_btn = tk.Button(root, text="Show", command=toggle_password, font=("Arial", 10), bg="#CE3E3E", borderwidth=0)
canvas.create_window(320, 275, window=toggle_btn, width=40, height=43)

# Create Account Link
def open_register():
    root.destroy()
    subprocess.Popen(["python", "register_page.py"])

create_account_label = tk.Label(root, text="Create an Account", font=("Arial", 10), fg="#A90000", bg="#E1DEDE", cursor="hand2")
create_account_label.bind("<Button-1>", lambda e: open_register())
canvas.create_window(290, 313, window=create_account_label, width=107, height=24)

# Login Button
def open_dashboard():
    login_page_backend.handle_login(username_entry, password_entry, root)

login_button = tk.Button(
    root,
    text="LOGIN",
    font=("Arial", 24),
    bg="#A24141",
    fg="white",
    activebackground="#922121",
    activeforeground="white",
    borderwidth=1,
    command=open_dashboard
)
canvas.create_window(176, 358, window=login_button, width=170, height=45)

# Run Application
root.mainloop()
