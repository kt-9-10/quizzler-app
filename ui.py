from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Courier"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # labels
        self.score_label = Label(text="Score:", font=(FONT_NAME, 12, "bold"))
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  relief="flat", bg=THEME_COLOR, command=self.push_true)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,
                                   relief="flat", bg=THEME_COLOR, command=self.push_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.score_label.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")

        if self.quiz.still_has_questions():
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def push_true(self):
        # is_correct = self.quiz.check_answer("true")
        self.give_feedback(self.quiz.check_answer("true"))

    def push_false(self):
        # is_correct = self.quiz.check_answer("false")
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white", text="Correct!")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white", text="Mistake...")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        self.window.after(1000, self.get_next_question)

