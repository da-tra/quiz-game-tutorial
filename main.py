from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# write a for loop to iterate over the question_data.
# create a question object from each entry in question_data.
# append each question to the data bank.

question_bank = []


# pair = question_data[i]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
quiz = QuizBrain(question_bank)

# print(quiz.question_number)

while quiz.still_has_questions():
    quiz.next_question()

    # quiz.question_number += 1
print("You've completed the quiz.")
print(f"Your final score is {quiz.score} / {quiz.question_number}.")