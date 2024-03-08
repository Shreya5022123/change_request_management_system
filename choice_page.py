import tkinter as tk

def open_admin_login_page_and_close_current(window):
    import admin_page
    window.destroy()
    admin_page.open_admin_login_page()

def open_team_member_login_page_and_close_current(window):
    import team_member_page
    window.destroy()
    team_member_page.open_team_member_login_page()


def open_choice_page():
    window = tk.Tk()
    window.title("Login Choice")

    admin_button = tk.Button(window, text="Admin", command=lambda: open_admin_login_page_and_close_current(window))
    admin_button.pack(pady=10)

    team_member_button = tk.Button(window, text="Team Member", command=lambda: open_team_member_login_page_and_close_current(window))
    team_member_button.pack(pady=10)



    window.mainloop()
