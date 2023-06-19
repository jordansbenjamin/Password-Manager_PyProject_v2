from tkinter import * # Only imports classes and constants
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ('Arial', 15)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    r_letter = [random.choice(letters) for char in range(nr_letters)]

    r_symbol = [random.choice(symbols) for symbol in range(nr_symbols)]

    r_number = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = r_letter + r_symbol + r_number

    random.shuffle(password_list)

    password = "".join(password_list)

    passw_input.delete(0, END)
    passw_input.insert(0, f"{password}")
    pyperclip.copy(password)
    messagebox.showinfo(message="Password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    data_lst = [web_input.get(), email_input.get(), passw_input.get()]
    data_lst.append("\n")
    data = " | ".join(str(value) for value in data_lst)
    
    if len(data_lst[0]) == 0 or len(data_lst[1]) == 0 or len(data_lst[2]) == 0:
        messagebox.askretrycancel(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=data_lst[0], message=f"These are the details entered: \nEmail: {data_lst[1]}" f"\nPassword: {data_lst[2]} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", 'a') as df:
                df.write(data)
                web_input.delete(0, END)
                email_input.delete(0, END)
                # email_input.insert(0, "name@email.com")
                passw_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo_canvas
canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website
# Label
web_label = Label(text="Website:", font=FONT)
web_label.grid(column=0, row=1)
# Website input
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2, sticky="EW")
web_input.focus()


# Email/username
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)
# Email input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "name@email.com")

# Password
# Label
passw_label = Label(text="Password:", font=FONT)
passw_label.grid(column=0, row=3)
# Password input
passw_input = Entry(width=21)
passw_input.grid(column=1, row=3, sticky="EW")

# Generate password button
generate_pw_btn = Button(text="Generate Password", width=11, command=generate_password)
generate_pw_btn.grid(column=2, row=3, sticky="EW")

# Add button
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()