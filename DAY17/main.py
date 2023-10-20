from data import question_data, question_data1
from quiz_brain import QuizBrain
from question_model import Question


def get_question_bank(data, text='text', answer='answer'):
    for question in data:
        question_bank.append(Question(question[text], question[answer]))


question_bank = []
get_question_bank(question_data1, 'question', 'correct_answer')
print(question_bank[0].text)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_qustion()
print(f'You\'ve completed the quiz ')
print(f'Your final score was : {quiz.true_answar}/{quiz.question_numbre}')
