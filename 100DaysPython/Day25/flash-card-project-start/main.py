import os 
from tkinter import * 
import random

BACKGROUND_COLOR = "#B1DDC6"
BASE_DIR = os.path.dirname(__file__)
random_key = "key"
CORRECT = 0

########### READING DATA ######################
import pandas as pd 

df = pd.read_csv(os.path.join(BASE_DIR, 'data/french_words.csv'))
data_dict = {row[1].French : row[1].English for row in df.iterrows()}

list_keys = [key for key, value in data_dict.items()]

########## INVERT THE CARD ################
def get_answer():
    global random_key
    global list_keys
    list_keys.append(random_key)
    window.after(1000)
    canvas.itemconfig(image, image=card_back_img)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=data_dict[random_key], fill='white')

########## NEXT CARD ################
def get_next():
    global CORRECT
    global random_key
    global list_keys
    text_value = canvas.itemcget(title_text, "text")
    if text_value == "French":
        CORRECT += 1
    score.config(text=CORRECT)
    window.after(1000)
    canvas.itemconfig(image, image=card_front_img)
    canvas.itemconfig(title_text, text='French', fill='black')
    random_key = random.choice(list_keys)
    list_keys.remove(random_key)
    canvas.itemconfig(word_text, text=random_key, fill='black')


########### MAKING UI #########################

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

score_text = Label(text="SCORE : ", font=("Courier", 50))
score_text.grid(row=1, column=2)

score = Label(text=CORRECT, font=("Courier", 50))
score.grid(row=1, column=3)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=os.path.join(BASE_DIR, "images/card_front.png"))
card_back_img = PhotoImage(file=os.path.join(BASE_DIR, "images/card_back.png"))

random_key = random.choice(list_keys)
list_keys.remove(random_key)

image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill='black')
word_text = canvas.create_text(400, 263, text=random_key, font=("Ariel", 60, "bold"), fill='black')
canvas.grid(row=0, column=1, columnspan=2)

# creating the cross button - when user don't know the answer
cross_img = PhotoImage(file=os.path.join(BASE_DIR, "images/wrong.png"))
cross_button = Button(image=cross_img, highlightthickness=0, command=get_answer)
cross_button.grid(row=1, column=0)

# creating the tick button - when user know the answer
tick_img = PhotoImage(file=os.path.join(BASE_DIR, "images/right.png"))
tick_button = Button(image=tick_img, highlightthickness=0, command=get_next)
tick_button.grid(row=1, column=1)

window.mainloop()