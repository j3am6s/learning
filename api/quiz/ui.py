import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="This is the question",
            font=("Arial", 20), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.image_right = tk.PhotoImage(file="api/quiz/images/true.png")
        self.right = tk.Button(image=self.image_right, highlightthickness=0, command=self.right_pressed)
        self.right.grid(row=2, column=0)
        self.image_wrong = tk.PhotoImage(file="api/quiz/images/false.png")
        self.wrong = tk.Button(image=self.image_wrong, highlightthickness=0, command=self.wrong_pressed)
        self.wrong.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas["bg"] = "white"
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def wrong_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self, is_right):
        if is_right:
            self.canvas["bg"] = "green"
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas["bg"] = "red"
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
        
