import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.session import username, password
from tkinter import messagebox

current_page = "Private"


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

# ============================
# Top Menubar
# ============================
menubar_frame = tk.Frame(root, width=916, height=41, bg="#F1DADA")
menubar_frame.place(x=0, y=0)

# Username Label (left side)
username_text = tk.StringVar(value=username)
username_label = tk.Label(menubar_frame, textvariable=username_text, bg="#F1DADA",
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
    if option == "Discounts":
        subprocess.Popen(["python", "page/discounts.py"])
        root.destroy()
    elif option == "Booking History":
        subprocess.Popen(["python", "page/booking_history.py"])
        root.destroy()
    elif option == "Settings":
        subprocess.Popen(["python", "page/settings.py"])
        root.destroy()
    elif option == "Log-out":
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

# Load images and resize to 186x186
motorcycle_img = ImageTk.PhotoImage(Image.open("pictures/mototaxi.webp").resize((186, 186)))
taxicab_img = ImageTk.PhotoImage(Image.open("pictures/car.webp").resize((186, 186)))
suv_img = ImageTk.PhotoImage(Image.open("pictures/suv.png").resize((186, 186)))

# Place images
canvas.create_image(49, 90, anchor="nw", image=motorcycle_img)
canvas.create_image(354, 90, anchor="nw", image=taxicab_img)
canvas.create_image(666, 90, anchor="nw", image=suv_img)

# ============================
# Transportation Option Rectangles + Labels
# ============================

canvas.create_rectangle(16, 286, 266, 375, fill="#C16060", outline="")
canvas.create_text(141, 330, text="MOTORCYCLE", font=("Arial", 24, "bold"), fill="black", anchor="center")

canvas.create_rectangle(325, 286, 575, 375, fill="#C16060", outline="")
canvas.create_text(450, 330, text="TAXICAB\n(4-seater)", font=("Arial", 20, "bold"), fill="black", anchor="center")

canvas.create_rectangle(634, 286, 884, 375, fill="#C16060", outline="")
canvas.create_text(759, 330, text="SUV\n(6-seater)", font=("Arial", 20, "bold"), fill="black", anchor="center")

root.mainloop()
