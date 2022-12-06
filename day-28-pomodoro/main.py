import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="25:00")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        timer_label.config("Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN*60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    mins, secs = divmod(count, 60)
    timer_prompt = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text, text=timer_prompt)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            current_text = check_marks["text"]
            updated_text = current_text + "✓"
            check_marks.config(text=updated_text)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 19, "bold"))
timer_label.grid(column=1, row=0)

check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=4)

start_button = tk.Button(text="Start", font=(FONT_NAME, 10, "italic"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 10, "italic")  , command=reset_timer)
reset_button.grid(column=2, row=3)

window.mainloop()
