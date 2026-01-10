from tkinter import * 
from tkinter import messagebox
import random
import json
import os
BASE_DIR = os.path.dirname(__file__)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Capital letters (A–Z)
capital_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# Small letters (a–z)
small_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# Symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '+', '=', '{', '}', '[', ']', '|',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
]

# Numbers
numbers = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]


def random_password():
    global numbers 
    global symbols 
    global small_letters
    global capital_letters
    ###### total capitals, smalls, numbers, symbols we have
    total_capitals = len(capital_letters)
    total_smalls = len(small_letters)
    total_symbols = len(symbols)
    total_numbers = len(numbers) 

    num_capital_letters = random.randint(1, 4)
    num_small_letters = random.randint(1, 4)
    num_symbols = random.randint(1, 4)
    num_numbers = random.randint(1, 4)

    # IDEA - for each position of password we'll use random number from (1 to 4) 
    # if 1 we'll input a random Capital letter
    # if 2 we'll input a random Small letter 
    # if 3 we'll input a random Symbol letter
    # if 4 we'll input a random Number

    # Also keep track of whether number of characters user want is exceeded or not
    total_password_len = num_capital_letters + num_numbers + num_small_letters

    password_gen = ""
    password_len = 0
    while(password_len < total_password_len):
        # what to put at this position - Capital_letter (1), Small_letter (2), Symbol (3), Number (4)
        random_num = random.randint(1, 4)
        if random_num == 1:
            if num_capital_letters > 0:
                idx = random.randint(0, total_capitals-1)
                password_gen += capital_letters[idx]
                num_capital_letters -= 1
                password_len += 1
            else:
                continue 
        elif random_num == 2:
            if num_small_letters > 0:
                idx = random.randint(0, total_smalls-1)
                password_gen += small_letters[idx]
                num_small_letters -= 1
                password_len += 1
            else:
                continue
        elif random_num == 3:
            if num_symbols > 0:
                idx = random.randint(0, total_symbols-1)
                password_gen += symbols[idx]
                num_symbols -= 1
                password_len += 1
            else:
                continue
        elif random_num == 4:
            if num_numbers > 0:
                idx = random.randint(0, total_numbers-1)
                password_gen += str(numbers[idx])
                num_numbers -= 1
                password_len += 1
            else:
                continue
    print(f"Password : {password_gen}")
    password_var.set(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    DATA_FILE = os.path.join(BASE_DIR, 'data_json.json')
    email = email_input.get()
    website = website_input.get()
    password = password_var.get()

    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if not email or not website or not password:
        messagebox.showwarning(title="Empty Fields", message=f"Some fields are empty. Please fill them and then submit!")
        return

    is_ok = messagebox.askyesno(title="Saving Data", message=f"Do you really want to save the data?\n Email : {email}\n Website : {website}\n Password : {password}")

    if is_ok:
        # Step 1: Load existing data
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError as e:
            print(f"File : {e} not found.")
            print("creating new file")
            with open(DATA_FILE, "w") as file:
                data = {}
                json.dump(data, file)
        
        # Step 2: Update data
        data.update(new_data)

        # Step 3: Write back to file
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    
        # once details are saved make reset all the inputs 
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_var.set("")

def search_data():
    DATA_FILE = os.path.join(BASE_DIR, 'data_json.json')

    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
    except Exception as e:
        print(f"File not found : {e}")
        with open(DATA_FILE, "w") as file:
                data = {}
                json.dump(data, file)
    
    website_name = website_input.get()
    try:
        details = data[website_name]
    except KeyError as e:
        print(f"This website not exists for you : {e}")
        messagebox.showinfo(title="Website pasword", message=f"This website not exists. for you {website_name}")
    else:
        messagebox.showinfo(title="Website pasword", message=f"Email/Username : {details['email']},\n Password : {details['password']}")




# ---------------------------- UI SETUP ------------------------------- #
IMG_PATH = os.path.join(BASE_DIR, 'logo.png')

window = Tk()
window.config(padx=20, pady=10)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=IMG_PATH)
canvas.create_image(103, 112, image=logo_img)
canvas.grid(row=0, column=1)

# input block 1 
website = Label(text="Website")
website.grid(row=1, column=0)

website_input = Entry()
website_input.grid(column=1, row=1)

# search button
save_button = Button(text="Search", command=search_data, width=20)
save_button.grid(row=1, column=2)

# input block 2
email = Label(text="Email")
email.grid(row=2, column=0)

email_input = Entry()
email_input.grid(row=2, column=1)

# input block 3
password = Label(text="Password")
password.grid(row=3, column=0)

password_var = StringVar()
password_input = Entry(textvariable=password_var)
password_input.grid(row=3, column=1)

# button to generate 
generate_password = Button(text="Generate password", command=random_password)
generate_password.grid(row=3, column=2)

# button to add the details to .txt
save_button = Button(text="Save Details", command=save_details, width=20)
save_button.grid(row=4, column=1)

window.mainloop()