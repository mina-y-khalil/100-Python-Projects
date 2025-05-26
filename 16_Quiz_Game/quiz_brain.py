class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list) #this will return True or False to manage the while loop in main.py

    def next_question(self):
        current_question = self.q_list[self.q_number] #this is a class
        self.q_number += 1
        user_answer = input(f"Q{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
        else:
            print("Sorry! your answer is wrong.")
        print(f"The correct answer was: {current_answer}")
        print(f"Your current score is: {self.score}/{self.q_number}")





