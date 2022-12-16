import tkinter as tk
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
FONT_NAME = "Ariel"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_master = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 15, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=900, height=750, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            450, 375,
            text="Espanol",
            font=(FONT_NAME, 15, "italic"),
            width=800
            )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_image = tk.PhotoImage(file="images/false.png")
        true_image = tk.PhotoImage(file="images/true.png")
        self.false_button = tk.Button(
            image=false_image,
            highlightthickness=0,
            command=lambda: self.press_button(False)
            )
        self.false_button.grid(column=1, row=2)
        self.true_button = tk.Button(
            image=true_image,
            highlightthickness=0,
            command=lambda: self.press_button(True)
            )
        self.true_button.grid(column=0, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz_master.still_has_question():
            question_text = self.quiz_master.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the Quiz. You're final score: {self.quiz_master.score}/{self.quiz_master.question_number}",
                )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_button(self, answer: bool):
        if answer:
            is_right = self.quiz_master.check_answer("true")
        else:
            is_right = self.quiz_master.check_answer("false")
        if is_right:
            self.canvas.configure(bg="green")
            print("green")
        else:
            self.canvas.configure(bg="red")
            print("red")
        self.window.after(200, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz_master.score}")
