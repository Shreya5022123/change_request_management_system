import tkinter as tk
import admin_choice
import choice_page

def go_back(window):
    window.destroy()
    choice_page.open_choice_page()

def verify_login(username, password, project_title):
    if username == "admin" and password == "password" and project_title == "project1":
        return True
    else:
        return False

def login(username, password, project_title, window, error_label):
    if verify_login(username, password, project_title):
        window.destroy()
        admin_choice.open_admin_choice_page()
    else:
        error_label.config(text="Invalid username or password")

def open_admin_login_page():
    window = tk.Tk()
    window.title("Admin Login")

    username_label = tk.Label(window, text="Admin Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(window, text="Admin Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    project_title_label = tk.Label(window, text="Project Name:")
    project_title_label.grid(row=2, column=0, padx=10, pady=5)
    project_title_entry = tk.Entry(window)
    project_title_entry.grid(row=2, column=1, padx=10, pady=5)

    error_label = tk.Label(window, text="", fg="red")
    error_label.grid(row=3, columnspan=2, padx=10, pady=5)

    login_button = tk.Button(window, text="Login", command=lambda: login(username_entry.get(), password_entry.get(), project_title_entry.get(), window, error_label))
    login_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(window, text="Back", command=lambda: go_back(window))
    back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

open_admin_login_page()
