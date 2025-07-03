import tkinter as tk
from tkinter import messagebox

def open_dashboard(user_key):
    global current_user_key
    current_user_key = user_key
    root = tk.Tk()
    root.title("Transportation Booking")
    root.geometry("500x400")

    def book_ride():
        transport_type = transport_entry.get().strip()
        if not transport_type:
            messagebox.showerror("Input Error", "Enter a type of transport.")
            return

        # Save booking to user's file
        file_path = f"./{user_key}.txt"
        with open(file_path, "a") as file:
            file.write(f"Booked ride: {transport_type}\n")

        messagebox.showinfo("Booked", f"{transport_type} booked successfully!")

    tk.Label(root, text=f"Welcome, {user_key.split('_')[0]}", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="Enter Transport Type (Jeep, LRT, etc):").pack()

    transport_entry = tk.Entry(root)
    transport_entry.pack(pady=5)

    tk.Button(root, text="Book Ride", command=book_ride).pack(pady=10)

    root.mainloop()
