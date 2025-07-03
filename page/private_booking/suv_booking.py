import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import webbrowser
import os
import sys
from datetime import datetime


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.session import username, password, discount
from backend.fare_calculator import Suv

# === SESSION/DISCOUNT STATE ===
session_discount = discount

# === MAIN TKINTER WINDOW ===
root = tk.Tk()
root.title("SUV Booking System")
root.geometry("916x571")
root.resizable(False, False)

# === BACKGROUND IMAGE ===
bg_image = Image.open("pictures/v-de-leon-pureza-av.jpg")
bg_image = bg_image.resize((916, 571))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=916, height=571)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# === DASHBOARD BOOKING SECTION ===
booking_frame = tk.Frame(root, bg="#FFFFFF")
booking_frame.place(x=230, y=100, width=460, height=400)

tk.Label(booking_frame, text="Start Location:", font=("Arial", 12), bg="#FFFFFF").place(x=10, y=10)
start_entry = tk.Entry(booking_frame, font=("Arial", 12), width=40)
start_entry.place(x=140, y=10)

tk.Label(booking_frame, text="End Location:", font=("Arial", 12), bg="#FFFFFF").place(x=10, y=50)
end_entry = tk.Entry(booking_frame, font=("Arial", 12), width=40)
end_entry.place(x=140, y=50)

tk.Label(booking_frame, text="Discount:", font=("Arial", 12), bg="#FFFFFF").place(x=10, y=90)
discount_var = tk.StringVar(value=session_discount)
discount_entry = tk.Entry(booking_frame, font=("Arial", 12), textvariable=discount_var, state="readonly", width=37)
discount_entry.place(x=140, y=90)

fare_label = tk.Label(booking_frame, text="Estimated Fare: ₱0", font=("Arial", 12), bg="#FFFFFF")
fare_label.place(x=140, y=130)

bookings = []
geolocator = Nominatim(user_agent="fare_estimator")

# === DISTANCE USING GEOPY ===
def get_distance_km(start, end):
    try:
        start_location = geolocator.geocode(start)
        end_location = geolocator.geocode(end)

        if not start_location:
            print(f"Could not find start location: '{start}'")
        if not end_location:
            print(f"Could not find end location: '{end}'")

        if start_location and end_location:
            start_coords = (start_location.latitude, start_location.longitude)
            end_coords = (end_location.latitude, end_location.longitude)
            distance_km = round(geodesic(start_coords, end_coords).km, 2)
            print(f"Start: {start_coords}, End: {end_coords}, Distance: {distance_km} km")
            return distance_km
        else:
            return 0
    except Exception as e:
        print("Error fetching distance:", e)
        return 0

# === OPEN MAP ===
def open_google_maps(start, end):
    if not start or not end:
        messagebox.showwarning("Missing Fields", "Please fill in both start and end locations.")
        return
    start_url = start.replace(' ', '+')
    end_url = end.replace(' ', '+')
    url = f"https://www.google.com/maps/dir/{start_url}/{end_url}"
    webbrowser.open(url)

# === FARE CALCULATION ===
def calculate_and_display_fare(start, end, discount):
    distance = get_distance_km(start, end)
    suv = Suv(discount)
    fare = suv.calculate_fare(distance)
    fare_label.config(text=f"Estimated Fare: ₱{fare}")

def manual_calculate_fare():
    start = start_entry.get()
    end = end_entry.get()
    discount = discount_var.get()
    if not start or not end:
        fare_label.config(text="Estimated Fare: ₱0")
        return
    fare_label.config(text="Calculating...")
    root.after(100, lambda: calculate_and_display_fare(start, end, discount))

def book_ride():
    start = start_entry.get()
    end = end_entry.get()
    discount = discount_var.get()

    if not start or not end:
        messagebox.showwarning("Missing Fields", "Please fill all fields.")
        return

    distance = get_distance_km(start, end)
    suv = Suv(discount)
    fare = suv.calculate_fare(distance)

    booking = {
        "start": start,
        "end": end,
        "discount": discount,
        "distance_km": distance,
        "fare": fare
    }
    bookings.append(booking)

    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    # === Save booking to backend/bookings.txt ===
    bookings_file = os.path.join(os.path.dirname(__file__), "..", "..", "backend", "users", f"{username}_{password}_{discount}.txt")
    try:
        with open(bookings_file, "a", encoding="utf-8") as f:
            f.write("========================================\n")
            f.write(f"Date/Time : {now}\n")
            f.write(f"Vehicle   : SUV\n")
            f.write(f"From      : {start}\n")
            f.write(f"To        : {end}\n")
            f.write(f"Distance  : {distance} km\n")
            f.write(f"Discount  : {discount}\n")
            f.write(f"Fare      : ₱{fare}\n")
            f.write("========================================\n\n")
    except Exception as e:
        print(f"Warning: Could not save booking: {e}")

    messagebox.showinfo("Booking Confirmed", f"SUV booked from {start} to {end}. Fare: ₱{fare}")
    fare_label.config(text=f"Estimated Fare: ₱{fare}")

def cancel_last_booking():
    if bookings:
        bookings.pop()
        messagebox.showinfo("Cancelled", "The last booking has been cancelled.")
    else:
        messagebox.showinfo("No Bookings", "No bookings to cancel.")

# === BUTTONS ===
tk.Button(booking_frame, text="Calculate Fare", font=("Arial", 12), bg="#FFA500", fg="white",
          command=manual_calculate_fare).place(x=140, y=170)

tk.Button(booking_frame, text="Book Ride", font=("Arial", 12), bg="#008CBA", fg="white",
          command=book_ride).place(x=280, y=170)

tk.Button(booking_frame, text="Cancel Last Booking", font=("Arial", 12), bg="#f44336", fg="white",
          command=cancel_last_booking).place(x=140, y=210)

tk.Button(booking_frame, text="View Route on Map", font=("Arial", 12), bg="#4CAF50", fg="white",
          command=lambda: open_google_maps(start_entry.get(), end_entry.get())).place(x=140, y=250)

root.mainloop()
