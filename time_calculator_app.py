import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Function to calculate the time difference
def calculate_time_difference():
    try:
        start_time_str = start_time_entry.get()
        end_time_str = end_time_entry.get()

        # Handle "now" input for end time
        if end_time_str.lower() == "now":
            end_time = datetime.now()
        else:
            # Convert the entered end time to datetime
            end_time = datetime.strptime(end_time_str, "%d %B %Y %I:%M %p")

        # Convert the entered start time to datetime
        start_time = datetime.strptime(start_time_str, "%d %B %Y %I:%M %p")

        # Calculate the difference
        time_difference = end_time - start_time

        # Format the difference
        days = time_difference.days
        seconds = time_difference.seconds
        hours, minutes = divmod(seconds, 3600)

        result_label.config(text=f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid date and time in the format: '28 October 2024 3:45 PM'")


# Function to set the end time to the current time
def set_now():
    now = datetime.now().strftime("%d %B %Y %I:%M %p")
    end_time_entry.delete(0, tk.END)  # Clear the entry field
    end_time_entry.insert(0, now)  # Insert the current datetime


# Set up the main window
root = tk.Tk()
root.title("Time Difference Calculator")

# Create a frame to hold the widgets with larger size
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=40, pady=40)

# Start time input label and entry field
start_time_label = tk.Label(frame, text="Enter start time (e.g., 28 October 2024 3:45 PM):", font=("Helvetica", 12))
start_time_label.grid(row=0, column=0, sticky="w", pady=10)
start_time_entry = tk.Entry(frame, width=40, font=("Helvetica", 12))
start_time_entry.grid(row=0, column=1, pady=10)

# End time input label and entry field
end_time_label = tk.Label(frame, text="Enter end time (e.g., 12 November 2024 12:00 PM or 'now'):",
                          font=("Helvetica", 12))
end_time_label.grid(row=1, column=0, sticky="w", pady=10)
end_time_entry = tk.Entry(frame, width=40, font=("Helvetica", 12))
end_time_entry.grid(row=1, column=1, pady=10)

# Button to set end time to current time
now_button = tk.Button(frame, text="Set End Time to Now", command=set_now, font=("Helvetica", 12), bg="#2196F3",
                       fg="white", padx=20, pady=10)
now_button.grid(row=2, column=0, columnspan=2, pady=10)

# Button to calculate time difference
calculate_button = tk.Button(frame, text="Calculate", command=calculate_time_difference, font=("Helvetica", 12),
                             bg="#4CAF50", fg="white", padx=20, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(frame, text="", font=("Helvetica", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
