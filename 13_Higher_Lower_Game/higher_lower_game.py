from art import logo,vs
from game_data import data
import random

print(logo)
still_correct = True
a_choice = random.choice(data)
b_choice = random.choice(data)
points = 0

def if_correct():
     print(f"you are correct and your points now is {points}")
     print(f"compare now A: {user_choice} and B:{b_choice[0]} {b_choice[2]} from {b_choice[3]}")

while still_correct:
        print(f"Compare A: {a_choice[0]} {a_choice[2] } from {a_choice[3]} ")
        print(vs)
        print(f"Against B: {b_choice[0] } {b_choice[2]} from {b_choice[3]}")
        user_choice = (input("Who has the more followers? Type 'A' or 'B'").lower())
        if a_choice[1] > b_choice[1] and user_choice == a_choice[1]:
            points += 1
            if_correct()
        elif a_choice[1] < b_choice[1] and user_choice == b_choice[1]:
            points += 1
            if_correct()
        else:
            print(f"you lost and your score is {points}")
            still_correct = False




