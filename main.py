# import data
import question_model
from quiz_brain import QuizBrain
import requests

api_url = "https://opentdb.com/api.php?amount=50&difficulty=medium&type=boolean"
question_bank = []

try:
    response = requests.get(api_url)
    response.raise_for_status()

    data = response.json()

    for num in range(0, len(data['results'])):
        new_q = question_model.Question(text=data['results'][num]["question"],
                                        answer=data['results'][num]["correct_answer"])
        question_bank.append(new_q)


except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching data from the API: {e}")

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")