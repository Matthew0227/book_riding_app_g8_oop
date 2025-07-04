import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import backend.register_page_backend


# Main Window Setup
root = tk.Tk()
root.title("BYAHE Ride Booking System")
root.geometry("916x571")
root.resizable(False, False)

# Background Image
bg_image = Image.open("pictures/v-de-leon-pureza-av.jpg")
bg_image = bg_image.resize((916, 571))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=916, height=571)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Left Side Panel
canvas.create_rectangle(0, 0, 365, 571, fill="#E1DEDE", outline="")

# Header Text
book_label = tk.Label(root, text="BYAHE BOOK RIDING", font=("Arial", 32), bg="#E1DEDE", fg="#000000")
canvas.create_window(182, 40, window=book_label, width=339, height=56)

# NEW USERNAME Label
username_label = tk.Label(root, text="NEW USERNAME", font=("Arial", 14), bg="#E1DEDE", fg="#000000", anchor="w", justify="left")
canvas.create_window(30, 150, window=username_label, width=300, height=28, anchor="w")

username_entry = tk.Entry(root, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0)
canvas.create_window(175, 185, window=username_entry, width=325, height=43)

# PASSWORD Label
password_label = tk.Label(root, text="PASSWORD", font=("Arial", 14), bg="#E1DEDE", fg="#000000", anchor="w", justify="left")
canvas.create_window(30, 240, window=password_label, width=300, height=28, anchor="w")

password_entry = tk.Entry(root, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0, show="*")
canvas.create_window(175, 275, window=password_entry, width=325, height=43)

# CONFIRM PASSWORD Label
confirm_label = tk.Label(root, text="CONFIRM PASSWORD", font=("Arial", 14), bg="#E1DEDE", fg="#000000", anchor="w", justify="left")
canvas.create_window(30, 330, window=confirm_label, width=300, height=28, anchor="w")

confirm_entry = tk.Entry(root, font=("Arial", 9), bg="#8B8585", fg="white", insertbackground="white", borderwidth=0, show="*")
canvas.create_window(175, 365, window=confirm_entry, width=325, height=43)

# Toggle for Password Field
def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show="")
        toggle_btn.config(text="Hide")

def toggle_password2():
    if confirm_entry.cget("show") == "":
        confirm_entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        confirm_entry.config(show="")
        toggle_btn.config(text="Hide")

toggle_btn = tk.Button(root, text="Show", command=toggle_password, font=("Arial", 10), bg="#CE3E3E", borderwidth=0)
canvas.create_window(320, 275, window=toggle_btn, width=40, height=43)

toggle_btn = tk.Button(root, text="Show", command=toggle_password2, font=("Arial", 10), bg="#CE3E3E", borderwidth=0)
canvas.create_window(320, 365, window=toggle_btn, width=40, height=43)


# Create Account Link
def open_register():
    root.destroy()
    subprocess.Popen(["python", "login_page.py"])

login_page_label = tk.Label(root, text="Already have an account?", font=("Arial", 10), fg="#A90000", bg="#E1DEDE", cursor="hand2")
login_page_label.bind("<Button-1>", lambda e: open_register())
canvas.create_window(270, 420, window=login_page_label, width=150, height=24)

# Register Button
def open_dashboard():
    backend.register_page_backend.handle_registration(username_entry, password_entry, confirm_entry, root)

register_button = tk.Button(
    root,
    text="REGISTER",
    font=("Arial", 24),
    bg="#A24141",
    fg="white",
    activebackground="#922121",
    activeforeground="white",
    borderwidth=1,
    command=open_dashboard
)
canvas.create_window(176, 480, window=register_button, width=170, height=45)

# Run Application
root.mainloop()
