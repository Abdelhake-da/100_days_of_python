from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain, nb_question: int):
        # variable
        self.quiz = quiz
        # window
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.nb_question = nb_question
        # score label
        self.score_label = Label(text=f'Score: 0/{nb_question}', fg='white', bg=THEME_COLOR)
        self.score_label.config()
        self.score_label.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='hola',
            fill=THEME_COLOR,
            font=('Arial', 15, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)
        self.change_question()
        # button true
        true_image = PhotoImage(file='images/true.png')
        self.true_b = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_b.grid(column=0, row=2)
        # button false
        false_image = PhotoImage(file='images/false.png')
        self.false_b = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_b.grid(column=1, row=2)
        self.window.mainloop()

    def change_question(self):
        if self.quiz.question_number < self.nb_question:
            self.change_score(self.quiz.score)
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.change_score(self.quiz.score)
            self.true_b.config(state='disabled')
            self.false_b.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text=f'You\'ve completed the quiz\n'
                                                            f'Your final score was: {self.quiz.score}/{self.nb_question}')
        self.canvas.config(bg='white')

    def change_score(self, num: int):
        txt = f'Score: {num}/{self.nb_question}'
        self.score_label.config(text=txt)

    def true_answer(self):
        self.check('true')

    def false_answer(self):
        self.check('false')

    def color_bg_change(self, txt: str):
        self.canvas.config(bg=txt)
        self.window.after(500, self.change_question)

    def check(self, answer):
        if self.quiz.check_answer(answer):
            self.color_bg_change('green')
        else:
            self.color_bg_change('red')
