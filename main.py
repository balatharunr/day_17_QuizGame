from question_model import Questions
from data import question_data
from quiz_brain import Quiz_Brain


question_bank = []
for dict in question_data:
    question = Questions(dict["text"], dict["answer"])
    question_bank.append(question)

quiz = Quiz_Brain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
    