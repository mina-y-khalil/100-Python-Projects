class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list

    def still_has_questions(self):
        return self.q_number < len(self.q_list) #this will return True or False to manage the while loop in main.py

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        input(f"Q{self.q_number}: {current_question.text} (True/False): ")



