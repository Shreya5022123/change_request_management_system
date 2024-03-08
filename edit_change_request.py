import tkinter as tk
from tkinter import messagebox
import admin_choice

def open_admin_choice(window):
    window.destroy()
    admin_choice.open_admin_choice_page()

def save_change_request():
    # Functionality for saving change request
    change_request_text = change_request_entry.get("1.0", "end-1c")  # Get text from the text box
    deadline_date = deadline_entry.get()  # Get text from the entry for deadline
    messagebox.showinfo("Saved", "Change request saved successfully!")

def delete_change_request():
    # Functionality for deleting change request
    change_request_text = change_request_entry.get("1.0", "end-1c")  # Get text from the text box
    deadline_date = deadline_entry.get()  # Get text from the entry for deadline
    # Implement deletion logic here
    messagebox.showinfo("Deleted", "Change request deleted successfully!")

def open_edit_change_request_page():
    window = tk.Tk()
    window.title("Change Request Page")

    # Label and Textbox for Change Request
    change_request_label = tk.Label(window, text="Change Request:")
    change_request_label.pack(pady=(10, 5))
    change_request_entry = tk.Text(window, height=5, width=40)
    change_request_entry.pack(pady=(0, 10))

    # Label and Entry for Deadline
    deadline_label = tk.Label(window, text="Deadline (Date):")
    deadline_label.pack(pady=(10, 5))
    deadline_entry = tk.Entry(window)
    deadline_entry.pack(pady=(0, 10))

    # Button to Save Change Request
    save_button = tk.Button(window, text="Save", command=save_change_request)
    save_button.pack(side="left", padx=(20, 10))

    # Button to Delete Change Request
    delete_button = tk.Button(window, text="Delete", command=delete_change_request)
    delete_button.pack(side="left", padx=(10, 20))

    # back button
    back_button = tk.Button(window, text="back", command=lambda: open_admin_choice(window))
    back_button.pack(side="left", padx=(100, 20))

    window.mainloop()

# open_edit_change_request_page()
