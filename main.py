from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
import math

timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    shot_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(shot_break_sec)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


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
reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(highlightthickness=0)
reset_button.grid(row=2, column=2)
"""check_mark"""
check_mark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(row=3, column=1)

window.mainloop()
