import data
import question_model
from quiz_brain import QuizBrain

question_bank = []
for num in range(0, len(data.question_data)):
    new_q = question_model.Question(text=data.question_data[num]["text"],
                                    answer=data.question_data[num]["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz.next_question()