# asking the questions 
# checking whether answer is correct
# checking if we're at the end of quiz 

class QuizBrain:
    # constructor for quiz brain
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list 
        self.score = 0

    def get_next_question(self):
        ques_obj = self.q_list[self.q_number]
        question = ques_obj.text 
        answer = ques_obj.answer
        self.q_number += 1
        user_input = input(f"{self.q_number}. {question} (True / False): ") 

        if user_input == answer:
            self.score += 1
            print(f"You got the question right!")
        else:
            print(f"You got the question wrong!")
        print(f"Current score : {self.score}/{self.q_number}")
    
    def check_end_of_quiz(self):
        if self.q_number < len(self.q_list):
            return False
        print(f"Quiz Ended!")
        print(f"Your Score : {self.score}/{len(self.q_list)}")
        return True
