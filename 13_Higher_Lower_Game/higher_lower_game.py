from art import logo,vs
from game_data import data
import random

print(logo)
still_correct = True

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def is_correct(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
       return user_guess == "a"
    else:
        return user_guess == "b"

a_choice = random.choice(data)

score = 0


while still_correct:
    b_choice = random.choice(data)
    if a_choice == b_choice:
        b_choice = random.choice(data)
        print(f"Compare A: {format_data(a_choice)} ")
        print(vs)
        print(f"Against B: {format_data(b_choice)}")
        user_choice = (input("Who has the more followers? Type 'A' or 'B' ").lower())

        #check if the user is correct.
        a_follower_count = a_choice["follower_count"]
        b_follower_count = b_choice["follower_count"]
        is_correct(user_choice,a_follower_count,b_follower_count)
        if is_correct(user_choice,a_follower_count,b_follower_count):
            a_choice = b_choice
            score += 1
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            still_correct = False




