import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

import tkinter as tk


form = tk.Tk()
form.title("Form")
form.columnconfigure([0,1,2,3], weight = 1, minsize=75)
form.rowconfigure([0,1,2], weight = 1, minsize=100)

nameFrame = tk.Frame(
    master = form,
    relief = tk.RAISED,
    borderwidth = 5
    )
nameFrame.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = "nsew")
name = tk.Label(
    master = nameFrame,
    text = "Name: ",
    bg = "white",
    fg = "black",
    width = 8
)
name.pack()
name_e = tk.Entry(master = nameFrame)
name_e.pack(fill = tk.X)



ad1Frame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
ad1Frame.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = "nsew")
addressLine1 = tk.Label(
    master = ad1Frame,
    text = "Address Line 1: ",
    bg = "black",
    fg = "white",
    width = 17
)
addressLine1.pack()
addressLine1_e =tk.Entry(master = ad1Frame)
addressLine1_e.pack(fill = tk.X)



ad2Frame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
ad2Frame.grid(row = 2, column = 0, padx = 0, pady = 0, sticky = "nsew")
addressLine2 = tk.Label(
    master = ad2Frame,
    text = "Address Line 2: ",
    bg = "white",
    fg = "black",
    width = 17
)
addressLine2.pack()
addressLine2_e =tk.Entry(master=ad2Frame)
addressLine2_e.pack(fill = tk.X)



cityFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
cityFrame.grid(row = 3, column = 0, padx = 0, pady = 0, sticky = "nsew")
city = tk.Label(
    master=cityFrame,
    text = "City: ",
    bg = "black",
    fg = "white",
    width = 6
)
city.pack()
city_e =tk.Entry(master=cityFrame)
city_e.pack(fill = tk.X)



stateFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
stateFrame.grid(row = 0, column = 1, padx = 0, pady = 0, sticky = "nsew")
state = tk.Label(
    master=stateFrame,
    text = "State: ",
    bg = "white",
    fg = "black",
    width = 7
)
state.pack()
state_e =tk.Entry(master=stateFrame)
state_e.pack(fill = tk.X)



zipFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
zipFrame.grid(row = 1, column = 1, padx = 0, pady = 0, sticky = "nsew")
zipCode = tk.Label(
    master=zipFrame,
    text = "Zip Code: ",
    bg = "black",
    fg = "white",
    width = 7
)
zipCode.pack()
zipCode_e =tk.Entry(master=zipFrame)
zipCode_e.pack(fill = tk.X)



phoneFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
phoneFrame.grid(row = 2, column = 1, padx = 0, pady = 0, sticky = "nsew")
phoneNumber = tk.Label(
    master=phoneFrame,
    text = "Phone Number: ",
    bg = "white",
    fg = "black",
    width = 14
)
phoneNumber.pack()
phoneNumber_e =tk.Entry(master=phoneFrame)
phoneNumber_e.pack(fill = tk.X)



emailFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
emailFrame.grid(row = 3, column = 1, padx = 0, pady = 0, sticky = "nsew")
emailAddress = tk.Label(
    master=emailFrame,
    text = "Email Address: ",
    bg = "black",
    fg = "white",
    width = 17
)
emailAddress.pack()
emailAddress_e =tk.Entry(master=emailFrame)
emailAddress_e.pack(fill = tk.X)



def print_form():
    n = name_e.get()
    print(n)
    a1 = addressLine1_e.get()
    print(a1)
    a2 = addressLine2_e.get()
    print(a2)
    c = city_e.get()
    print(c)
    s = state_e.get()
    print(s)
    z = zipCode_e.get()
    print(z)
    num = phoneNumber_e.get()
    print(num)
    e = emailAddress_e.get()
    print(e)

submitFrame = tk.Frame(
    master = form,
    relief =tk.RAISED,
    borderwidth = 5
)
submitFrame.grid(row = 1, column = 2, padx = 0, pady = 0, sticky = "nsew")
submit =tk.Button(
    master=submitFrame,
    text = "Submit",
    bg = "white",
    fg = "black",
    command = print_form
)
submit.pack()
submit.pack(fill = tk.X)


form.mainloop()