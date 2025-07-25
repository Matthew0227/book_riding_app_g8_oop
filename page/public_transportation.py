import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import os
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.session import username, password

current_page = "Public"

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

# ============================
# Top Menubar
# ============================
menubar_frame = tk.Frame(root, width=916, height=41, bg="#F1DADA")
menubar_frame.place(x=0, y=0)

# Username Label (left side)
welcome_text = tk.StringVar(value=f"Welcome!, {username}")
username_label = tk.Label(menubar_frame, textvariable=welcome_text, bg="#F1DADA",
                          font=("Arial", 24), anchor="w", width=16)
username_label.place(x=7, y=0, height=41)

# Dropdown Menu (right side)
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
menu.add_command(label="Back", command=lambda: on_menu_select("Booking"))
menu.add_command(label="Discounts", command=lambda: on_menu_select("Discounts"))
menu.add_command(label="Booking History", command=lambda: on_menu_select("Booking History"))
menu.add_command(label="Settings", command=lambda: on_menu_select("Settings"))
menu.add_separator()
menu.add_command(label="Log-out", command=lambda: on_menu_select("Log-out"))

menu_button.config(menu=menu)

# Delay placement until width is known
def update_menu_position():
    menu_width = menu_button.winfo_reqwidth()
    menu_button.place(x=916 - menu_width - 7, y=0, height=41)

root.after(10, update_menu_position)

# ============================
# Transport Images
# ============================
jeep_img = ImageTk.PhotoImage(Image.open("pictures/jeep.png").resize((186, 186)))
bus_img = ImageTk.PhotoImage(Image.open("pictures/bus.png").resize((186, 186)))
lrt_img = ImageTk.PhotoImage(Image.open("pictures/public.webp").resize((186, 186)))

canvas.create_image(49, 90, anchor="nw", image=jeep_img)
canvas.create_image(354, 90, anchor="nw", image=bus_img)
canvas.create_image(666, 90, anchor="nw", image=lrt_img)

# ============================
# Transport Buttons
# ============================

def open_vehicle_page(vehicle_name):
    booking_path = os.path.join("page", "public_fare", "public_trans.py")
    subprocess.Popen(["python", booking_path, vehicle_name])
    root.destroy()

tk.Button(root, text="JEEP", font=("Arial", 24, "bold"),
          bg="#C16060", fg="black", command=lambda: open_vehicle_page("JEEP")
).place(x=16, y=286, width=250, height=89)

tk.Button(root, text="BUS", font=("Arial", 20, "bold"),
          bg="#C16060", fg="black", command=lambda: open_vehicle_page("BUS")
).place(x=325, y=286, width=250, height=89)

tk.Button(root, text="LRT", font=("Arial", 20, "bold"),
          bg="#C16060", fg="black", command=lambda: open_vehicle_page("LRT")
).place(x=634, y=286, width=250, height=89)

# ============================
# Mainloop
# ============================
root.mainloop()
