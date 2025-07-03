import tkinter as tk
from PIL import Image, ImageTk
import sys
import os
import subprocess

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
    correct_filename = "public_transportation.py" 
    public_page = os.path.join(base_dir, "page", correct_filename)
    print(f"Launching: {public_page}")
    subprocess.Popen(["python", public_page])
    root.destroy()

def show_image(image_name, container=None, side="top", width=600, height=800, padx=0):
    """Safely load and display image"""
    image_path = os.path.join(pictures_dir, image_name)
    try:
        img = Image.open(image_path).resize((width, height))
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(container if container else root, image=photo)
        label.image = photo  # keep reference
        label.pack(side=side, padx=padx)
    except FileNotFoundError:
        tk.Label(container if container else root, text=f"Image not found: {image_name}", fg="red", font=("Arial", 12)).pack(pady=20)

def show_vehicle_info():
    if vehicle_type == "JEEP":
        tk.Label(root, text="JEEP Fare Rates", font=("Arial", 18)).pack(pady=10)
        show_image("PUJ.jpg")

    elif vehicle_type == "BUS":
        tk.Label(root, text="BUS Fare Rates", font=("Arial", 18)).pack(pady=10)
        show_image("PUB.jpg")

    elif vehicle_type == "LRT":
        tk.Label(root, text="LRT Fare", font=("Arial", 18)).pack(pady=10)

        # Frame for side-by-side images
        image_frame = tk.Frame(root)
        image_frame.pack(pady=10)

        # Show both LRT1 and LRT2 side by side
        show_image("LRT1.jpg", container=image_frame, side="left", width=800, height=800, padx=5)
        show_image("LRT2.jpg", container=image_frame, side="left", width=800, height=800, padx=5)

    else:
        tk.Label(root, text="Unknown Transport Type", font=("Arial", 18)).pack(pady=20)

    # Go Back Button
    go_back_btn = tk.Button(root, text="← Go Back", font=("Arial", 14), bg="#C16060", fg="white", command=go_back)
    go_back_btn.place(x=10, y=10, width=100, height=40)

show_vehicle_info()
root.mainloop()
