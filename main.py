from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

import math


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

"""canvas"""
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

"""Timer_label"""
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.config(bg=YELLOW, fg=GREEN, highlightthickness=0)
timer_label.grid(row=0, column=1)
"""start-button"""
start_button = Button(text="start", command=start_timer)
start_button.config(highlightthickness=0)
start_button.grid(row=2, column=0)

"""reset_button"""
reset_button = Button(text="Reset")
reset_button.config(highlightthickness=0)
reset_button.grid(row=2, column=2)
"""check_mark"""
check_mark = Label(text="✔", fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(row=3, column=1)

window.mainloop()
