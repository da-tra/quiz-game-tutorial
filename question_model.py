#create a Question class with an __init()__ method with two attributes: TEXT and ANSWER
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# question_1 = Question("The Backstreet Boys had 4 members.", "False")

# print(question_1.text, question_1.answer)