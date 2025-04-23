#ranomly choose a word from the animals list
import random
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
placeholder = ""

for position in range (0,len(secret_word)):
    placeholder += "_"
# print(placeholder)

main_score = 10
balance = main_score
display = ""

while balance != 0:
    user_input = str(input(f"what is your guess? ")).lower()
    if user_input not in secret_word:
        display += "_"
        balance -= 1
        print(f"you lost one of your life 😭 your remaining score is {balance}/{main_score} {display}")

    else:
        for letter in secret_word:
            if letter == user_input:
                display += letter
        print(f"You have selected a correct letter 🤩 {display}")


print("GAME OVER 🥲")