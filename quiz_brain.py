class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_q_number = self.question_number + 1
        input(f"Q.{current_q_number}: {current_question.text} (True/False)? ")
