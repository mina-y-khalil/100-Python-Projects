from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#using the blueprint of the classes and assign it to new variables
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like {options}: ").lower()
    if choice == "off":
        is_on = False
        print ("Turning off the machine ... 😴")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(coffee_maker.is_resource_sufficient(drink))

