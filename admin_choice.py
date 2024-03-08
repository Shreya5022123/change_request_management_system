import tkinter as tk
import code
import edit_change_request

def open_code_page(window):
    window.destroy()
    code.open_code_page("admin")

def open_add_change_request():
    # Functionality for adding change request
    print("Adding change request...")

def open_edit_change_request():
    # Functionality for editing change request
    print("Editing change request...")

def open_delete_change_request():
    # Functionality for deleting change request
    print("Deleting change request...")

def open_admin_login_page_and_close_current(window):
    import admin_page
    window.destroy()
    admin_page.open_admin_login_page()

def open_admin_choice_page():
    window = tk.Tk()
    window.title("Admin Choice Page")

    # Button for editing code
    edit_code_button = tk.Button(window, text="Edit Code", command=lambda: open_code_page(window))

    edit_code_button.pack(pady=10)

    # Button for editing change request
    edit_change_request_button = tk.Button(window, text="Edit Change Request", command=edit_change_request.open_edit_change_request_page)
    edit_change_request_button.pack(pady=10)

    # back button
    back_button = tk.Button(window, text="back", command=lambda: open_admin_login_page_and_close_current(window))
    back_button.pack(pady=10)

    window.mainloop()

# open_admin_choice_page()
