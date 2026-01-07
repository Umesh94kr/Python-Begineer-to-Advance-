
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(10)

def reset_timer():
    count=0
    canvas.itemconfig(timer_text, text=count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time 

def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import * 
import os
BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
IMG_PATH = os.path.join(BASE_DIR, 'tomato.png')

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=IMG_PATH)
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(
    103, 112,
    text="00:00",
    font=("Helvetica", 44, "bold"),
    fill="white",
    anchor="center"
)
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="✔️", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)


window.mainloop()