import tkinter as tk
from tkinter import ttk, messagebox

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Farmer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city

class Volunteer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city
        self.confirmation = ""

class Event:
    def __init__(self, event_name, event_date, description, farmer):
        self.event_name = event_name
        self.event_date = event_date
        self.description = description
        self.farmer = farmer
        self.volunteers = []

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

def get_volunteer_details():
    volunteer_window = tk.Toplevel(root)
    volunteer_window.title("Volunteer Details")

    ttk.Label(volunteer_window, text="Enter Volunteer Details:").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(volunteer_window, text="First Name:").grid(row=1, column=0, pady=5)
    first_name_entry = ttk.Entry(volunteer_window)
    first_name_entry.grid(row=1, column=1, pady=5)

    ttk.Label(volunteer_window, text="Last Name:").grid(row=2, column=0, pady=5)
    last_name_entry = ttk.Entry(volunteer_window)
    last_name_entry.grid(row=2, column=1, pady=5)

    ttk.Label(volunteer_window, text="Phone Number:").grid(row=3, column=0, pady=5)
    phone_number_entry = ttk.Entry(volunteer_window)
    phone_number_entry.grid(row=3, column=1, pady=5)

    ttk.Label(volunteer_window, text="City:").grid(row=4, column=0, pady=5)
    city_entry = ttk.Entry(volunteer_window)
    city_entry.grid(row=4, column=1, pady=5)

    def save_volunteer_details():
        volunteer_window.destroy()
        return Volunteer(
            first_name_entry.get(),
            last_name_entry.get(),
            phone_number_entry.get(),
            city_entry.get()
        )

    ttk.Button(volunteer_window, text="Save", command=save_volunteer_details).grid(row=5, column=0, columnspan=2, pady=10)

def get_farmer_details():
    farmer_window = tk.Toplevel(root)
    farmer_window.title("Farmer Details")

    ttk.Label(farmer_window, text="Enter Farmer Details:").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(farmer_window, text="First Name:").grid(row=1, column=0, pady=5)
    first_name_entry = ttk.Entry(farmer_window)
    first_name_entry.grid(row=1, column=1, pady=5)

    ttk.Label(farmer_window, text="Last Name:").grid(row=2, column=0, pady=5)
    last_name_entry = ttk.Entry(farmer_window)
    last_name_entry.grid(row=2, column=1, pady=5)

    ttk.Label(farmer_window, text="Phone Number:").grid(row=3, column=0, pady=5)
    phone_number_entry = ttk.Entry(farmer_window)
    phone_number_entry.grid(row=3, column=1, pady=5)

    ttk.Label(farmer_window, text="City:").grid(row=4, column=0, pady=5)
    city_entry = ttk.Entry(farmer_window)
    city_entry.grid(row=4, column=1, pady=5)

    def save_farmer_details():
        farmer_window.destroy()
        return Farmer(
            first_name_entry.get(),
            last_name_entry.get(),
            phone_number_entry.get(),
            city_entry.get()
        )

    ttk.Button(farmer_window, text="Save", command=save_farmer_details).grid(row=5, column=0, columnspan=2, pady=10)

def create_event(farmer, volunteers):
    event_window = tk.Toplevel(root)
    event_window.title("Event Details")

    ttk.Label(event_window, text="Enter Event Details:").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(event_window, text="Event Name:").grid(row=1, column=0, pady=5)
    event_name_entry = ttk.Entry(event_window)
    event_name_entry.grid(row=1, column=1, pady=5)

    ttk.Label(event_window, text="Event Date:").grid(row=2, column=0, pady=5)
    event_date_entry = ttk.Entry(event_window)
    event_date_entry.grid(row=2, column=1, pady=5)

    ttk.Label(event_window, text="Event Description:").grid(row=3, column=0, pady=5)
    description_entry = ttk.Entry(event_window)
    description_entry.grid(row=3, column=1, pady=5)

    def save_event_details():
        event_window.destroy()
        event = Event(
            event_name_entry.get(),
            event_date_entry.get(),
            description_entry.get(),
            farmer
        )
        for volunteer in volunteers:
            event.add_volunteer(volunteer)

        # Display confirmation window
        display_confirmation_window(event)

    ttk.Button(event_window, text="Save", command=save_event_details).grid(row=4, column=0, columnspan=2, pady=10)

def display_confirmation_window(event):
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Volunteer Confirmations")

    ttk.Label(confirmation_window, text=f"Volunteer Confirmations for Event '{event.event_name}':").grid(row=0, column=0, columnspan=2, pady=10)

    for i, volunteer in enumerate(event.volunteers, start=1):
        ttk.Label(confirmation_window, text=f"{i}. {volunteer.first_name} {volunteer.last_name}:", anchor="e").grid(row=i, column=0, padx=5, pady=5)
        ttk.Entry(confirmation_window, textvariable=tk.StringVar(value=volunteer.confirmation), state="readonly", width=10, justify="center").grid(row=i, column=1, padx=5, pady=5)

    # Send message to farmer based on volunteer confirmations
    send_message_to_farmer(event)

    ttk.Button(confirmation_window, text="Close", command=confirmation_window.destroy).grid(row=len(event.volunteers) + 1, column=0, columnspan=2, pady=10)

def send_message_to_farmer(event):
    confirmed_volunteers = [volunteer for volunteer in event.volunteers if volunteer.confirmation.lower() == "yes"]

    if confirmed_volunteers:
        message = f"Confirmed arrivals for event '{event.event_name}':\n"
        for volunteer in confirmed_volunteers:
            message += f"{volunteer.first_name} {volunteer.last_name}\n"

            # Send a message to the farmer for each confirmed volunteer
            send_confirmation_message_to_farmer(volunteer)

        messagebox.showinfo("Confirmed Arrivals", message)
    else:
        messagebox.showinfo("No Confirmations", "No volunteers confirmed their arrival for the event.")

def send_confirmation_message_to_farmer(volunteer):
    farmer_message = f"{volunteer.first_name} {volunteer.last_name} has confirmed his presence."
    # You can replace the following line with the method you prefer to notify the farmer
    messagebox.showinfo("Volunteer Confirmation", farmer_message)

def confirm_arrival(volunteer):
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirm Arrival")

    ttk.Label(confirmation_window, text=f"Confirm arrival for {volunteer.first_name} {volunteer.last_name}?").grid(row=0, column=0, columnspan=2, pady=10)

    def set_confirmation(value):
        volunteer.confirmation = value
        confirmation_window.destroy()

        # Send confirmation message to farmer if the volunteer confirms arrival
        if value.lower() == "yes":
            send_confirmation_message_to_farmer(volunteer)

    ttk.Button(confirmation_window, text="Yes", command=lambda: set_confirmation("yes")).grid(row=1, column=0, pady=10)
    ttk.Button(confirmation_window, text="No", command=lambda: set_confirmation("no")).grid(row=1, column=1, pady=10)

# Main application
root = tk.Tk()
root.title("Event Management Application")

ttk.Button(root, text="Enter Volunteer Details", command=get_volunteer_details).pack(pady=10)
ttk.Button(root, text="Enter Farmer Details", command=get_farmer_details).pack(pady=10)
ttk.Button(root, text="Create Event", command=lambda: create_event(None, [])).pack(pady=10)
ttk.Button(root, text="Confirm Arrival", command=lambda: confirm_arrival(Volunteer("Sample", "Volunteer", "", ""))).pack(pady=10)

root.mainloop()

