from question_model import Question
from data import question_data

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

print(question_bank[0].text)

# question_1 = Question("The Backstreet Boys had 4 members.", "False")

# question_bank = [
    # Question(q1, a1),
# ]