from data import questions_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(item['question'], item['correct_answer']) for item in questions_data]
quiz_master = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz_master)
