#ranomly choose a word from the animals list
import random
#welcome message
print('''Hi there, let's play the Hangman game! If you're not familiar with the rules, you can visit the following link to learn how to play: "https://en.wikipedia.org/wiki/Hangman_(game)".\n
We'll be guessing the name of an animal. You need to guess one letter from the animal's name. Let's get started!''')

animals_list = [
    "cat", "dog", "cow", "pig", "fox",
    "bat", "ant", "bee", "dolphin", "rat",
    "owl", "duck", "goat", "frog", "fish",
    "bear", "deer", "lion", "elephant", "crab"
]
secret_word = random.choice(animals_list)
print(secret_word)

# creating a placeholder with the same numbers of blanks as secret_word
placeholder = ""
for position in range (0,len(secret_word)):
    placeholder += "_"
print(placeholder)

# main_score = 10
# balance = main_score

game_over = False
correct_letters = []

while not game_over:
    user_input = str(input(f"what is your guess? ")).lower()
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

    if "_" not in display:
        game_over = True
        print(f"\n🎉 Congratulations! You guessed it right: {secret_word}")