def check_answer(user_answer, correct_answer):
    user_answer = user_answer.lower()
    if user_answer == 'f':
        user_answer = 'false'
    elif user_answer == 't':
        user_answer = 'true'
    else:
        print("Incorrect input.")
    correct_answer = correct_answer.lower()
    print(f"The correct answer is {correct_answer}")
    return user_answer == correct_answer


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?")
        if check_answer(answer, question.answer):
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def result(self):
        print("You've completed the quiz")
        print(f"Your final score is {self.score}/{self.question_number}\n")

