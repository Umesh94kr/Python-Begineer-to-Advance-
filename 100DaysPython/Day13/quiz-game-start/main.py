from data import question_data 
from question_model import Question
from quiz_brain import QuizBrain

# question_bank - will be a list of Question object
question_bank = [] 
from data import question_data

for q in question_data:
    question_object = Question(q['text'], q['answer'])
    question_bank.append(question_object)

########## WRITE THE MAIN LOGIC ############
quiz = QuizBrain(question_bank)

while(quiz.check_end_of_quiz() == False):
    quiz.get_next_question()
