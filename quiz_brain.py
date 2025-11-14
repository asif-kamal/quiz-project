class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer.lower()

        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").lower()
        self.check_answer(answer, correct_answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print("The correct answer is %s." % correct_answer)
        print("Score: %d/%d" % (self.score, self.question_number))
        print("\n")
