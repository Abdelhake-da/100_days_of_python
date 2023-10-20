def answar_fun(answar):
    if answar == 't' or answar == 'true':
        return 'True'
    elif answar == 'f' or answar == 'false':
        return 'False'
class QuizBrain:
    def __init__(self, question_list):
        self.true_answar = 0
        self.question_numbre = 0
        self.question_list = question_list

    def next_qustion(self):
        question = self.question_list[self.question_numbre]
        self.question_numbre += 1
        answar = input(f'Q.{self.question_numbre} - {question.text} (True or False) ?').lower()
        if answar_fun(answar) == question.answar:
            self.true_answar += 1
            print('You got it right!')
            print(f'Your current score is : {self.true_answar}/{self.question_numbre}')
        else:
            print('That\'s wrong.')
            print(f'The correct answer was : {question.answar}')
            print(f'Your current score is : {self.true_answar}/{self.question_numbre}')
        print('\n')
    def still_has_questions(self):
        if self.question_numbre < len(self.question_list):
            return True
        else:
            return False
