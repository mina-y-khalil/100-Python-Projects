from data import resources,MENU

drink_is_dispensed = True

while drink_is_dispensed:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        print("Turn off the machine ... ")
        drink_is_dispensed = False
        break
    elif user_order == "report":
        print(resources)