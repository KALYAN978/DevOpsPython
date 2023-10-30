from tkinter import *  #tkinter is used for creating graphical user interface
from tkinter import messagebox  #its a module not a class
from random import choice, randint, shuffle
import pyperclip
import json


#----------Password Generator

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(8, 10)]
    password_symbols = [choice(symbols) for _ in range(2, 4)]
    password_numbers = [choice(numbers) for _ in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    """
    password_list = []    #storing password in a list

    for char in range(nr_letters):
    password_list.a ppend(random.choice(letters))

    for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

    for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    """

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
#-----------Password-------



def save():
    website = website_entry.get()  #holding data in entries or BOXES
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=f"Entries/Boxes cannot be empty")
    else:
        try:
            with open("data.json","r") as data_file:  # "w" =write mode #with (with)file we dont need to write f.close()
                #json.dump(new_data, data_file, indent=4)    #(data, file) --> indent: No. of spaces to indent on the json data
                #Reading the old data
                data = json.load(data_file)  # it takes the json data and converts it into a Python dictionary
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new Data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving the updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)  # Inorder delete the entered data in UI
            password_entry.delete(0, END)
            # after holding the data we r saving into the file



    # if len(website) == 0 or len(password) == 0:
    #     messagebox.showinfo(title="Oops", message=f"Entries/Boxes cannot be empty")
    # else:
    #     #creating the popbox
    #     # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
    #     #                                           f"\nPassword: {password} \nIs it ok to save?")
    #
    #     if is_ok:
    #         with open("data.txt", "a") as data_file:  #"a" =append mode #with (with)file we dont need to write f.close()
    #             data_file.write(f"{website} | {email} | {password}\n")
    #             website_entry.delete(0,END)   #Inorder delete the entered data in UI
    #             password_entry.delete(0,END)
    #             # after holding the data we r saving into the file


#====================FIND PASSWORD ====================

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file doesnot exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} exists")




#==================UI SETUP=============

window = Tk()  #creating a window
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)  #we adding padding by using config


canvas = Canvas(height=200, width =200)
logo_img = PhotoImage(file = "logo.png")   #importing image from photo image class
canvas.create_image(100, 100, image = logo_img)   #placing image inside the canvas
#canvas.pack()   #layout or dimension
canvas.grid(row=0, column=1)


#create Labels or names
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column =0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries nothing but boxes
website_entry = Entry(width=17)   #width is the property of entry class
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "kalyan@gmail.com")  	#Index - where to insert the text
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1,)


#Buttons
search_button = Button(text = "Search",width=14, command=find_password)
search_button.grid(row=1,column=2)
generate_password_button = Button(text="Generate Password", command = generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4,column=1, columnspan=2)



window.mainloop()   #window will start from mainloop
