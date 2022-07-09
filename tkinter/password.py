import tkinter as tk
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_button():
    web_entry = website_entry.get()
    mail_entry = email_entry.get()
    pass_entry = password_entry.get()
    new_data = {
        web_entry: {
            "email": mail_entry,
            "password": pass_entry,
        }
    }
    if len(web_entry)==0 or len(mail_entry)==0 or len(pass_entry)==0 :
        messagebox.showinfo(message="Please don't leave any fields empty.")
    else:
        try:
            with open("tkinter/passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except json.JSONDecodeError:
            with open("tkinter/passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("tkinter/passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    try:
        with open("tkinter/passwords.json", "r") as file:
            data = json.load(file)
            email = data[website_entry.get()]["email"]
            password = data[website_entry.get()]["password"]
            messagebox.showinfo(message=f"Your info for {website_entry.get()} is: {email} {password}")
    except KeyError:
        messagebox.showinfo(message="This website doesn't have a password (yet).")
    except json.JSONDecodeError:
        messagebox.showinfo(message="No Data File Found...")

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="tkinter/logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)


website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus() #cursor directly goes there

website_search = tk.Button(text="Search", font=("Arial", 9), width=8, command=search)
website_search.grid(row=1, column=2)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "manon1606manon@gmail.com") #0 or END, preput something


password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=24)
password_entry.grid(row=3, column=1)

generate = tk.Button(text="Generate", font=("Arial", 9), width=8, command=generate_password)
generate.grid(row=3, column=2)


add = tk.Button(text="Add", width=36, font=("Arial", 10), command=add_button)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
