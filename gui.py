# Python program to generate random
# password using Tkinter module
import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
# Function for calculation of password
def low():
	entry.delete(0, END)

	# Get the length of passowrd
	length = var1.get()

	lowSecutiy = "abcdefghijklmnopqrstuvwxyz"
	mediumSecurity = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	highSecurity = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
	password = ""

	# if strength selected is low
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lowSecutiy)
		return password

	# if strength selected is medium
	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(mediumSecurity)
		return password

	# if strength selected is strong
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(highSecurity)
		return password
	else:
		print("Please choose an option")


# Function for generation of password
def generate():
	password1 = low()
	entry.insert(10, password1)


# Function for copying password to clipboard
def save():
	url_target = url.get()
	Username = user.get()
	random_password = entry.get()
	f= open(Username+".txt", "a+")
	f.write("Your targeted URL: "+url_target+"\r\n"+"Your UserName: "+Username+"\r\n"+"Your Password: "+random_password+"\r\n")
	messagebox.showinfo("Credentials Saved", "Your Credentials are saved.")
# Main Function

# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()
# Title of your GUI window
root.title("Random Password Generator")
# TYPE URL
url_target = Label(root, text="URL")
url_target.grid(row=0)
url = Entry(root)
url.grid(row=0, column=1)

#TYPE USER name
Username = Label(root, text= "UserName/Email")
Username.grid(row=1)
user = Entry(root)
user.grid(row=1, column=1)

# create label and entry to show
# password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=2)
entry = Entry(root)
entry.grid(row=2, column=1)

# create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=3)

# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="save", command=save)
copy_button.grid(row=4)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=2, column=2)

# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=3, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=3)
radio_middle.grid(row=3, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=0)
radio_strong.grid(row=3, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=3)

# start the GUI
root.mainloop()
