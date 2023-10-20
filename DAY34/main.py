from requests.models import Response

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}
# response = requests.get(url='https://opentdb.com/api.php', params=parameters)
# question_data = response.json()['results']
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
interface = QuizInterface(quiz, len(question_bank))