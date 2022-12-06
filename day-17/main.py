from data import question_data, new_question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(item['text'], item['answer']) for item in question_data]
question_bank = [Question(item['question'], item['correct_answer']) for item in new_question_data]
print((question_bank[0]).text)
#quizmaster = QuizBrain(question_bank)
#while quizmaster.still_has_question():
#    quizmaster.next_question()
#
#quizmaster.result()
