import tkinter as tk
from PIL import Image, ImageTk
import sys
import os
import subprocess
from tkinter import messagebox

# Vehicle passed as command-line argument
vehicle_type = sys.argv[1] if len(sys.argv) > 1 else "UNKNOWN"

root = tk.Tk()
root.geometry("800x600")
root.title(f"{vehicle_type} Fare Info")

# Get full path to pictures
script_dir = os.path.dirname(os.path.abspath(__file__))
pictures_dir = os.path.join(script_dir, "..", "pictures")

def go_back():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public_page = os.path.join(base_dir, "public_transportation.py")

    if os.path.exists(public_page):
        subprocess.Popen(["python", public_page])
        root.destroy()
    else:
        messagebox.showerror("File Not Found", f"{public_page} not found.")

def show_images_scrolled_together(image_list, width=760):
    """Display multiple images stacked vertically in a single scrollable canvas"""
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(canvas_frame, width=width)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Inner frame to hold all images
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    for image_name in image_list:
        image_path = os.path.join(pictures_dir, image_name)
        try:
            img = Image.open(image_path)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(inner_frame, image=photo)
            label.image = photo  # keep reference
            label.pack(pady=5)
        except FileNotFoundError:
            tk.Label(inner_frame, text=f"Image not found: {image_name}", fg="red", font=("Arial", 12)).pack(pady=20)

def show_image(image_name, width=760, height=800):
    """Single image scrollable (used by JEEP and BUS)"""
    show_images_scrolled_together([image_name], width)

def show_vehicle_info():
    if vehicle_type == "JEEP":
        tk.Label(root, text="JEEP Fare Rates", font=("Arial", 18)).pack(pady=10)
        show_image("PUJ.jpg")

    elif vehicle_type == "BUS":
        tk.Label(root, text="BUS Fare Rates", font=("Arial", 18)).pack(pady=10)
        show_image("PUB.jpg")

    elif vehicle_type == "LRT":
        tk.Label(root, text="LRT Fare", font=("Arial", 18)).pack(pady=10)
        show_images_scrolled_together(["LRT1.jpg", "LRT2.jpg"], width=760)

    else:
        tk.Label(root, text="Unknown Transport Type", font=("Arial", 18)).pack(pady=20)

    # Go Back Button
    go_back_btn = tk.Button(root, text="← Go Back", font=("Arial", 14), bg="#C16060", fg="white", command=go_back)
    go_back_btn.place(x=10, y=10, width=100, height=40)

show_vehicle_info()
root.mainloop()
