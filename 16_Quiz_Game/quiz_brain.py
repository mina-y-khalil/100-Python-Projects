class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list

    def next_question(self):
        current_question = self.q_list[self.q_number]
        input(f"Q{self.q_number}: {current_question.text} (True/False): ")