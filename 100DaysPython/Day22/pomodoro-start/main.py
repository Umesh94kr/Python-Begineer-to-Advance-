
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
is_start=True

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    title_label.config(text="Timer", fg=GREEN)
    global is_start
    is_start=False
    count=0
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global is_start 
    global reps
    if is_start == False:
        is_start = True 
        reps = 1
    
    if reps%2 == 0 and reps < 8:
        title_label.config(text="BREAK", fg=RED)
        count_down(minutes=5, seconds=0)
        reps += 1
    elif reps%2 != 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(minutes=WORK_MIN, seconds=0)
        reps += 1
    elif reps == 8:
        title_label.config(text="BREAK", fg=RED)
        count_down(minutes=20, seconds=0)
    else:
        print(f"Your session ended!")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time 

def count_down(minutes, seconds):
    global is_start
    if is_start:
        if int(seconds / 10) != 0:
            text = f"{minutes}:{seconds}"
        elif int(seconds/10) == 0:
            text = f"{minutes}:0{seconds}"
        else:
            text = f"{minutes}:{seconds}"
        canvas.itemconfig(timer_text, text=text)
        if minutes > 0 or (minutes == 0 and seconds > 0):
            if seconds > 0:
                window.after(1000, count_down, minutes, seconds-1)
            if seconds == 0:
                window.after(1000, count_down, minutes-1, 59)
        else:
            start_timer()

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