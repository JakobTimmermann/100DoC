import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- SEARCH ENTRIES ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tk.messagebox.showerror(title="Ooops", message="No Data File Found")
    else:
        if website in data.keys():
            password = data[website]["password"]
            email = data[website]["email"]
            tk.messagebox.showinfo(title=website, message=f"EMail/User:{email}\nPassword:{password}")
        else:
            tk.messagebox.showinfo(title=website, message=f"No details for {website} found")



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
    email = user_entry.get()

    if len(website) == 0 or len(password) == 0:
        tk.messagebox.showerror(title="Ooops", message="Please do not leave any field empty!")
    else:

        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            if website in data:
                current_password = data[website]["password"]
                update_entry = tk.messagebox.askokcancel(
                                    title="Repetition detected",
                                    message=f"{website} already in database."
                                            f"Do you want to update old password ({current_password})?",
                                    )
        except FileNotFoundError:
            pass
        if not update_entry:
            website_entry.delete(0, 'end')
            website_entry.focus()
            user_entry.delete(0, 'end')
            user_entry.insert(0, "jakob.ch.timmermann@gmail.com")
            password_entry.delete(0, 'end')
            return 0

        is_okay = tk.messagebox.askokcancel(
                                  title=website,
                                  message=f"These are the details:\n"
                                          f"EMail: {email}\n"
                                          f"Password: {password}\n"
                                          f"Is this okay to save?"
                                           )
        if is_okay:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=True)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=True)
            finally:
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

website_entry = tk.Entry(width=19, justify='left')
website_entry.grid(column=1, row=1)
website_entry.focus()

user_entry = tk.Entry(width=35, justify='left')
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "jakob.ch.timmermann@gmail.com")

password_entry = tk.Entry(width=19, justify='left')
password_entry.grid(column=1, row=3)

search_button = tk.Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

generate_button = tk.Button(text="Generate", width=14, command=password_generator)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=34, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

tk.mainloop()