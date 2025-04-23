secret_word = "python"
balance = 6
while balance != 0:
    user_input = str(input("what is your guess? ")).lower()
    if user_input in secret_word:
        print ("You have selected a correct letter 🤩")
    elif user_input not in secret_word:
        balance -=1
        print(f"you lost one of your life your remaining score is {balance}/6")
print("GAME OVER 🥲")