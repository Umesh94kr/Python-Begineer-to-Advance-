from tkinter import * 

def button_click():
    print("I got clicked.")
    miles = float(input_miles.get())
    print(f"Miles : {miles}")
    kms = miles * 1.60934
    output_label.config(text=f"{round(kms, 2)}")
    return kms

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=500, height=300)

# text for input miles 
my_label1 = Label(text="Miles", font=("Arial", 24, "bold"))
my_label1.grid(column=0, row=0)

# text to display 
my_label2 = Label(text='kms', font=("Arial", 24, "bold"))
my_label2.grid(column=0, row=2)

# input block 1 (taking miles)
input_miles = Entry()
input_miles.grid(column=1, row=0)

# output block (giving converted miles in km)
output_label = Label(text="", font=("Arial", 14))
output_label.grid(row=2, column=1)

# convert button
convert_button = Button(text="Convert", command=button_click)
convert_button.grid(column=1, row=1)

window.mainloop()
