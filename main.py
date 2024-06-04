from question_model import Question
from data import question_data

#write a for loop to iterate over the question_data.
# create a question object from each entry in question_data.
# append each question to the data bank.

question_bank = []


#pair = question_data[i]

for i in [0, len(question_data) - 1]:
    q_dic = question_data[i]
    text = q_dic["text"]
    answer = q_dic["answer"]
    question = Question(text, answer)
    question_bank.append(question)

print(question_bank)

# question_1 = Question("The Backstreet Boys had 4 members.", "False")

# question_bank = [
    # Question(q1, a1),
# ]