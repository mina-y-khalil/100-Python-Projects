print ("welcome to the Roller Coaster ")
height = int(input("what is the height? "))
# price list
bill = 0
adult_tickets = 25
youth_tickets = 20
child_tickets = 10
picture_price = 3

# nested if
if height >= 120:
    if (int(input("what is your age? "))) <= 12:
        bill = child_tickets
        print(f"Child tickets are ${bill}")
    elif height <= 18:
        bill = youth_tickets
        print(f"Youth tickets are ${bill}")
    else:
        bill = adult_tickets
        print(f"Adult tickets are ${bill}")
    wants_photo = input(f"Do you want to have a photo take for extra ${picture_price}? Type y for yes and n for No. ")
    if wants_photo == "y":
        print(f"Your total bill now is ${bill+picture_price}")
    else:
        print(f"Ok, your total bill is ${bill}")

else:
    print("sorry! you are too short to play the game it is not safe for you")
