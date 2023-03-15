from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website_data = input_website.get()
    email_data = input_emaiL_name.get()
    password_data = input_password.get()

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message=f"Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"These are the details entered: \nEmail: {email_data}"
                                               f"\nPassword: {password_data} \nIs it okay to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.writelines(f"{website_data} | {email_data} | {password_data}\n")
                input_website.delete(0, "end")
                input_password.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#create labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_name_label = Label(text="Email/Username:")
email_name_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#create entries
input_website = Entry(width=36)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_emaiL_name = Entry(width=36)
input_emaiL_name.grid(column=1, row=2, columnspan=2)
input_emaiL_name.insert(0, "dev.theokim@gmail.com")

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

#create buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()