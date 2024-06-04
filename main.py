from question_model import Question
from data import question_data

#write a for loop to iterate over the question_data.
# create a question object from each entry in question_data.
# append each question to the data bank.

question_bank = []

for q in question_data:
    question = Question()
    question(q, question_data[q])
    question_bank.append(question)
#     append ...

# question_1 = Question("The Backstreet Boys had 4 members.", "False")

# question_bank = [
    # Question(q1, a1),
# ]