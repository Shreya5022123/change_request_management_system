import tkinter as tk
import admin_choice # Import the module containing the first admin page function
import team_member_page  # Import the module containing the second admin page function

def save_changes():
    # Functionality for saving changes
    print("Changes saved.")

def go_back(window, previous_page):
    # Functionality for going back to the previous page
    window.destroy()  # Close the current window

    if previous_page == "admin":
        admin_choice.open_admin_choice_page()  # Open admin choice page
    elif previous_page == "team_member":
        team_member_page.open_team_member_login_page()  # Open the team_member_login page

def open_code_page(previous_page):
    window = tk.Tk()
    window.geometry("650x510")  # Change the size of the window
    window.title("Code Page")  # Add a title to the window

    # Dividing the window into three parts vertically
    top_frame = tk.Frame(window, height=70, bg="yellow")  # Reduced height to 40 pixels
    top_frame.grid(row=0, column=0, sticky="ew")

    mid_frame = tk.Frame(window, bg="white")  # 100% of the screen
    mid_frame.grid(row=1, column=0, sticky="nsew")

    bottom_frame = tk.Frame(window, height=40, bg="blue")  # Reduced height to 40 pixels
    bottom_frame.grid(row=2, column=0, sticky="ew")

    # Components for mid_frame
    mid_scrollbar_y = tk.Scrollbar(mid_frame, orient="vertical")
    mid_scrollbar_x = tk.Scrollbar(mid_frame, orient="horizontal")
    mid_text = tk.Text(mid_frame, wrap="none", yscrollcommand=mid_scrollbar_y.set, xscrollcommand=mid_scrollbar_x.set)

    mid_text.grid(row=0, column=0, sticky="nsew")
    mid_scrollbar_y.grid(row=0, column=1, sticky="ns")
    mid_scrollbar_x.grid(row=1, column=0, sticky="ew")

    mid_scrollbar_y.config(command=mid_text.yview)
    mid_scrollbar_x.config(command=mid_text.xview)

    # Components for bottom_frame
    bottom_frame_top = tk.Frame(bottom_frame, bg="blue")  # Create a frame within bottom_frame
    bottom_frame_top.pack(fill="both", expand=True)

    save_button = tk.Button(bottom_frame_top, text="Save", bg="lightgrey", fg="black", width=15, command=save_changes)  # Increase the width
    save_button.pack(side="left", padx=20, pady=5)

    back_button = tk.Button(bottom_frame_top, text="Back", bg="lightgrey", fg="black", width=15, command=lambda: go_back(window, previous_page))  # Increase the width
    back_button.pack(side="right", padx=20, pady=5)

    # Components for top_frame
    # Add any components you want to display in the top_frame here

    print("Opening next page...")
    window.mainloop()


