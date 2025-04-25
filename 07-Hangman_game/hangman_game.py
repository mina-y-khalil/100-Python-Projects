#ranomly choose a word from the animals list
import random
from hangman_words import animals_list
from hangman_art import hangman_stages, logo
#welcome message
print(logo)
print('''Hi there, let's play the Hangman game! If you're not familiar with the rules, you can visit the following link to learn how to play: "https://en.wikipedia.org/wiki/Hangman_(game)".\n
We'll be guessing the name of an animal. You need to guess one letter from the animal's name. Let's get started!''')

secret_word = random.choice(animals_list)
print(secret_word)

# creating a placeholder with the same numbers of blanks as secret_word
placeholder = ""
for position in range (0,len(secret_word)):
    placeholder += "_"
print(placeholder)

main_score = len(hangman_stages) -1
# print(main_score)
balance = main_score

game_over = False
correct_letters = []

while not game_over:
    user_input = str(input(f"what is your guess? ")).lower()
    if user_input in correct_letters:
        print(f"You've already guessed letter '{user_input}' before 😉")
    display = ""
    for letter in secret_word:
        if letter == user_input:
            display += letter
            correct_letters.append(user_input)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if user_input not in secret_word:
        balance -= 1
        print(f"Wrong guess 😭 Remaining score: {balance}/{main_score}")
        print(hangman_stages[main_score-balance])
        if balance == 0:
            game_over = True
            print(hangman_stages[-1])
            print(f"\n💀 Game Over! The correct word was: {secret_word}")


    if "_" not in display:
        game_over = True
        print(f"\n🎉 Congratulations! You guessed it right: {secret_word}")