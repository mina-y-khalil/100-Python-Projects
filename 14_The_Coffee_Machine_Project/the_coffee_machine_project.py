from data import resources,MENU,profit

is_on = True

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

while is_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        print("Turning off the machine ... 💤 ")
        is_on = False
        break
    elif user_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_order]
        if is_resource_sufficient(drink["ingredients"]):
            process_coins()


