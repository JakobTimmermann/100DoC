import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)} (True/False)?"

    def check_answer(self, user_answer):
        user_answer = user_answer.lower()
        correct_answer = self.current_question.answer
        correct_answer = correct_answer.lower()
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False

    def still_has_question(self):
        return self.question_number < len(self.question_list)
