import tkinter as tk
import choice_page
import code

# Dummy function to verify team member login
def verify_login(username, password, project_title):
    # Replace this logic with your actual verification process
    if (username == "team_member1" and password == "password1" and project_title == "project1") or \
       (username == "team_member2" and password == "password2" and project_title == "project1") or \
       (username == "team_member3" and password == "password3" and project_title == "project1") or \
       (username == "team_member4" and password == "password4" and project_title == "project1"):
        return True
    else:
        return False

def go_back(window):
    window.destroy()
    choice_page.open_choice_page()

def open_code_page(window):
    window.destroy()
    code.open_code_page("team_member")

def open_team_member_login_page():
    window = tk.Tk()
    window.title("Team Member Login")

    username_label = tk.Label(window, text="Team Member Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(window, text="Team Member Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    project_title_label = tk.Label(window, text="project name:")
    project_title_label.grid(row=2, column=0, padx=10, pady=5)
    project_title_entry = tk.Entry(window)
    project_title_entry.grid(row=2, column=1, padx=10, pady=5)

    error_label = tk.Label(window, text="", fg="red")
    error_label.grid(row=3, columnspan=2, padx=10, pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        project_title = project_title_entry.get()
        if verify_login(username, password, project_title):
            open_code_page(window)
        else:
            error_label.config(text="Invalid username or password")

    login_button = tk.Button(window, text="Login", command=login)
    login_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(window, text="Back", command=lambda: go_back(window))
    back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

# Call the function to open the login page
# open_team_member_login_page()
