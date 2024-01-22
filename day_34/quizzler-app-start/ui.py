from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="word", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_passed)
        self.true_button.grid(column=0, row=2)
        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_passed)
        self.false_button.grid(column=1, row=2)

        self.score = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You`ve reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_passed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_passed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
