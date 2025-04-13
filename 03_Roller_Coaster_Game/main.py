print ("welcome to the Roller Coaster ")
height = int(input("what is the height? "))
# nested if
if height >= 120:
    if (int(input("what is your age? "))) >= 18:
        print("you have to pay full ticket this will cost $20")
    else:
        print("Good news! you will pay only half ticket $10")
else:
    print("sorry! you are too short to play the game it is not safe for you")