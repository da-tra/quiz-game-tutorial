from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#write a for loop to iterate over the question_data.
# create a question object from each entry in question_data.
# append each question to the data bank.

question_bank = []


#pair = question_data[i]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
quiz = QuizBrain(question_bank)
quiz.next_question