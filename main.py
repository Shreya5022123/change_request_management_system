import tkinter as tk


def open_choice_page_and_close_current():
    import choice_page
    window.destroy()
    choice_page.open_choice_page()


window = tk.Tk()
window.title("Main Page")

login_button = tk.Button(window, text="Click here to login", command=open_choice_page_and_close_current)
login_button.pack(pady=20)

window.mainloop()


