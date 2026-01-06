import tkinter 

def button_click():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked.")
    
window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)

# Label 
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack() # packer to pack a label, when using grid don't use pack
my_label.grid(column=0, row=0)

# Button 1
button = tkinter.Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1)

# Button 2
new_button = tkinter.Button(text='Click Me')
new_button.grid(column=2, row=0)

input = tkinter.Entry()
# input.pack()
input.grid(column=2, row=2)

# this keeps the window running 
window.mainloop()