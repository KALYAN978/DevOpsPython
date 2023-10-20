from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km =   miles * 1.609 #1 mile = 1.609km
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20,pady=20)  #padding by using config

#now we have to craete widgets and layed out screen
miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text = "Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text = "is_equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)   #command will trigger miles to km function
calculate_button.grid(column=1, row=2)                             #without () paranthesis bcoz we only get called when it get clicked



window.mainloop()