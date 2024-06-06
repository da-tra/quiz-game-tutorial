# from question_model import Question
# from data import question_data

# TODO asking the question
# TODO checking if the answer was correct
# TODO checking if it's the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number + 1}: {current_question.text}: (True / False) ")
 
