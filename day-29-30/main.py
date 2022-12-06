import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(5, 7))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    user = user_entry.get()
    if len(website) == 0 or len(password) == 0:
        tk.messagebox.showerror(title="Ooops", message="Please do not leave any field empty!")
    else:
        is_okay = tk.messagebox.askokcancel(
                                  title=website,
                                  message=f"These are the details:\n"
                                          f"EMail: {user}\n"
                                          f"Password: {password}\n"
                                          f"Is this okay to save?"
                                           )
        if is_okay:
            with open("saved_passwords.csv", "a") as file:
                file.write(f"{website},{user},{password}\n")
            website_entry.delete(0, 'end')
            website_entry.focus()
            user_entry.delete(0, 'end')
            user_entry.insert(0, "jakob.ch.timmermann@gmail.com")
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=100, pady=100,)
window.option_add('*Dialog.msg.width', 34)
window.option_add('*Dialog.msg.font', 'Helvetica 10')

logo_img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

labels = {}
for n, element in enumerate(["Website", "EMail/Username", "Password"]):
    labels[element] = tk.Label(text=f"{element}:", anchor="w")
    labels[element].grid(column=0, row=n + 1, pady=10, padx=10)

website_entry = tk.Entry(width=35, justify='left')
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_entry = tk.Entry(width=35, justify='left')
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "jakob.ch.timmermann@gmail.com")

password_entry = tk.Entry(width=19, justify='left')
password_entry.grid(column=1, row=3)

generate_button = tk.Button(text="Generate", width=14, command=password_generator)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=34, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

tk.mainloop()